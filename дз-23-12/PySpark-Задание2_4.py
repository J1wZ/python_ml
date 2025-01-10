from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import concat_ws

spark = SparkSession.builder.master("local").getOrCreate()

#API
df_orders = spark.read.csv("CVS\\orders.csv", inferSchema=True, header=True, sep=",")
df_order_items = spark.read.csv("CVS\\order_items.csv", inferSchema=True, header=True, sep=",")
df_customers = spark.read.csv("CVS\\customers.csv", inferSchema=True, header=True, sep=",")

df_res = df_customers.join(df_orders, 
                           df_orders["customer_id"] == df_customers["customer_id"], "inner")

df_res = df_res.join(df_order_items, 
                           df_order_items["order_id"] == df_res["order_id"], "inner")

df_res = df_res.groupBy(concat_ws(" ",df_customers["first_name"], 
              df_customers["last_name"])
                        ).agg(
                        F.sum(df_res["quantity"] * 
                        (df_res["list_price"] * 
                         (1-df_res["discount"]))
                         ).alias("Total_Money_Spent")
                         ).withColumnRenamed("concat_ws( , first_name, last_name)", "Customer")

df_res.orderBy(F.desc("Total_Money_Spent")).show(5)
#spark.sql
df_orders.createOrReplaceTempView("orders")
df_order_items.createOrReplaceTempView("order_items")
df_customers.createOrReplaceTempView("customers")

spark.sql("""
        SELECT CONCAT_WS(' ',customers.first_name, customers.last_name) as Customer,
                sum(order_items.quantity * (order_items.list_price * (1 - order_items.discount))) AS Total_Money_Spent
        FROM customers
        inner join orders on orders.customer_id = customers.customer_id
        inner join order_items on order_items.order_id = orders.order_id
        GROUP BY Customer
        order by Total_Money_Spent
        DESC LIMIT 5;
          """).show()
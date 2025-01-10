from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.master("local").getOrCreate()

#API
df_orders = spark.read.csv("CVS\\orders.csv", inferSchema=True, header=True, sep=",")
df_order_items = spark.read.csv("CVS\\order_items.csv", inferSchema=True, header=True, sep=",")

df_res = df_orders.join(df_order_items, 
                           df_order_items["order_id"] == df_orders["order_id"], "inner")


df_res = df_res.groupBy(F.month("order_date")
                        ).agg(
                        F.count("product_id").alias("Total Number of Orders"),
                        F.sum(df_order_items["quantity"] * 
                        (df_order_items["list_price"] * 
                         (1-df_order_items["discount"]))
                         ).alias("Total sales")).withColumnRenamed("month(order_date)", "Month")

df_res.orderBy("Month").show()
#spark.sql
df_orders.createOrReplaceTempView("orders")
df_order_items.createOrReplaceTempView("order_items")

spark.sql("""
            SELECT month(orders.order_date) AS Month,
                    count(orders.order_id) AS Total_Number_of_Orders,
                    sum(order_items.quantity * (order_items.list_price * (1 - order_items.discount))) AS Total_Sales
            FROM orders
            inner join order_items on order_items.order_id = orders.order_id
            GROUP BY Month
            ORDER BY Month;
          """).show()
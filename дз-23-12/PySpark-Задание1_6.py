from pyspark.sql import SparkSession
from pyspark.sql.functions import concat_ws

spark = SparkSession.builder.master("local").getOrCreate()

#API
df_customers = spark.read.csv("CVS\\customers.csv", inferSchema=True, header=True, sep=",")
df_orders = spark.read.csv("CVS\\orders.csv", inferSchema=True, header=True, sep=",")

df_res = df_customers.join(df_orders, 
                           df_orders["customer_id"] == df_customers["customer_id"], "inner")

df_res = df_res.select(
    concat_ws(" ",df_customers["first_name"], 
              df_customers["last_name"]).alias("customer"))
df_res = df_res.groupBy("customer").count()

df_res.show()
#spark.sql
df_customers = spark.read.csv("CVS\\customers.csv", inferSchema=True, header=True, sep=",")
df_orders = spark.read.csv("CVS\\orders.csv", inferSchema=True, header=True, sep=",")


df_customers.createOrReplaceTempView("customers")
df_orders.createOrReplaceTempView("orders")

spark.sql("""
            SELECT CONCAT_WS(' ',customers.first_name, customers.last_name) as customer, COUNT(orders.order_id) as count
            FROM customers
            INNER JOIN orders ON orders.customer_id = customers.customer_id
            GROUP BY customer;
          """).show()
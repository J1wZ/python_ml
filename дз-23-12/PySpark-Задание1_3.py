from pyspark.sql import SparkSession
from pyspark.sql.functions import concat_ws

spark = SparkSession.builder.master("local").getOrCreate()

#API
from pyspark.sql.functions import concat_ws

df_customers = spark.read.csv("CVS\\customers.csv", inferSchema=True, header=True, sep=",")
df_orders = spark.read.csv("CVS\\orders.csv", inferSchema=True, header=True, sep=",")
df_stores = spark.read.csv("CVS\\stores.csv", inferSchema=True, header=True, sep=",")

df_res = df_customers.join(df_orders, 
                           df_orders["customer_id"] == df_customers["customer_id"])

df_res = df_res.join(df_stores, 
                     df_stores["store_id"] == df_orders["store_id"]
                     ).where(df_stores["store_name"] == 'Rowlett Bikes')

df_res = df_res.select(
    concat_ws(" ",df_customers["first_name"], 
              df_customers["last_name"]).alias("customer"),
              df_customers["email"], df_customers["phone"])

df_res.dropDuplicates().show()

#spark.sql
df_customers.createOrReplaceTempView("customers")
df_stores.createOrReplaceTempView("stores")
df_orders.createOrReplaceTempView("orders")

spark.sql("""
          SELECT CONCAT_WS(' ',customers.first_name, customers.last_name) as customer, customers.email, customers.phone
            FROM customers
            JOIN orders ON orders.customer_id = customers.customer_id
            JOIN stores ON stores.store_id = orders.store_id
            WHERE stores.store_name = 'Rowlett Bikes'
          """).dropDuplicates().show()
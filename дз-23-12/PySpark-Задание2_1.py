from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.master("local").getOrCreate()

#API
df_products = spark.read.csv("CVS\\products.csv", inferSchema=True, header=True, sep=",")
df_order_items = spark.read.csv("CVS\\order_items.csv", inferSchema=True, header=True, sep=",")

df_res = df_products.join(df_order_items, 
                           df_order_items["product_id"] == df_products["product_id"], "inner")


df_res = df_res.groupBy("product_name"
                        ).agg(F.sum
                        (df_order_items["quantity"] * 
                        (df_order_items["list_price"] * 
                         (1-df_order_items["discount"]))
                         ).alias("Total_sales"))

df_res.show()
#spark.sql
df_products.createOrReplaceTempView("products")
df_order_items.createOrReplaceTempView("order_items")

spark.sql("""
            Select  products.product_name , (SUM(order_items.quantity * (order_items.list_price * (1-order_items.discount)))) as total_sales
            FROM products
            Inner Join order_items on order_items.product_id = products.product_id
            Group by products.product_name
          """).show()
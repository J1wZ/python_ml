from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").getOrCreate()

#API
df_brands = spark.read.csv("CVS\\brands.csv", inferSchema=True, header=True, sep=",")

df_products = spark.read.csv("CVS\\products.csv", inferSchema=True, header=True, sep=",")

df_res = df_products.join(df_brands, df_brands["brand_id"] == df_products["brand_id"])
df_res = df_res.select("product_name", "brand_name")
df_res.show()

#spark.sql
df_brands.createOrReplaceTempView("brands")
df_products.createOrReplaceTempView("products")

spark.sql("""
          SELECT products.product_name, brands.brand_name 
            FROM products 
            JOIN brands ON brands.brand_id = products.brand_id
          """).show()
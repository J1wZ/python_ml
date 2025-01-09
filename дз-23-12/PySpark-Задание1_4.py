from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").getOrCreate()

#API
df_products = spark.read.csv("CVS\\products.csv", inferSchema=True, header=True, sep=",")
df_categories = spark.read.csv("CVS\\categories.csv", inferSchema=True, header=True, sep=",")

df_res = df_products.join(df_categories, 
                           df_categories["category_id"] == df_products["category_id"])


df_res = df_res.groupBy("category_name").count()

df_res.show()
#spark.sql
df_products.createOrReplaceTempView("products")
df_categories.createOrReplaceTempView("categories")

spark.sql("""
          SELECT categories.category_name, COUNT(products.product_id) as count
          FROM products
          JOIN categories ON categories.category_id = products.category_id
          GROUP BY categories.category_name;
          """).show()
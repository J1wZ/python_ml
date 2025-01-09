from pyspark.sql import SparkSession
from pyspark.sql.functions import concat_ws

spark = SparkSession.builder.master("local").getOrCreate()

#API
df_staffs = spark.read.csv("CVS\\staffs.csv", inferSchema=True, header=True, sep=",")

df_stores = spark.read.csv("CVS\\stores.csv", inferSchema=True, header=True, sep=",")

df_res = df_staffs.join(df_stores, df_stores["store_id"] == df_staffs["store_id"]).where(df_staffs["active"] == 1)
df_res = df_res.select(concat_ws(" ",df_staffs["first_name"], df_staffs["last_name"]).alias("staff"),"store_name")
df_res.orderBy(['staff'], ascending = [True]).show()

#spark.sql
df_staffs.createOrReplaceTempView("staffs")
df_stores.createOrReplaceTempView("stores")

spark.sql("""
          SELECT CONCAT_WS(' ',staffs.first_name, staffs.last_name) as staff, stores.store_name
          FROM staffs
          JOIN stores ON stores.store_id = staffs.store_id
          WHERE staffs.active = 1
          order by staff
          """).show()
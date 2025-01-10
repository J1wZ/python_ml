from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").getOrCreate()

#API
df_orders = spark.read.csv("CVS\\orders.csv", inferSchema=True, header=True, sep=",")

df_res = df_orders.groupBy("order_status").count()

df_res.orderBy(['order_status'], ascending = [True]).show()
#spark.sql
df_orders.createOrReplaceTempView("orders")

spark.sql("""
            Select orders.order_status, count(orders.order_id) as order_count
            from orders
            group by orders.order_status
            order by orders.order_status;
          """).show()
# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.window import *

# COMMAND ----------

# MAGIC %fs ls '/mnt/raw/'

# COMMAND ----------

df = spark.read.option('multiline', 'true').json('/mnt/raw/json/ye_quotes.json')
df1 = spark.read.option('multiline', 'true').json('/mnt/raw/json/ye_quotes1.json')

# COMMAND ----------

df.write.mode('overwrite').saveAsTable('quotes')
df1.write.mode('append').saveAsTable('quotes')

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC CREATE OR REPLACE table quotes
# MAGIC AS
# MAGIC SELECT DISTINCT *
# MAGIC FROM default.quotes;
# MAGIC 
# MAGIC SELECT distinct * FROM quotes

# COMMAND ----------

df = spark.sql('SELECT * FROM quotes')
df = df.withColumn("monotonically_increasing_id", monotonically_increasing_id())
window = Window.orderBy(col('monotonically_increasing_id'))
dfc = df.withColumn('increasing_id', row_number().over(window))
display(dfc)

# COMMAND ----------

dfc = dfc.select('increasing_id', 'quote')
dfc = dfc.withColumnRenamed("increasing_id", "Id") \
         .withColumnRenamed("quote", "Quote")
dfc.write.mode('overwrite').saveAsTable('quotes')
display(dfc)

# COMMAND ----------

# MAGIC %sql 
# MAGIC 
# MAGIC select * from quotes

# COMMAND ----------

dfc.write.json('/mnt/clean/json/all_kanye_quotes')

# COMMAND ----------

data_location = "/mnt/clean/json/all_kanye_quotes"
files = dbutils.fs.ls(data_location)
file = [x.path for x in files if x.path.endswith(".json")][0]
dbutils.fs.mv(file, data_location.rstrip('/') + ".json")
dbutils.fs.rm(data_location, recurse = True)

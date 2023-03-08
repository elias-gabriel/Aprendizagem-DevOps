# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession.builder.config("spark.databricks.delta.catalog.enabled", "true").getOrCreate()

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC CREATE DATABASE 1_raw

# COMMAND ----------

arquivos = dbutils.fs.ls('/mnt/')
display(arquivos)

# COMMAND ----------

for arquivo in arquivos:
    table_name = arquivo.name
    if table_name.endswith('.parquet'):
        file_path = arquivo.path
        delta_path = f'/mnt/{table_name}'
        try:
            schema, name = table_name.split('.')[:-1]
            full_name = f'{schema}.{name}'
            flag = spark.sql(f"SHOW TABLES FROM 1_raw LIKE '{name}'")
            
            if flag.rdd.isEmpty():
                df = spark.read.format('parquet').load(file_path)
                # Rename any columns that have invalid characters or names
                for col_name in df.columns:
                    new_name = col_name.replace('-', '_')
                    if new_name != col_name:
                        df = df.withColumnRenamed(col_name, new_name)
                df.write.option("overwriteSchema", "true").mode("overwrite").format('delta').saveAsTable(f'1_raw.{name}', path=delta_path)
                print(f"Successfully created Delta table {name}")
            else:
                print(f"Delta table {name} already exists")
        except ValueError as ve:
            print(f"ValueError: {ve}")
            import traceback
            traceback.print_exc()
    else:
        print('File is not a parquet file:', table_name)


# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC show tables from 1_raw

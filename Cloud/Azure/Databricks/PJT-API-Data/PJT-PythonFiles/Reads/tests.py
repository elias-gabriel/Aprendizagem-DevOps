# Databricks notebook source
#spark.conf.set("parquet.enable.summary-metadata", "false")
#spark.conf.set("mapreduce.fileoutputcommitter.marksuccessfuljobs", "false")


# COMMAND ----------

#read_all_teams
ds = spark.read.option("multiline","true").json('/mnt/pjtdsd/raw/all_teams.json')
#display(ds)

# COMMAND ----------

from pyspark.sql.functions import explode
ex = (ds.select(explode(ds.data)))
#display(ex)

# COMMAND ----------

from pyspark.sql.types import ArrayType, StructType

def flatten(df, sentinel="x"):
    def _gen_flatten_expr(schema, indent, parents, last, transform=False): 
        def handle(field, last):
            path = parents + (field.name,)
            alias = (
                " as "
                + "_".join(path[1:] if transform else path)
                + ("," if not last else "")
            )
            if isinstance(field.dataType, StructType):
                yield from _gen_flatten_expr(
                    field.dataType, indent, path, last, transform
                )
            elif (
                isinstance(field.dataType, ArrayType) and
                isinstance(field.dataType.elementType, StructType)
            ):
                yield indent, "transform("
                yield indent + 1, ".".join(path) + ","
                yield indent + 1, sentinel + " -> struct("
                yield from _gen_flatten_expr(
                    field.dataType.elementType, 
                    indent + 2, 
                    (sentinel,), 
                    True, 
                    True
                )
                yield indent + 1, ")"
                yield indent, ")" + alias
            else:
                yield (indent, ".".join(path) + alias)

        try:
            *fields, last_field = schema.fields
        except ValueError:
            pass
        else:
            for field in fields:
                yield from handle(field, False)
            yield from handle(last_field, last)

    lines = []
    for indent, line in _gen_flatten_expr(df.schema, 0, (), True):
        spaces = " " * 4 * indent
        lines.append(spaces + line)

    expr = "struct(" + "\n".join(lines) + ") as " + sentinel
    return df.selectExpr(expr).select(sentinel + ".*")

# COMMAND ----------

ff = flatten(ex)
display(flatten(ex))


# COMMAND ----------

ff = ff.drop("col_full_name")
display(ff)

# COMMAND ----------

data_location = "/mnt/pjtdsd/clean"

files = dbutils.fs.ls(data_location)
csv_file = [x.path for x in files if x.path.endswith(".csv")][0]
dbutils.fs.mv(csv_file, data_location.rstrip('/') + ".csv")
dbutils.fs.rm(data_location, recurse = True)

# COMMAND ----------

df = flatten(ex)
df.write.saveAsTable("all_teams")

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC drop table if exists all_teams

# COMMAND ----------

#df = flatten(ex)
#df.write.parquet('/mnt/stgaccpjt/clean/all_teams.parquet')
pq = spark.read.parquet('/mnt/stgaccpjt/clean/all_teams.parquet')
#df.write.saveAsTable("all_teams")
display(pq)

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select * from all_teams LIMIT 30

# COMMAND ----------

# MAGIC %run ../set-up-sql

# COMMAND ----------

df.write \
  .format('com.databricks.spark.sql') \
  .option("url", f"jdbc:sqlserver://{ServerName}.database.windows.net;database={DbName}") \
  .option("user", UserName) \
  .option("password", Password) \
  .option("tempDir", f"wasbs://{ContainerName}@{ACCOUNT}.blob.core.windows.net/Files") \
  .option('foward_spark_azure_storage_credentials', 'true')
  .option("dbtable", "dbo.all_teams") \
  .mode("overwrite") \
  .save()

# COMMAND ----------

#transformedmydf = mydf.withColumnRenamed("[NOME_ANTIGO]", "[NOME_NOVO]")

# COMMAND ----------

transformedmydf = df.withColumnRenamed("col_abbreviation", "abrevi")
display(transformedmydf)

# COMMAND ----------

#ransformedmydf.write.json('/mnt/stgaccpjt/clean/all_teams.json')
#l = spark.read.json('/mnt/stgaccpjt/clean/all_teams.json')
display(jl)

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/mnt/stgaccpjt/clean/'

# COMMAND ----------

#jn = flatten(ex)
#jn.write.json('/mnt/stgaccpjt/clean/all_teams.json')
jnl = spark.read.json('/mnt/stgaccpjt/clean/all_teams.json')
display(jnl)



# COMMAND ----------

jnl = spark.read.csv('/mnt/stgaccpjt/clean/teste.csv', header='true')
display(jnl)

# COMMAND ----------

jnl = spark.read.parquet('/mnt/stgaccpjt/clean/games.parquet')
display(jnl)

# COMMAND ----------


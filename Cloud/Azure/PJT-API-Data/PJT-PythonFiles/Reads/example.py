# Databricks notebook source
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

ex = flatten(ex)
display(ex)

# COMMAND ----------

transformedColumn = ex.withColumnRenamed("col_abbreviation", "Abbreviation") \
                      .withColumnRenamed("col_city", "City") \
                      .withColumnRenamed("col_conference", "Conference") \
                      .withColumnRenamed("col_division", "Division") \
                      .withColumnRenamed("col_full_name", "Full_Name") \
                      .withColumnRenamed("col_id", "Id") \
                      .withColumnRenamed("col_name", "Name")
display(transformedColumn)


# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC drop table if exists all_teams

# COMMAND ----------

transformedColumn.write.saveAsTable("all_teams")
dbutils.fs.rm('/mnt/pjtdsd/clean/json/all_teams/', recurse = True)
transformedColumn.write.json('/mnt/pjtdsd/clean/json/all_teams')

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/mnt/pjtdsd/clean/json/'

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select * from all_teams

# COMMAND ----------

read = spark.read.json('/mnt/pjtdsd/clean/json/all_teams.json')
display(read)

# COMMAND ----------

data_location = "/mnt/pjtdsd/clean/json/all_teams/"
files = dbutils.fs.ls(data_location)
file = [x.path for x in files if x.path.endswith(".json")][0]
dbutils.fs.mv(file, data_location.rstrip('/') + ".json")
dbutils.fs.rm(data_location, recurse = True)

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/mnt/pjtdsd/clean/json/all_teams.json'

# COMMAND ----------

#pq = spark.read.parquet('/mnt/stgaccpjt/clean/parquet/all_teams.parquet')
#display(pq)

# COMMAND ----------


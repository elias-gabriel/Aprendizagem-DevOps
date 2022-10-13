# Databricks notebook source
from pyspark.sql.functions import explode

# COMMAND ----------

df = spark.read.option('multiline', 'true').json('/mnt/raw/json/advice_data.json')
display(df)

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

ex = flatten(df)
display(ex)

# COMMAND ----------

df = ex.drop("message_text", "message_type")
df = df.na.drop("all") # dropar linha com valores nulos de todas as colunas
df = df.select('slip_id', 'slip_advice')
display(df)

# COMMAND ----------

df = df.withColumnRenamed("slip_id", "Id") \
       .withColumnRenamed("slip_advice", "Advice")


# COMMAND ----------

df.write.mode('overwrite').saveAsTable('advices')

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC SELECT distinct * FROM advices

# COMMAND ----------

df.write.json('/mnt/clean/json/advice_data')

# COMMAND ----------

data_location = "/mnt/clean/json/advice_data"
files = dbutils.fs.ls(data_location)
file = [x.path for x in files if x.path.endswith(".json")][0]
dbutils.fs.mv(file, data_location.rstrip('/') + ".json")
dbutils.fs.rm(data_location, recurse = True)

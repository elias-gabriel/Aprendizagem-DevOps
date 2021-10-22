# Databricks notebook source
#read_all_teams
ds = spark.read.option("multiline","true").json('/mnt/pjtdsd/raw/all_games.json')
#display(ds)

# COMMAND ----------

from pyspark.sql.functions import explode
ex = (ds.select(explode(ds.data)))
display(ex)

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

transformedColumn = ex.withColumnRenamed("col_date", "Date") \
                      .withColumnRenamed("col_home_team_abbreviation", "Home_Team_Abbreviation") \
                      .withColumnRenamed("col_home_team_city", "Home_Team_City") \
                      .withColumnRenamed("col_home_team_conference","Home_Team_Conference") \
                      .withColumnRenamed("col_home_team_division", "Home_Team_Division") \
                      .withColumnRenamed("col_home_team_full_name", "Home_Team_FullName") \
                      .withColumnRenamed("col_home_team_id", "Home_TeamId") \
                      .withColumnRenamed("col_home_team_name", "Home_Team_Name") \
                      .withColumnRenamed("col_home_team_score", "Home_Team_Score") \
                      .withColumnRenamed("col_id", "Id") \
                      .withColumnRenamed("col_period", "Period") \
                      .withColumnRenamed("col_postseason", "Postseason") \
                      .withColumnRenamed("col_season", "Season") \
                      .withColumnRenamed("col_status", "Status") \
                      .withColumnRenamed("col_time", "Time") \
                      .withColumnRenamed("col_visitor_team_abbreviation", "Visitor_Team_Abbreviation") \
                      .withColumnRenamed("col_visitor_team_city", "Visitor_Team_City") \
                      .withColumnRenamed("col_visitor_team_conference", "Visitor_Team_Conference") \
                      .withColumnRenamed("col_visitor_team_division", "Visitor_Team_Division") \
                      .withColumnRenamed("col_visitor_team_full_name", "Visitor_Team_FullName") \
                      .withColumnRenamed("col_visitor_team_id", "Visitor_TeamId") \
                      .withColumnRenamed("col_visitor_team_name", "Visitor_Team_Name") \
                      .withColumnRenamed("col_visitor_team_score", "Visitor_Team_Score") \
  
transformedColumn = transformedColumn.drop("Time")
display(transformedColumn)

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC drop table if exists all_games

# COMMAND ----------

transformedColumn.write.saveAsTable("all_games")
dbutils.fs.rm('/mnt/pjtdsd/clean/json/all_games', recurse = True)
transformedColumn.write.json('/mnt/pjtdsd/clean/json/all_games')

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/mnt/pjtdsd/clean/json/'

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select * from all_games order by Id

# COMMAND ----------

data_location = "/mnt/pjtdsd/clean/json/all_games"
files = dbutils.fs.ls(data_location)
file = [x.path for x in files if x.path.endswith(".json")][0]
dbutils.fs.mv(file, data_location.rstrip('/') + ".json")
dbutils.fs.rm(data_location, recurse = True)

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/mnt/pjtdsd/clean/json/'

# COMMAND ----------

read = spark.read.json('/mnt/pjtdsd/clean/json/all_games.json')
display(read)

# COMMAND ----------

#pq = spark.read.parquet('/mnt/stgaccpjt/clean/parquet/all_games.parquet')
#display(pq)

# COMMAND ----------


# This code will take a specific table from Databricks and  write it on SQL Sever

server_name = "sql-elias"
jdbc_url = f"jdbc:sqlserver://{server_name}.database.windows.net"
port = "1433"
database = "<database_name>"
jdbc_username = "<sql_username>"
jdbc_password = "<sql_password>"
    
df.write \
  .format("jdbc") \
  .option("url", jdbc_url) \
  .option("port", port) \
  .option("dbtable", "table_from_databricks") \
  .option("database", database)  \
  .option("user", jdbc_username) \
  .option("password", jdbc_password) \
  .option("createTable", "true") \
  .mode("overwrite") \
  .save()


# This code will take the tables on the list and write them on SQL Sever

table_names = ["friends_info", "quotes", "advices"]

for table_name in table_names:
    df = spark.table(table_name)
    
    server_name = "<database_name>"
    jdbc_url = f"jdbc:sqlserver://{server_name}.database.windows.net"
    port = "1433"
    database = "<database_name>"
    jdbc_username = "<sql_username>"
    jdbc_password = "<sql_password>"
    
    df.write \
      .format("jdbc") \
      .option("url", jdbc_url) \
      .option("port", port) \
      .option("dbtable", table_name) \
      .option("database", database) \
      .option("user", jdbc_username) \
      .option("password", jdbc_password) \
      .option("createTable", "true") \
      .mode("overwrite") \
      .save()
    
# You can also use Key Vault

table_names = ["table_1", "table_2", "table_3"]

for table_name in table_names:
    df = spark.table(table_name)
    
    server_name = "<database_name>"
    jdbc_url = f"jdbc:sqlserver://{server_name}.database.windows.net"
    port = "1433"
    database = "<database_name>"
    jdbc_username = "<sql_username>"
    jdbc_password = dbutils.secrets.get(scope='scope_name', key='SQLPasswd')
    
    df.write \
      .format("jdbc") \
      .option("url", jdbc_url) \
      .option("port", port) \
      .option("dbtable", table_name) \
      .option("database", database) \
      .option("user", jdbc_username) \
      .option("password", jdbc_password) \
      .option("createTable", "true") \
      .mode("overwrite") \
      .save

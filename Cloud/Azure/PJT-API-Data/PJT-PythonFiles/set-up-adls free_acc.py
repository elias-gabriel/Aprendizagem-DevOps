# Databricks notebook source
storage_account_name = 'pjtdsd'
client_id = '235ca3be-c14a-4651-886f-a0071149f661'
tenant_id = 'e5056ff4-e962-4509-9b70-8670ce3b1435'
client_secret = 'pJn7Q~GaESfDb3TDULxY~PekG6LPt3OTKH.O5'


# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{client_id}",
           "fs.azure.account.oauth2.client.secret": f"{client_secret}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

# COMMAND ----------

container_name = "raw"
dbutils.fs.mount(
  source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
  mount_point = f"/mnt/{storage_account_name}/{container_name}",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls('/mnt/pjtdsd/raw')

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/mnt/pjtdsd/raw'

# COMMAND ----------

def mount_adls(container_name):
  dbutils.fs.mount(
    source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storage_account_name}/{container_name}",
    extra_configs = configs)

# COMMAND ----------

mount_adls('clean')

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/mnt/pjtdsd/clean'

# COMMAND ----------


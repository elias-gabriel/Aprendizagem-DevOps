#Configure Key Vault for Databricks

# Create your Key Vault and add the Secrets
# Add this in your main page of Databricks: secrets/createScope, shoud be like: https://adb-4xxxxxxxx.xx.azuredatabricks.net/?o=4961293589681410#secrets/createScope
# Scope Name: Chose a name for your Scope Name
# DNS Name: You will put the Key Vault URL: https://kv-xxx-xxx.vault.azure.net/
# Resource ID: In your Key Vault Main Page, go to PROPERTIES, then copy the Resource ID String: /subscriptions/xxx/xxx/xxx/xxx/xxx/xxx/xxx


# Get all Registereds Scopes on Databricks
dbutils.secrets.listScopes()

# Get all secrets of your Scope
dbutils.secrets.list('Scope_Name')

# Add the secret of the Scope in a variable 
secret = dbutils.secrets.get(scope='Scope_Name', key='Secret_Name')

# DO NOT DO THIS: List the Secret on Databricks
secret = dbutils.secrets.get(scope='Scope_Name', key='Secret_Name')

for row in secret:
    print(row)

# Using to Make a Connection With the Azure DataLake

storage_account_name = ''
client_id = dbutils.secrets.get(scope='Scope_Name', key='databricks-services-clientID')
tenant_id = dbutils.secrets.get(scope='Scope_Name', key='databricks-services-tenantID')
client_secret = dbutils.secrets.get(scope='Scope_Name', key='databricks-services-clientSecret')
# Note: You will have to add those infos on the Key Vault First

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{client_id}",
           "fs.azure.account.oauth2.client.secret": f"{client_secret}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}


def mount_adls(containers):
    try:
        for container in containers:
            dbutils.fs.mount(
            source = f"abfss://{container}@{storage_account_name}.dfs.core.windows.net",
            mount_point = f"/mnt/{container}",
            extra_configs = configs)
    except ValueError as err:
        print(err)
        pass

      
      
def unmount_datalake(containers):
    try:
        for container in containers:
            dbutils.fs.unmount(f"/mnt/{container}/")
    except ValueError as err:
        print(err)
        pass
      
  containers = ["raw", "clean"]

  
  try:
    mount_adls(containers)
except:
    unmount_datalake(containers)
    mount_adls(containers)

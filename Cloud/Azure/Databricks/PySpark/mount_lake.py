storage_account_name = ""
client_id            = ""
tenant_id            = ""
client_secret        = ""


### KEY VAULT ###

storage_account_name = ''
client_id = dbutils.secrets.get(scope='SCOPE_NAME', key='SECRET_NAME')
tenant_id = dbutils.secrets.get(scope='SCOPE_NAME', key='sSECRET_NAME')
client_secret = dbutils.secrets.get(scope='SCOPE_NAME', key='SECRET_NAME')

### ### ###

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

containers = ["transient", "raw", "trusted", "refined"]

try:
    mount_adls(containers)
except:
    unmount_datalake(containers)
    mount_adls(containers)


mt = dbutils.fs.mounts()
display(mt)
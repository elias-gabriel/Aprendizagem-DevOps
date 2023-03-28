import requests
import json

def azuread_auth(tenant_id: str, client_id: str, client_secret: str, resource_url: str):
    """
    Authenticates Service Principal to the provided Resource URL, and returns the OAuth Access Token
    """
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
    payload= f'grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}&resource={resource_url}'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    access_token = json.loads(response.text)['access_token']
    return access_token

def get_purview_assets(data_catalog_name: str,azuread_access_token: str,table_name: str):
    url = f"https://{data_catalog_name}.purview.azure.com/catalog/api/search/query?api-version=2022-08-01-preview"

    headers = {
        'Authorization': f'Bearer {azuread_access_token}',
        'Content-Type': 'application/json'
        }

    payload="""{
            "keywords": null,
            "limit": 1000,
            "filter": {
                "and": [
                {
                    "attributeName": "qualifiedName",
                    "operator": "contains",
                    "attributeValue": "%s"
                }
                ]
            }
        }""" % (table_name)

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    return data['value']

tenant_id = ""
client_id = ""
client_secret = ""
resource_url = "https://purview.azure.net"
data_catalog_name = "<purview_account_name>"
azuread_access_token = azuread_auth(tenant_id,client_id,client_secret,resource_url)

table_name = ""
data  = get_purview_assets(data_catalog_name,azuread_access_token,table_name)
print(data)

import requests
import json

purview_account_name = ""

with open("token.txt", "r") as f:
    access_token = f.read().strip()

def get_data_by_table_name(table_name):
    api_url = f"https://{purview_account_name}.purview.azure.com/catalog/api/search/query?api-version=2022-08-01-preview"
    headers = {"Authorization": f"Bearer {access_token}",
               "Content-Type": "application/json"}

    request_body = {
    "searchText": f"qualifiedName:\"{table_name}\"",
    "searchMode": "All",
    "facets": [],
    "sortBy": "name",
    "sortOrder": "ascending",
    "pageSize": 1,  
    "skip": 0,
    "limit": 1  
    }


    try:
        get_data_request = requests.post(url=api_url, headers=headers, json=request_body)
        get_data_request.raise_for_status()

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:  # Unauthorized
            print("Error: Token expired. Please refresh the token and try again.")
        else:
            print(f"Error: An HTTP error occurred: {e}")
        return []

    data = get_data_request.json()

    if 'value' not in data:
        print(f"Error: 'value' key missing in response data:\n{data}")
        return []

    return data['value']

table_name = ""
data = get_data_by_table_name(table_name)

with open("results.json", "w", encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
#print(data)

for item in data:
    item_id = item['id']
    qualified_name = item['qualifiedName'].split("@")[0]
    name = item['name']
    type = item['entityType']
    
    print(f"\nid: {item_id}")
    print(f"qualifiedName: {qualified_name}")
    print(f"name: {name}")
    print(f"entityType: {type}")
    print("\n")

    
    #get the token here? https://github.com/elias-gabriel/Aprendizagem-DevOps/blob/master/Cloud/Azure/get_pur_token.ps1

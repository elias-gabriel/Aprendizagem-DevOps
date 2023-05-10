def get_purview_assets(data_catalog_name: str, azuread_access_token: str, table: str, source: str):
    url = f"https://{data_catalog_name}.purview.azure.com/catalog/api/search/query?api-version=2022-08-01-preview"

    headers = {
        'Authorization': f'Bearer {azuread_access_token}',
        'Content-Type': 'application/json'
    }

    # Construir a consulta de pesquisa
    if source.lower() == "sql":
        search_query = f"synapse {table}"
    else:
        search_query = f"datalake {source} tbl_raw_{source}_{table}"

    payload = {
        "keywords": search_query,
        "limit": 1
    }

    response = requests.request("POST", url, headers=headers, json=payload)
    data = response.json()

    return data

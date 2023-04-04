# pip install requests
# pip install pyapacheatlas

import requests
import json
import re
import time
from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import col, lit
from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core import AtlasProcess, PurviewClient, AtlasException
from pyspark.sql.functions import col, monotonically_increasing_id, row_number
from pyspark.sql.window import Window

guid_start = -1
row_start = 1

def create_lineage(source_guid, destination_guid):
    global guid_start
    global row_start

    auth = ServicePrincipalAuthentication(
        tenant_id = "",
        client_id = "",
        client_secret = ""
    )

    client = PurviewClient(
        account_name="",
        authentication=auth
    )
    
    process_qn = f'Notebook: Purview - Create Lineage {row_start}'
    process_type_name = 'Process'

    new_lineage = AtlasProcess(
        name= f'Notebook Processing {row_start}',
        typeName=process_type_name,
        qualified_name=process_qn,
        inputs=[{"guid": source_guid}],
        outputs=[{"guid": destination_guid}],
        guid=guid_start
        )

    try:
        results = client.upload_entities(batch=[new_lineage])
        print(f"Lineage created for source_guid: {source_guid} and destination_guid: {destination_guid}\n")
        spark.sql(f"UPDATE 0_par.lineage_actions SET action = 1 WHERE guid_origem = '{source_guid}' AND guid_destino = '{destination_guid}'")
        guid_start -= 1
        row_start += 1
    except AtlasException as e:
        print(f"Failed to create lineage for source_guid: {source_guid} and destination_guid: {destination_guid}. Error message: {e}\n")
    else:
        print(f"Lineage already exists for source_guid: {source_guid} and destination_guid: {destination_guid}\n") 

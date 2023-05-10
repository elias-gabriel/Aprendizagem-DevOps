spark.sql("""

USE CATALOG hive_metastore;
CREATE SCHEMA if not exists hive_metastore.im_development

""")

tables = spark.catalog.listTables('main.im_development')
total_tables = len(tables)  

for i, table in enumerate(tables):
    table_name = table.name

    try:
        tb_origem = spark.table(f'main.im_development.{table_name}')
        tb_origem.write.mode("overwrite").format('delta').saveAsTable(f'hive_metastore.im_development.{table_name}')
        
        percentage = ((i+1) / total_tables) * 100
        if (i+1) % (total_tables // 10) == 0: 
            print(f'Tabela {table_name} migrada com sucesso. {percentage:.2f}% migrado.')
        else:
            print(f'Tabela {table_name} migrada com sucesso.')
    except Exception as e:
        print(f'Erro ao migrar a tabela {table_name}: {str(e)}')

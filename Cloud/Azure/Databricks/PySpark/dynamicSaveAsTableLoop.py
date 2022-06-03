arquivos = dbutils.fs.ls('/mnt/')

for arquivo in arquivos:

    file = arquivo.path
    table_name = arquivo.name.split('.')[0]    
    deltaFile = f'/mnt/{table_name}'
    flag = spark.sql(f"SHOW TABLES FROM #DATABASE_NAME# LIKE '{table_name}'")
    
    if flag.rdd.isEmpty():
        df = spark.read.format('parquet').load(file)
        df.write.option("overwriteSchema", "true").mode("overwrite").format('delta').saveAsTable(f'refined.{table_name}', path = deltaFile)

########################################################################################################################################

lista_bricks = [a.name for a in spark.catalog.listTables('DATABASE_NAME')]
print(lista_bricks)

arquivos = dbutils.fs.ls('/mnt/refined/')
display(arquivos)

arquivos = dbutils.fs.ls('/mnt/refined/')
lista_lake = []

for arquivo in arquivos:
    table_name_adls = arquivo.name.split('.')[0]
    lista_lake.append(table_name_adls)
print(lista_lake)

list_difference = []
for element in lista_lake:
    if element not in lista_bricks:
        list_difference.append(element)

print(list_difference)

for table in list_difference:
    print(table)

for table in list_difference:
    df = spark.read.format('parquet').load(table)
    df.write.option("overwriteSchema", "true").mode("overwrite").format('delta').saveAsTable(f'DATABASE_NAME.{table}')

# Drop tables
for table in lista_bricks:
    spark.sql(f'drop table if exists {table}')
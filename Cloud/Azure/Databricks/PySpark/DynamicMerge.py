arquivos = dbutils.fs.ls('/mnt/transient/legado/')

def merge_lake(df, key_column):
    print(key_column)
    df.createOrReplaceTempView("source")
    if len(key_column) < 2:
        query_merge = f"""
        MERGE INTO refined.{table_name} t
        USING source s
        on s.{key_column[0]} = t.{key_column[0]}
        WHEN MATCHED THEN UPDATE SET *
        WHEN NOT MATCHED THEN INSERT *
        """
    elif len(key_column) == 2:
        query_merge = f"""
        MERGE INTO refined.{table_name} t
        USING source s
        on s.{key_column[0]} = t.{key_column[0]} AND s.{key_column[1]} = t.{key_column[1]}
        WHEN MATCHED THEN UPDATE SET *
        WHEN NOT MATCHED THEN INSERT *
        """
    print(query_merge)
    spark.sql(query_merge)


for arquivo in arquivos:

    file = arquivo.path
    table_name = arquivo.name.split('.')[0]    
    deltaFile = f'/mnt/refined/{table_name}'
    try:
        tb = spark.sql(f"select * from refined.controle_tabelas where table_name LIKE '{table_name}'")
        tb.display()
        if tb.filter(tb.flag_controller == 1).collect():
            print('controller 1')
            key = tb.collect()
            keys = key[0]['key_table'].split(',')
            df = (spark.read.format('parquet').load(file))
            merge_lake(df, keys)
            break
        else:
            print('controller 0')
        break
    except:
        pass
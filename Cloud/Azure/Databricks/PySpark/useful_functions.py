### File Save ###

def file_save(file_name, path, file_format):
    data_location = path + file_name
    files = dbutils.fs.ls(data_location)
    file = [x.path for x in files if x.path.endswith(f".{file_format}")][0]
    dbutils.fs.mv(file, data_location.rstrip('/') + f".{file_format}")
    dbutils.fs.rm(data_location, recurse = True)
    return print('OK')

file_save('cars_planes', '/mnt/stgaccpjt/raw/', 'csv')

### ###

### FK Column Creation ###
def fk_df(df_name):
    df_name = df_name.withColumn("FK_Column", lit("1"))
    return df_name

df1 = spark.read.csv('/mnt/stgaccpjt/raw/cars.csv', header = True)
df2 = spark.read.csv('/mnt/stgaccpjt/raw/planes.csv', header = True)

df1_fk = fk_df(df1)
df2_fk = fk_df(df2)

### ###

### Join ###

def join_df(df1, df2, join_type, column_name):
    df3 = df1.join(df2, column_name, join_type)
    return df3

dfs = join_df(df1_fk, df2_fk, 'full', 'FK_Column')

### ###
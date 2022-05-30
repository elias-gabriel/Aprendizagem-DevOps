######################### COMANDOS GERAIS PYSPARK #########################

# ex = dataframe

# Importar pacotes
from pyspark.sql.functions import regexp_replace, substring, lit, when 


# Renomear colunas
   transformedColumn = ex.withColumnRenamed("nome_antigo", "nome_novo")
   display(transformedColumn)

# Remover colunas
   ex.drop("nome_coluna").display()

# Salvar dataframe como tabela no banco SQL
   transformedColumn.write.saveAsTable("all_teams")

# Ler o Schema de um dataframe
   ex.printSchema()

# Ler o conteúdo de um dataframe
   ex.display()

# Ler as linha de uma coluna
   ex.select("nome_coluna").display()

# Criar uma coluna a partir de outra coluna de um dataframe
   ex.withColumn("coluna_copiada", col("coluna_existente")).display()

# Remover colunas duplicadas
   ex.dropDuplicates().display()

#Remover linhas duplicadas
   ex.dropDuplicates(["nome_coluna"]).display()

# Remover linhas com valores nulos
   ex.na.drop().display()

# Remover caracteres especiais
   ex.select(regexp_replace("nome_coluna", "[caracteres_desejados]", "").alias("nome_coluna")).display()

# Remover caracteres especiais e substituir por outro
   ex.select(regexp_replace("nome_coluna", "[caracteres_desejados]", "cartere_substituto").alias("nome_coluna")).display()

# Remover caracteres a partir de determinado índice
   ex.select(substring("nome_coluna", 0, 3).alias("nome_coluna")).display()

# Adicionar coluna no dataframe
   ex.withColumn("coluna_nova", lit("valor_coluna")).select("coluna_nova").display()

# Adicionar coluna no dataframe com valor nulo
   ex.withColumn("coluna_nova", lit(None)).select("coluna_nova").display()

# Substituir valores de uma coluna pelos de outra coluna
   ex.withColumn("coluna_nova", when(col("coluna_existente") == "valor_a_substituir", "valor_substituido").otherwise(col("coluna_existente"))).display()

# Atualizar valores de uma coluna
  # Os valores da coluna "coluna_id" serão multiplicados por 100
   ex.withColumn("coluna_id",col("coluna_id")*100).display()
   
# Listar pontos de montagem do Data Lake
   mt = dbutils.fs.mounts()
   display(mt)

# Criar pontos de montagem do Data Lake no Bricks
   def mount_adls(container_name):
    dbutils.fs.mount(
    source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storage_account_name}/{container_name}",
    extra_configs = configs)

    mount_adls('nome_container')

# Remover pontos de montagem do Data Lake no Bricks
   def unmount_adls(container_name):
    dbutils.fs.unmount(
    f"/mnt/{storage_account_name}/{container_name}")

    unmount_adls('nome_container')

# Criar um dataframe a partir de um arquivo CSV
   df = spark.read.csv("/mnt/nome_container/nome_arquivo.csv", header=True, inferSchema=True)

# Delta Lake - Salvar dataframe como tabela no Delta Lake
   df.write.format("delta").save("/mnt/nome_container/nome_arquivo.delta")

# Ler arquivo delta
   df = spark.read.format("delta").load("/mnt/nome_container/nome_arquivo.delta")
   display(df)

# Delta Lake - Atualizar tabela no Delta Lake
   df.write.format("delta").mode("overwrite").save("/mnt/nome_container/nome_arquivo.delta")

# Delta Lake - Remover tabela do Delta Lake
   df.unpersist()

# Mesclar dataframes
   df1 = spark.read.csv("/mnt/nome_container/nome_arquivo.csv", header=True, inferSchema=True)
   df2 = spark.read.csv("/mnt/nome_container/nome_arquivo.csv", header=True, inferSchema=True)
   df3 = df1.union(df2)

# Criar coluna com valor padrão
   df3.withColumn("coluna_novo", lit("valor_padrao")).select("coluna_novo").display()

# Join
   df1.join(df2, 'coluna', 'join_type')

# Union
   df1.union(df2)
   
# Upper case
   df1.select(upper("coluna_existente").alias("coluna_existente")).display()

# Merge
   df1.merge(df2, "coluna_existente", "coluna_existente")

################ WORKING WITH PANDAS ################
import pandas as pd

data = pd.read_csv("/mnt/nome_container/nome_arquivo.csv")
data = data.drop(columns=["coluna_a_remover"])
data = data.rename(columns={"coluna_a_renomear": "nome_novo"})
data = data.drop_duplicates(subset=["coluna_a_remover"])
data = data.dropna(subset=["coluna_a_remover"])
data = data.fillna(value="valor_padrao")
data = data.replace({"coluna_a_substituir": "valor_substituido"})
data = data.replace({"coluna_a_substituir": "valor_substituido"}, regex=True)
data = data.replace({"coluna_a_substituir": "valor_substituido"}, inplace=True)

################ ### ################

# Generic join between two dataframes
df1 = spark.read.parquet('/mnt/stgaccpjt/clean/parquet/all_teams.parquet')
df2 = spark.read.parquet('/mnt/stgaccpjt/clean/parquet/all_players.parquet')

df3 = df1.join(df2, 'Id', 'full')

def join_df(df1, df2, join_type, column_name):
    df3 = df1.join(df2, column_name, join_type)
    return df3

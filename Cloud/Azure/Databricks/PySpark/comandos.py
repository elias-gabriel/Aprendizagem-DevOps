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

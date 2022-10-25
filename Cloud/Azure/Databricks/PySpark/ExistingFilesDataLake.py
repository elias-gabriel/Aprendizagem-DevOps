arquivos = dbutils.fs.ls('/mnt/raw/json/')
lista = spark.read.csv('/mnt/raw/json/lista.csv', header = True)

lista_lake = []
lista_arquivos = []
fora_lake = []

for arquivo in lista.collect():
    file = arquivo.arquivos
    lista_arquivos.append(file)
print(lista_arquivos)

for arquivo in arquivos:
    file = arquivo.name
    lista_lake.append(file)  
print(lista_lake)


def compara_lista(lista_lake, lista_arquivos):
    for arquivo in lista_lake:
        if arquivo in lista_arquivos:
            print('Arquivo', arquivo, 'já existe no lake')
        else:
            print('Arquivo', arquivo, 'não existe no lake')
            fora_lake.append(arquivo)
            fora_lake.write.csv('/mnt/raw/json/fora_lake.csv', header = True)
    return fora_lake
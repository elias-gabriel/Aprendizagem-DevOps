arquivos = dbutils.fs.ls('/mnt/raw/')
files = []

for arquivo in arquivos:
    file = arquivo.name
    if file.endswith('.json'):
        files.append(file)
for file in files:
    name = file.split('.')[0]
    dbutils.fs.mv(f"/mnt/raw/{file}", f"/mnt/raw/json/{file}")
    print(name + ' moved succesfully')
    

from pyspark.sql.types import StructType

def get_schema():
    list_schema = df.dtypes
    fields = []

    for i in range(len(list_schema)):
        if(list_schema[i][1] == 'int'):
            list_schema[i] = (list_schema[i][0], 'integer')

    for i in list_schema:
        fields.append({'metadata':{}, 'name':i[0], 'nullable':True, 'type':i[1]})

    final_schema = StructType.fromJson({'fields':fields, 'type':i[1]})
    return final_schema
     
# using
df.read.option('schema', final_schema).option('inferschema', True).csv('path')

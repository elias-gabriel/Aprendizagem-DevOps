import pyodbc
import csv

server = ''
database = ''
username = ''
password = ''

connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = connection.cursor()

sql_agg = """   

SELECT v_schema.name AS ViewSchema, v.name AS ViewName, 
       t_schema.name AS TableSchema, 
       STUFF((SELECT DISTINCT ', ' + t.name 
              FROM sys.views v2 
              JOIN sys.objects o ON v2.object_id = o.object_id 
              JOIN sys.schemas s ON o.schema_id = s.schema_id 
              JOIN sys.sql_expression_dependencies ed ON ed.referencing_id = v2.object_id 
              JOIN sys.objects t ON ed.referenced_id = t.object_id 
              WHERE t.type = 'U' AND ed.referenced_class = 1 AND v2.name = v.name 
              FOR XML PATH('')), 1, 2, '') AS TablesInView
FROM sys.views v
JOIN sys.objects o ON v.object_id = o.object_id
JOIN sys.schemas v_schema ON o.schema_id = v_schema.schema_id
JOIN sys.schemas t_schema ON t_schema.schema_id IN (
    SELECT DISTINCT t.schema_id 
    FROM sys.views v2 
    JOIN sys.objects o2 ON v2.object_id = o2.object_id 
    JOIN sys.schemas s ON o2.schema_id = s.schema_id 
    JOIN sys.sql_expression_dependencies ed ON ed.referencing_id = v2.object_id 
    JOIN sys.objects t ON ed.referenced_id = t.object_id 
    WHERE t.type = 'U' AND ed.referenced_class = 1 AND v2.name = v.name
)
WHERE v.is_ms_shipped = 0
ORDER BY v_schema.name, v.name, t_schema.name;

"""

sql_2 = """ 

SELECT DISTINCT v_schema.name AS ViewSchema, v.name AS ViewName, t_schema.name AS TableSchema, t.name AS TableName
FROM sys.views AS v
INNER JOIN sys.sql_dependencies AS d ON v.object_id = d.object_id
INNER JOIN sys.objects AS t ON d.referenced_major_id = t.object_id
INNER JOIN sys.objects AS v_obj ON v.object_id = v_obj.object_id
INNER JOIN sys.schemas AS v_schema ON v_obj.schema_id = v_schema.schema_id
INNER JOIN sys.schemas AS t_schema ON t.schema_id = t_schema.schema_id
WHERE v.type = 'V'
ORDER BY v_schema.name, v.name, t_schema.name, t.name;

"""

cursor.execute(sql_agg)

with open('views_tables_agg.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Schema_Name', 'View_Name', 'Tables_in_View'])
    for row in cursor.fetchall():
        writer.writerow(row)



cursor.execute(sql_2)

with open('views_tables.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Schema_Name', 'View_Name', 'Tables_in_View'])
    for row in cursor.fetchall():
        writer.writerow(row)

connection.close()

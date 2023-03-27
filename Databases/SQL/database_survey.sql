--Agg Columns on TablesInView

SELECT v_schema.name AS ViewSchema, v.name AS ViewName, 
       t_schema.name AS TableSchema, 
       STUFF((SELECT DISTINCT ', ' + t.name 
              FROM sys.views v2 
              JOIN sys.objects o2 ON v2.object_id = o2.object_id 
              JOIN sys.schemas s2 ON o2.schema_id = s2.schema_id 
              JOIN sys.sql_expression_dependencies ed ON ed.referencing_id = v2.object_id 
              JOIN sys.objects t ON ed.referenced_id = t.object_id 
              WHERE t.type = 'U' AND ed.referenced_class = 1 AND v2.name = v.name 
              FOR XML PATH('')), 1, 2, '') AS TablesInView,
       sm.definition AS ViewDefinition,
       v_stats.last_user_update AS ViewLastModified,
       t_stats.last_user_update AS TableLastModified,
       v.create_date AS ViewCreated
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
JOIN sys.sql_modules sm ON sm.object_id = v.object_id
LEFT JOIN sys.dm_db_index_usage_stats v_stats ON v_stats.object_id = v.object_id
LEFT JOIN sys.dm_db_index_usage_stats t_stats ON t_stats.object_id = (
    SELECT TOP 1 t2.object_id 
    FROM sys.views v3 
    JOIN sys.objects o3 ON v3.object_id = o3.object_id 
    JOIN sys.schemas s3 ON o3.schema_id = s3.schema_id 
    JOIN sys.sql_expression_dependencies ed2 ON ed2.referencing_id = v3.object_id 
    JOIN sys.objects t2 ON ed2.referenced_id = t2.object_id 
    WHERE t2.type = 'U' AND ed2.referenced_class = 1 AND v3.name = v.name
)
WHERE v.is_ms_shipped = 0
ORDER BY v_schema.name, v.name, t_schema.name;


--Independet Rows

SELECT distinct v_schema.name AS ViewSchema, v.name AS ViewName, 
       t_schema.name AS TableSchema, 
       t.name AS TableName,
       sm.definition AS ViewDefinition,
       v_stats.last_user_update AS ViewLastModified,
       t_stats.last_user_update AS TableLastModified,
       v.create_date AS ViewCreated
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
JOIN sys.sql_modules sm ON sm.object_id = v.object_id
LEFT JOIN sys.dm_db_index_usage_stats v_stats ON v_stats.object_id = v.object_id
LEFT JOIN sys.dm_db_index_usage_stats t_stats ON t_stats.object_id = (
    SELECT TOP 1 t2.object_id 
    FROM sys.views v3 
    JOIN sys.objects o3 ON v3.object_id = o3.object_id 
    JOIN sys.schemas s3 ON o3.schema_id = s3.schema_id 
    JOIN sys.sql_expression_dependencies ed2 ON ed2.referencing_id = v3.object_id 
    JOIN sys.objects t2 ON ed2.referenced_id = t2.object_id 
    WHERE t2.type = 'U' AND ed2.referenced_class = 1 AND v3.name = v.name
)
JOIN sys.sql_dependencies sd ON sd.object_id = v.object_id
JOIN sys.objects t ON sd.referenced_major_id = t.object_id
WHERE v.is_ms_shipped = 0 AND t.type = 'U'
ORDER BY v_schema.name, v.name, t_schema.name, t.name;



-- FOR PROCEDURES:

SELECT distinct p_schema.name AS ProcedureSchema, p.name AS ProcedureName, 
       t_schema.name AS TableSchema, 
       t.name AS TableName,
       sm.definition AS ProcedureDefinition,
       p_stats.last_user_update AS ProcedureLastModified,
       t_stats.last_user_update AS TableLastModified,
       p.create_date AS ProcedureCreated
FROM sys.procedures p
JOIN sys.objects o ON p.object_id = o.object_id
JOIN sys.schemas p_schema ON o.schema_id = p_schema.schema_id
JOIN sys.schemas t_schema ON t_schema.schema_id IN (
    SELECT DISTINCT t.schema_id 
    FROM sys.procedures p2 
    JOIN sys.objects o2 ON p2.object_id = o2.object_id 
    JOIN sys.schemas s ON o2.schema_id = s.schema_id 
    JOIN sys.sql_expression_dependencies ed ON ed.referencing_id = p2.object_id 
    JOIN sys.objects t ON ed.referenced_id = t.object_id 
    WHERE t.type = 'U' AND ed.referenced_class = 1 AND p2.name = p.name
)
JOIN sys.sql_modules sm ON sm.object_id = p.object_id
LEFT JOIN sys.dm_db_index_usage_stats p_stats ON p_stats.object_id = p.object_id
LEFT JOIN sys.dm_db_index_usage_stats t_stats ON t_stats.object_id = (
    SELECT TOP 1 t2.object_id 
    FROM sys.procedures p3 
    JOIN sys.objects o3 ON p3.object_id = o3.object_id 
    JOIN sys.schemas s3 ON o3.schema_id = s3.schema_id 
    JOIN sys.sql_expression_dependencies ed2 ON ed2.referencing_id = p3.object_id 
    JOIN sys.objects t2 ON ed2.referenced_id = t2.object_id 
    WHERE t2.type = 'U' AND ed2.referenced_class = 1 AND p3.name = p.name
)
JOIN sys.sql_dependencies sd ON sd.object_id = p.object_id
JOIN sys.objects t ON sd.referenced_major_id = t.object_id
WHERE p.is_ms_shipped = 0 AND t.type = 'U'
ORDER BY p_schema.name, p.name, t_schema.name, t.name;

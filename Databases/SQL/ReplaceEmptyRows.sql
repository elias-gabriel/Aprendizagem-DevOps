-- This Procedure replaces empty rows of a column with null values

DROP PROCEDURE IF EXISTS set_null_on_empty_rows
GO

CREATE PROCEDURE set_null_on_empty_rows (@table_name varchar(255), @column_name varchar(255))
AS
BEGIN
    DECLARE @sql NVARCHAR(MAX);
    SET @sql = 'UPDATE ' + @table_name + ' SET ' + @column_name + ' = NULLIF(' + @column_name + ', '''')';
    EXECUTE sp_executesql @sql;
END

EXEC set_null_on_empty_rows 'schema_name.table_name','column_name'

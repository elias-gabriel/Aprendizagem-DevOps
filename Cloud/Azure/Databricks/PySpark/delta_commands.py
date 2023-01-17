#Delta Table -  Time Travel

DESCRIBE HISTORY <table_name>;

SELECT * FROM <table_name> VERSION AS OF <version>;

RESTORE TABLE <table_name> TO VERSION AS OF <version>; 

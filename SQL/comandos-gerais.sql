-- Criar Bando de Dados
-- DROP DATABASE IF EXISTS quickstartdb;
CREATE DATABASE quickstartdb;
USE quickstartdb;

-- Criar tabela e inserir dados
DROP TABLE IF EXISTS inventário;
CREATE TABLE inventário (id serial PRIMARY KEY, nome VARCHAR(50), quantidade INTEGER);
INSERT INTO inventário (nome, quantidade) VALUES ('banana', 150);
INSERT INTO inventário (nome, quantidade) VALUES ('laranja', 154);
INSERT INTO inventário (nome, quantidade) VALUES ('maçã', 100);

-- Ler
SELECT * FROM inventário;

-- Atualizar
UPDATE inventário SET quantidade = 200 WHERE id = 1;
SELECT * FROM inventário;

-- Deletar
DELETE FROM inventário WHERE id = 2;
SELECT * FROM inventário;

-- Alterar tipo da tabela -- 
alter TABLE inventário ALTER COLUMN nome varchar(60) NOT NULL

/*
-- Filtrar Sáida -- 
LIKE 'a%': Qualquer valor que começa com 'a'
LIKE '%a': Qualquer valor que termina com 'a'
LIKE '%or%': Qualquer valor que tenha as letras 'or' em qualquer posição
LIKE '_r%': Qualquer valor que tenha 'r' na segunda posição
LIKE 'a_%': Qualquer valor que começa com 'a' e tenha pelo menos 2 caracteres 
LIKE 'a__%': Qualquer valor que começa com 'a' e tenha pelo menos 3 caracteres 
LIKE 'a%o': Qualquer valor que começe com 'a' e termine com 'o' 
*/
SELECT * FROM inventário where nome LIKE '__ç%'
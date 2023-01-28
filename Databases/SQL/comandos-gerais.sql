-- Criar Bando de Dados
-- DROP DATABASE IF EXISTS quickstartdb;
CREATE DATABASE quickstartdb;
USE quickstartdb;

-- Criar tabela e inserir dados
DROP TABLE IF EXISTS inventário;
CREATE TABLE inventário (id serial PRIMARY KEY, nome_fruta VARCHAR(50), quantidade INTEGER);
INSERT INTO inventário (nome_fruta, quantidade) VALUES ('banana', 150);
INSERT INTO inventário (nome_fruta, quantidade) VALUES ('laranja', 154);
INSERT INTO inventário (nome_fruta, quantidade) VALUES ('maçã', 100);

-- Ler
SELECT * FROM inventário;

-- Atualizar
UPDATE inventário SET quantidade = 200 WHERE id = 1;
SELECT * FROM inventário;

-- Deletar
DELETE FROM inventário WHERE id = 2;
SELECT * FROM inventário;

-- Alterar tipo da tabela -- 
alter TABLE inventário ALTER COLUMN nome_fruta varchar(60) NOT NULL
ALTER TABLE nome_tabela CHANGE COLUMN nome_antigo_coluna novo_nome_coluna CHAR(35) NOT NULL DEFAULT '' ;

-- Alterar nome da tabela 
EXEC sp_rename 'nome_tabela', 'novo_nome';

-- Alterar nome da coluna
EXEC sp_rename 'nome_tabela.nome_coluna', 'novo_nome', 'COLUMN';

-- Listar Informações de tabelas do banco
SELECT *
FROM information_Schema.Columns C
FULL OUTER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE U ON C.COLUMN_NAME = U.COLUMN_NAME
WHERE C.TABLE_NAME = 'TABLE_NAME'

/*
-- Operação Like -- 
LIKE 'a%': Qualquer valor que começa com 'a'
LIKE '%a': Qualquer valor que termina com 'a'
LIKE '%or%': Qualquer valor que tenha as letras 'or' em qualquer posição
LIKE '_r%': Qualquer valor que tenha 'r' na segunda posição
LIKE 'a_%': Qualquer valor que começa com 'a' e tenha pelo menos 2 caracteres 
LIKE 'a__%': Qualquer valor que começa com 'a' e tenha pelo menos 3 caracteres 
LIKE 'a%o': Qualquer valor que começe com 'a' e termine com 'o' 
SELECT * FROM inventário where nome LIKE '__ç%' */

-- Index --
/* 
Permte que as aplicações de Banco de Dados encontrem os dados mais rapidamente, sem ter de ler a tabela toda.
OBS: Apenas crrie Índices em tabelas que recebem muitas consultas
     Tabelas Idexadas levam mais tempo para serem atualizadas

CREATE INDEX nome_índice ON nome_tabela (nome_coluna)
EX: CREATE INDEX consulta ON inventário (nome_fruta)
DELEÇÃO: ALTER TABLE inventário DROP INDEX 'consulta'
*/

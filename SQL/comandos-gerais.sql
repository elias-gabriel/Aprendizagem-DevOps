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
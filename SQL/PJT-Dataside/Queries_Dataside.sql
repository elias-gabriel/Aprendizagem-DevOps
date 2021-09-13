-- Ultimo Pedido Cliente
SELECT Nome, SobreNome, Data_Compra_Pedido, CPF_C from pedidos inner join clientes on pedidos.CPF_C 
= clientes.CPF  ORDER BY Data_Compra_Pedido DESC

-- RANKING Produto mais vendido
SELECT top 5 ProdutoID, produtos.Nome_Produto, COUNT(*) AS VENDAS from itens_pedidos inner join produtos on 
itens_pedidos.ProdutoID = produtos.Produto_ID GROUP by ProdutoID, produtos.Nome_Produto order by VENDAS DESC 

-- Quem fez o Pedido mais caro
SELECT top 5 Nome, SobreNome, pedidos.Valor, Data_Compra_Pedido from clientes inner join pedidos on clientes.CPF 
= pedidos.CPF_C ORDER BY Valor DESC 


/* Teste Tabela Histórica

UPDATE pedidos set Status_Compra = 'Entrege' where Numero_Pedido = 29
INSERT into pedidos VALUES ('59', '19.90 ', 'Pendente', '2021/05/22', '984.678.461-84')
UPDATE pedidos set Status_Compra = 'Em Transporte' where Numero_Pedido = 59


select * from clientes
select * from pedidos
SELECT * from produtos 
select * from hist_pedido */
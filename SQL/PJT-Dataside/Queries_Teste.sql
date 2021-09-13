select * from clientes 
SELECT * from itens_pedidos
SELECT * from pedidos
select * from produtos

select * from clientes where CPF ='984.678.461-84'

select Numero_Pedido from pedidos where CPF_C ='984.678.461-84'

select * from itens_pedidos where IDPedido = 21

select Nome_Produto from itens_pedidos inner JOIN produtos on itens_pedidos.ProdutoID = produtos.Produto_ID INNER join pedidos on itens_pedidos.IDPedido = pedidos.CPF_C


select p.Nome_Produto, ip.Quantidade, pe.Numero_Pedido  from produtos p inner join itens_pedidos ip on p.Produto_ID 
= ip.ProdutoID inner join pedidos pe on pe.Numero_Pedido = ip.IDPedido  where pe.CPF_C = '984.678.461-84'


SELECT top 5 Nome, SobreNome, Data_Compra_Pedido, CPF_C from pedidos inner join clientes on pedidos.CPF_C 
= clientes.CPF  where CPF_C= '324.931.280-01' ORDER BY Data_Compra_Pedido DESC



SELECT CPF_C, Nome, SobreNome, Data_Compra_Pedido from pedidos inner join clientes on pedidos.CPF_C 
= clientes.CPF ORDER by  1

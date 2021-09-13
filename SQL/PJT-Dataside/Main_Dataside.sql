drop table if exists clientes, pedidos, produtos, hist_pedido, itens_pedidos
GO

-- Tabela Clientes
create table clientes (
	ID_Cliente int unique Not Null,
	Nome varchar(30) NOT NULL,
	SobreNome varchar(30),
	Email varchar(30) NOT NULL, 
	CPF varchar(14) PRIMARY KEY NOT NULL,
	Data_Nascimento date NOT NULL, 
	Endereço varchar(70) NOT NULL
	)
--

-- Dados Clientes
INSERT into clientes VALUES('1','Gustavo', 'Borges','gustavo@gmail.com', '767.696.474-00', '2001/05/22', 'Rua Paracatu - São Paulo - SP'),
                            ('2', 'Felipe', 'Borges','Felipe@gmail.com', '984.678.461-84', '1987/08/18', 'Avenida Governador José Malcher - Belém - PR'),
                            ('3', 'Jéssica','Silva', 'jessica@gmail.com', '785.674.957-36', '2001/09/21', 'QE 11 Área Especial C - Guará I  - Brasília'),
                            ('4', 'Marcos', 'Lima', 'marcos@gmail.com', '324.931.280-01', '1987/07/11', 'Avenida Rio Branco - Rio de Janeiro - RJ'),
							('5', 'Ana', 'Clara', 'ana@gmail.com', '756.069.700-31', '1991/09/12', 'Avenida Afonso Pena - Belo Horizonte - MG'),
							('6', 'Leonardo', 'Martins', 'leonardo@gmail.com', '998.557.375-84', '1989/11/09', 'Travessa Antônio Ferreira - Capanema - PA'),
							('7', 'Thiago', 'Junior', 'thiago@gmail.com', '390.611.770-73', '1996/10/22', 'Rua Arlindo Nogueira - Teresina - PI'),
							('8', 'Vinicius', 'Lourenço', 'vinicius@gmail.com', '716.264.170-91', '1995/07/27', 'Rua Arlindo Nogueira -  São Paulo - SP'),
							('9', 'Beatriz', 'Silva', 'beatriz@gmail.com', '126.970.590-32', '2002/09/20', 'Rua Pereira Estéfano - São Paulo - SP'),
							('10', 'Juliana', 'Clara', 'juliana@gmail.com', '488.162.220-00', '2000/12/21', 'Avenida Desembargador Moreira - Fortaleza - CE')
--

-- Tabela Produtos
create table produtos(
	Produto_ID int PRIMARY KEY NOT NULL,
	Nome_Produto varchar(70) NOT NULL,
	Tipo_Produto char(8) NOT NULL,
	Valor money NOT NULL,
	Datas DATE NOT NULL
)

--Dados Produtos
INSERT INTO produtos VALUES('1','Camiseta Vermelha', 'Camiseta', '24.99', '2021/03/22'),
						   ('2','Chaveiro Aquaman', 'Chaveiro', '14.99', '2021/05/25'),
						   ('3','Camiseta Batman', 'Camiseta', '49.99', '2021/03/20'),
						   ('4','Caneca Azul 500ML', 'Caneca', '14.99', '2021/02/25'),
						   ('5','Caneca SuperMan 500ML', 'Caneca', '19.99', '2021/09/01'),					
						   ('6','Camiseta Homem Aranha', 'Camiseta', '49.99', '2021/08/24'),
						   ('7','Chaveiro Importado ', 'Chaveiro', '29.99', '2021/07/26'),
						   ('8','Kit 3 Camisetas Marvel ', 'Chaveiro', '89.99', '2021/04/22'),
						   ('9','Camiseta Polo', 'Camiseta', '39.99', '2021/05/30'),
						   ('10','Camiseta Marvel', 'Camiseta', '44.90', '2021/08/15')
--

--Tabela Itens Pedidos
create table itens_pedidos (
    IDPedido int,
	Quantidade int not null,
    ProdutoID int not null, FOREIGN KEY (ProdutoID) REFERENCES produtos(Produto_ID)
)

--Dados de Itens Pediso
INSERT INTO itens_pedidos VALUES('20', '2', '5'),
								('21','1', '1'),
								('21', '1', '10'),
								('22', '2', '10'),
								('23', '1', '3'),
								('23', '2', '2'),							
								('24', '2', '4'),
								('25', '3', '1'),
								('26', '1', '7'),
								('26', '5', '10'),
								('27', '4', '2'),
								('28', '1', '6'),
								('29', '1','8'),
								('29', '2', '4'),
								('29', '1', '7')
-- 

-- Tabela Pedidos
create table pedidos (
	Numero_Pedido int PRIMARY KEY NOT NULL,
	Valor money NOT NULL,
	Status_Compra varchar(20) NOT NULL,
	Data_Compra_Pedido date NOT NULL,
	CPF_C VARCHAR(14) not NULL, FOREIGN KEY (CPF_C) REFERENCES clientes(CPF),
)

--Dados dos Pedidos
INSERT INTO pedidos VALUES('20', '39.80', 'Aprovado','2021/04/28', '767.696.474-00'),						  
                          ('21', '69.80', 'Em Transporte', '2021/04/11', '984.678.461-84'),
						  ('22', '89.80', 'Aprovado', '2021/11/21', '324.931.280-01'),
						  ('23', '59.89', 'Entrege', '2021/01/11', '785.674.957-36'),
						  ('24', '29.98', 'Aprovado', '2021/09/07', '324.931.280-01'),
						  ('25', '74.97', 'Entrege', '2021/02/21', '756.069.700-31'),
						  ('26', '219.59', 'Aprovado', '2021/02/07', '998.557.375-84'),
						  ('27', '59.96', 'Cancelado', '2021/09/01', '390.611.770-73'),
						  ('28', '49.99', 'Pendente', '2021/03/30', '126.970.590-32'),
						  ('29', '149.96', 'Em Transporte', '2021/08/21', '488.162.220-00')


-- select Numero_Pedido, Status_Compra, Itens_Pedidos, Data_Compra_Pedido, FORMAT (Valor, 'C', 'pt-BR') as Valor FROM pedidos

--Tabela Histórica
create table hist_pedido (
	Numero_Pedido INT,
	Status_Compra VARCHAR(20),
	Ação varchar(12),
	Data_Modi DATETIME
)
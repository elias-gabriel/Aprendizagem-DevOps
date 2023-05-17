-- Serie A

INSERT INTO nba.jogadores VALUES 
	('Fernando', 'Rodrigues', 'Nando', NULL, 'A'),
	('Bruno', 'de Lucas', 'Dex', '2006-08-03', 'A'),
	('Elias', 'Gabriel', 'Big Fellas', '2005-05-24', 'A'),
	('Misael', 'Shelby', 'Shelby', null, 'A'),
	('João', 'Pedro', 'Jota', null, 'A'),
	('Matheus', 'Coelho', 'Mate', null, 'A')

-- Serie B
	
INSERT INTO nba.jogadores VALUES 
	('Haniel', 'Souza', 'Hani', NULL, 'B'),
	('Filipe', 'Mendes', 'Lipe', '2009-03-03', 'B'),
	('Gabriel', null, 'Mouse', null, 'B'),
	('Guilherme', 'Rocha', 'Gui', null, 'B'),
	('Guilherme', null, null, null, 'B'),
	('Lucas', null, null, null, 'B')
	



-- Inserir um jogador: nome, sobrenomme, apelido, datanascimento, serie
EXEC nba.InserirJogador 'Nome', 'Sobrenome', 'Apelido', '1990-01-01', 'A';

-- Inserir um local: nome, cidade
EXEC nba.InserirLocal 'Academia Leao de Juda', 'Aguas Lindas';

-- Inserir uma partida: data, localID, Jogador1, Vitorias1, Derrotas1, Jogador2, Vitorias2, Derrotas2
EXEC nba.InserirPartida '2023-05-15', 1, 9, 3, 2, 10, 2, 3;
EXEC nba.InserirPartida '2023-05-15', 1, 7, 3, 2, 11, 2, 3;
EXEC nba.InserirPartida '2023-05-16', 1, 8, 3, 2, 12, 2, 3;

select * from nba.partidas
-- Inserir estatísticas do jogo: partidaID, JogadorID, Cestasde2, Cestasde3, CestasLivres, Faltas
EXEC nba.InserirEstatisticasJogo 1, 9, 16, 12, 2, 12;
EXEC nba.InserirEstatisticasJogo 1, 10, 5, 19, 0, 17;

EXEC nba.InserirEstatisticasJogo 2, 7, 5, 20, 0, 11;
EXEC nba.InserirEstatisticasJogo 2, 11, 18, 14, 1, 4;

EXEC nba.InserirEstatisticasJogo 3, 8, 23, 33, 0, 7;
EXEC nba.InserirEstatisticasJogo 3, 12, 14, 34, 0, 2;

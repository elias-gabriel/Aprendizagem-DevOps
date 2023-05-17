-- campeonato_geral
CREATE VIEW nba.vw_campeonato_geral
as
SELECT 
    jogadores.Nome,
    jogadores.SobreNome,
    jogadores.Apelido,
    DATEDIFF(YEAR, DataNascimento, GETDATE()) - CASE 
		WHEN (MONTH(DataNascimento) > MONTH(GETDATE()))
			OR (
				MONTH(DataNascimento) = MONTH(GETDATE())
				AND DAY(DataNascimento) > DAY(GETDATE())
				)
			THEN 1
		ELSE 0
		END AS Idade,
    FORMAT(DataNascimento, 'dd/MM/yyyy') AS DataNascimento,
    jogadores.Serie,
    locais.Nome AS NomeLocal,
    locais.Cidade AS CidadeLocal,
    partidas.Data AS DataPartida,
    estatisticasJogo.CestasDe2,
    estatisticasJogo.CestasDe3,
    estatisticasJogo.CestasLivres,
    estatisticasJogo.CestasTotais,
    estatisticasJogo.Faltas,
    jogador_partida.Vitorias,
    jogador_partida.Derrotas,
    jogador_partida.JogosTotais,
    jogador_partida.ResultadoFinal
FROM 
    nba.jogadores 
JOIN 
    nba.partidas ON jogadores.JogadorID = partidas.JogadorID1 OR jogadores.JogadorID = partidas.JogadorID2
JOIN 
    nba.locais ON partidas.LocalID = locais.LocalID
JOIN 
    nba.estatisticasJogo ON jogadores.JogadorID = estatisticasJogo.JogadorID AND partidas.PartidaID = estatisticasJogo.PartidaID
JOIN 
    nba.jogador_partida ON jogadores.JogadorID = jogador_partida.JogadorID AND partidas.PartidaID = jogador_partida.PartidaID

-- Inserir Jogador
CREATE PROCEDURE nba.InserirJogador
    @Nome NVARCHAR(50),
    @SobreNome NVARCHAR(50),
    @Apelido NVARCHAR(30),
    @DataNascimento DATE,
    @Serie CHAR(1)
AS
BEGIN
    INSERT INTO nba.jogadores (Nome, SobreNome, Apelido, DataNascimento, Serie)
    VALUES (@Nome, @SobreNome, @Apelido, @DataNascimento, @Serie)
END;
GO



-- Inserir Local
CREATE PROCEDURE nba.InserirLocal
    @Nome NVARCHAR(100),
    @Cidade NVARCHAR(50)
AS
BEGIN
    INSERT INTO nba.locais (Nome, Cidade)
    VALUES (@Nome, @Cidade)
END;
GO


-- Inserir Partida
CREATE PROCEDURE nba.InserirPartida
    @Data DATETIME,
    @LocalID INT,
    @JogadorID1 INT,
    @VitoriasJogador1 INT,
    @DerrotasJogador1 INT,
    @JogadorID2 INT,
    @VitoriasJogador2 INT,
    @DerrotasJogador2 INT
AS
BEGIN
    INSERT INTO nba.partidas (Data, LocalID, JogadorID1, JogadorID2)
    VALUES (@Data, @LocalID, @JogadorID1, @JogadorID2)

    DECLARE @PartidaID INT
    SET @PartidaID = SCOPE_IDENTITY()

    INSERT INTO nba.partida_local (PartidaID, LocalID)
    VALUES (@PartidaID, @LocalID)

    INSERT INTO nba.jogador_partida (PartidaID, JogadorID, Vitorias, Derrotas)
    VALUES (@PartidaID, @JogadorID1, @VitoriasJogador1, @DerrotasJogador1), 
           (@PartidaID, @JogadorID2, @VitoriasJogador2, @DerrotasJogador2)
END;
GO


-- Inserir Estatisticas do Jogo
CREATE PROCEDURE nba.InserirEstatisticasJogo
    @PartidaID INT,
    @JogadorID INT,
    @CestasDe2 INT,
    @CestasDe3 INT,
    @CestasLivres INT,
    @Faltas INT
AS
BEGIN
    INSERT INTO nba.estatisticasJogo (PartidaID, JogadorID, CestasDe2, CestasDe3, CestasLivres, Faltas)
    VALUES (@PartidaID, @JogadorID, @CestasDe2, @CestasDe3, @CestasLivres, @Faltas)
END;
GO

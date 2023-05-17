DROP TABLE IF EXISTS nba.estatisticasJogo;
DROP TABLE IF EXISTS nba.jogador_partida;
DROP TABLE IF EXISTS nba.partida_local;
DROP TABLE IF EXISTS nba.partidas;
DROP TABLE IF EXISTS nba.locais;
DROP TABLE IF EXISTS nba.jogadores;


CREATE TABLE nba.jogadores (
    JogadorID INT IDENTITY PRIMARY KEY,
    Nome NVARCHAR(50),
    SobreNome NVARCHAR(50),
    Apelido NVARCHAR(30),
    DataNascimento DATE,
    Serie CHAR(1) CHECK(Serie IN ('A', 'B'))
);

CREATE TABLE nba.locais (
    LocalID INT IDENTITY PRIMARY KEY,
    Nome NVARCHAR(100),
    Cidade NVARCHAR(50)
);



CREATE TABLE nba.partidas (
    PartidaID INT IDENTITY PRIMARY KEY,
    Data DATETIME,
    LocalID INT FOREIGN KEY (LocalID) REFERENCES nba.locais(LocalID),
    JogadorID1 INT FOREIGN KEY REFERENCES nba.jogadores(JogadorID),
    JogadorID2 INT FOREIGN KEY REFERENCES nba.jogadores(JogadorID)
);


CREATE TABLE nba.estatisticasJogo (
    PartidaID INT FOREIGN KEY (PartidaID) REFERENCES nba.partidas(PartidaID),
    JogadorID INT FOREIGN KEY (JogadorID) REFERENCES nba.jogadores(JogadorID),
    CestasDe2 INT,
    CestasDe3 INT,
    CestasLivres INT,
    CestasTotais AS (CestasDe2 * 2 + CestasDe3 * 3 + CestasLivres),
    Faltas INT
);


CREATE TABLE nba.jogador_partida (
    PartidaID INT NOT NULL, 
    JogadorID INT NOT NULL, 
    Vitorias INT,
    Derrotas INT,
    JogosTotais AS (Vitorias + Derrotas),
    ResultadoFinal AS (CASE WHEN Vitorias >= 3 THEN 'Vitoria' ELSE 'Derrota' END),
    FOREIGN KEY (PartidaID) REFERENCES nba.partidas(PartidaID), 
    FOREIGN KEY (JogadorID) REFERENCES nba.jogadores(JogadorID)
);


CREATE TABLE nba.partida_local (
    PartidaID INT NOT NULL, 
    LocalID INT NOT NULL, 
    FOREIGN KEY (PartidaID) REFERENCES nba.partidas(PartidaID), 
    FOREIGN KEY (LocalID) REFERENCES nba.locais(LocalID)
);



	

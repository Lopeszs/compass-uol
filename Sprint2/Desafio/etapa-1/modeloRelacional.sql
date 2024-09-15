-- CRIAÇÃO DAS TABELAS NORMALIZADAS --

-- TABELA COMBUSTÍVEL
CREATE TABLE tbCombustivel (
	idCombustivel INT PRIMARY KEY,
	tipoCombustivel VARCHAR(20)
);


-- TABELA CARRO
CREATE TABLE tbCarro(
	idCarro INT PRIMARY KEY,
	kmCarro INT,
	chassiCarro VARCHAR(50),
	marcaCarro VARCHAR(80),
	modeloCarro VARCHAR(80),
	anoCarro INT,
	idCombustivel INT,
	FOREIGN KEY (idCombustivel) REFERENCES tbCombustivel (idCombustivel)
);


-- TABELA VENDEDOR
CREATE TABLE tbVendedor (
	idVendedor INT PRIMARY KEY,
	nomeVendedor VARCHAR(100),
	sexoVendedor SMALLINT,
	estadoVendedor VARCHAR(40)
);


-- TABELA CLIENTE
CREATE TABLE tbCliente (
	idCliente INT PRIMARY KEY,
	nomeCliente VARCHAR(100),
	cidadeCliente VARCHAR(40),
	estadoCliente VARCHAR(40),
	paisCliente VARCHAR(40)
);


-- TABELA LOCAÇÃO
CREATE TABLE tbLocacao (
	idLocacao INT PRIMARY KEY,
	dataLocacao DATETIME,
	horaLocacao TIME,
	qtdDiaria INT,
	vlrDiaria DECIMAL(10, 2),
	dataEntrega DATE,
	horaEntrega TIME,
	idCliente INT,
	idCarro INT,
	idVendedor INT,
	FOREIGN KEY (idCliente) REFERENCES tbCliente (idCliente),
	FOREIGN KEY (idCarro) REFERENCES tbCarro (idCarro),
	FOREIGN KEY (idVendedor) REFERENCES tbVendedor (idVendedor)
);


-- TRATANDO DADOS --

-- TRATANDO OS DADOS DOS CARROS
CREATE TEMPORARY TABLE tempCarro AS
SELECT 
    idCarro,
    kmCarro,
    classiCarro,
    marcaCarro,
    modeloCarro,
    anoCarro,
    idCombustivel
FROM tb_locacao
WHERE (idCarro, kmCarro) IN (
    SELECT idCarro, MAX(kmCarro)
    FROM tb_locacao
    GROUP BY idCarro
);

-- TRATANDO AS VARIÁVEIS DE LOCAÇÃO DO TIPO DATA
CREATE TEMPORARY TABLE tempLocacao AS
SELECT 
    idLocacao,
    -- Converte a dataLocacao para o formato 'YYYY-MM-DD'
    STRFTIME('%Y-%m-%d', SUBSTR(dataLocacao, 1, 4) || '-' || SUBSTR(dataLocacao, 5, 2) || '-' || SUBSTR(dataLocacao, 7, 2)) AS dataLocacao,
    horaLocacao,
    qtdDiaria,
    vlrDiaria,
    -- Converte a dataEntrega para o formato 'YYYY-MM-DD'
    STRFTIME('%Y-%m-%d', SUBSTR(dataEntrega, 1, 4) || '-' || SUBSTR(dataEntrega, 5, 2) || '-' || SUBSTR(dataEntrega, 7, 2)) AS dataEntrega,
    horaEntrega,
    idCliente,
    idCarro,
    idVendedor
FROM tb_locacao;


-- INSERÇÃO DOS DADOS --

-- DADOS DA TABELA COMBUSTÍVEL
INSERT INTO tbCombustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao;


-- DADOS DA TABELA CARRO
INSERT INTO tbCarro (idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT DISTINCT idCarro, kmCarro, classiCarro AS chassiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM tempCarro;


-- DADOS DA TABELA VENDEDOR
INSERT INTO tbVendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;


-- DADOS DA TABELA CLIENTE
INSERT INTO tbCliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;


-- DADOS DA TABELA LOCAÇÃO
INSERT INTO tbLocacao (idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCliente, idCarro, idVendedor, idCliente, idCarro, idVendedor)
SELECT DISTINCT idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCliente, idCarro, idVendedor, idCliente, idCarro, idVendedor
FROM tempLocacao;



-- CONSULTAS --
--------------------------------

SELECT * FROM tbCombustivel;

SELECT * FROM tbCarro;

SELECT * FROM tbVendedor;

SELECT * FROM tbCliente;

SELECT * FROM tbLocacao;

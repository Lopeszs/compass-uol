-- CRIAÇÃO DAS VIEWS --

-- DIMENSÃO CARRO
CREATE VIEW dim_Carro AS
SELECT 
	idCarro,
	kmCarro,
	chassiCarro,
	marcaCarro,
	modeloCarro,
	anoCarro,
	tipoCombustivel
FROM tbCarro AS car
JOIN tbCombustivel AS comb
ON car.idcombustivel = comb.idcombustivel;


-- DIMENSÃO CLIENTE
CREATE VIEW dim_Cliente AS
SELECT 
	idCliente,
	nomeCliente,
	cidadeCliente,
	estadoCliente,
	paisCliente
FROM tbCliente;


-- DIMENSÃO VENDEDOR
CREATE VIEW dim_Vendedor AS
SELECT
	idVendedor,
	nomeVendedor,
	sexoVendedor,
	estadoVendedor
FROM tbVendedor;


-- DIMENSÃO DATA
CREATE VIEW dim_Data AS
SELECT DISTINCT
    DATE(loc.dataLocacao) AS dataLocacao,  
    STRFTIME('%d', loc.dataLocacao) AS diaLocacao,
    STRFTIME('%W', loc.dataLocacao) AS semanaLocacao, 
    STRFTIME('%m', loc.dataLocacao) AS mesLocacao, 
    STRFTIME('%Y', loc.dataLocacao) AS anoLocacao,
    DATE(loc.dataEntrega) AS dataEntrega,  
    STRFTIME('%d', loc.dataEntrega) AS diaEntrega,
    STRFTIME('%W', loc.dataEntrega) AS semanaEntrega, 
    STRFTIME('%m', loc.dataEntrega) AS mesEntrega, 
    STRFTIME('%Y', loc.dataEntrega) AS anoEntrega 
FROM tbLocacao AS loc;


-- FATO LOCACAO
CREATE VIEW fato_Locacao AS
SELECT 
	idLocacao,
	dataLocacao,
	horaLocacao,
	qtdDiaria,
	vlrDiaria,
	dataEntrega,
	horaEntrega,
	idCliente,
	idCarro,
	idVendedor
FROM tbLocacao;
	

-- CONSULTAS --
--------------------------------

SELECT * FROM dim_Carro

SELECT * FROM dim_Cliente

SELECT * FROM dim_Vendedor

SELECT * FROM dim_Data

SELECT * FROM fato_Locacao
-- 10) A comissão de um vendedor é definida a partir de um percentual sobre o
-- total de vendas (quantidade * valor unitário) por ele realizado. O percentual
-- de comissão de cada vendedor está armazenado na coluna perccomissao,
-- tabela tbvendedor.
-- Com base em tais informações, calcule a comissao de todos os
-- vendedores, considerando todas as vendas armazenadas na base de
-- dados com status concluido.
-- As colunas presentes no resultado devem ser vendedor, valor_total_vendas
-- e comissao. O valor de comissão deve ser apresentado em ordem
-- decrescente arredondado na segunda casa decimal.

WITH total_vendas AS (
	SELECT vendedor.cdvdd,
	SUM(venda.qtd * venda.vrunt) AS t_vendas
	FROM tbvendedor AS vendedor
	LEFT JOIN tbvendas AS venda
	ON vendedor.cdvdd = venda.cdvdd
	WHERE venda.status = 'Concluído'
	GROUP BY vendedor.cdvdd
)
SELECT 
	vendedor.nmvdd AS vendedor,
	total_vendas.t_vendas AS valor_total_vendas,
	ROUND(((vendedor.perccomissao*(total_vendas.t_vendas)) / 100), 2) AS comissao
FROM tbvendedor AS vendedor
LEFT JOIN total_vendas
ON vendedor.cdvdd = total_vendas.cdvdd
ORDER BY comissao DESC
-- 12) Apresente a query para listar codigo, nome e data de nascimento dos
-- dependentes do vendedor com menor valor total bruto em vendas (não
-- sendo zero). As colunas presentes no resultado devem ser cddep, nmdep,
-- dtnasc e valor_total_vendas.
-- Observação: Apenas vendas com status concluido.


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
	dep.cddep,
	dep.nmdep,
	dep.dtnasc,
	total_vendas.t_vendas AS valor_total_vendas
FROM tbdependente AS dep
LEFT JOIN total_vendas
ON dep.cdvdd = total_vendas.cdvdd
ORDER BY total_vendas.t_vendas
LIMIT 1

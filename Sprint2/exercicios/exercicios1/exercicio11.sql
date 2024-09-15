-- 11) Apresente a query para listar o codigo e nome cliente com maior gasto na
-- loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta
-- ultima representando o somatorio das vendas (concluidas) atribuidas ao
-- cliente.

SELECT 
	cdcli, 
	nmcli,
	SUM(qtd * vrunt) AS gasto
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY cdcli, nmcli
ORDER BY gasto DESC
LIMIT 1


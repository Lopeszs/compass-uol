-- 16) Apresente a query para listar a quantidade média vendida de cada
-- produto agrupado por estado da federação. As colunas presentes no
-- resultado devem ser estado e nmprod e quantidade_media. Considere
-- arredondar o valor da coluna quantidade_media na quarta casa decimal.
-- Ordene os resultados pelo estado (1°) e nome do produto (2°).
-- Obs: Somente vendas concluidas.

SELECT 
	estado, 
	nmpro, 
	ROUND(AVG(qtd), 4) AS quantidade_media
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY estado, nmpro
ORDER BY estado, nmpro
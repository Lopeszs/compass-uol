-- 14) Apresente a query para listar o gasto médio por estado da federação. As
-- colunas presentes no resultado devem ser estado e gastomedio. Considere
-- apresentar a coluna gastomedio arredondada na segunda casa decimal e
-- ordenado de forma decrescente.
-- Observação: Apenas vendas com status concluido.

WITH total_vendas AS (
    SELECT estado,
           (qtd * vrunt) AS t_vendas
    FROM tbvendas
    WHERE status = 'Concluído'
)
SELECT 
    estado, 
    ROUND(AVG(t_vendas), 2) AS gastomedio
FROM total_vendas
GROUP BY estado
ORDER BY gastomedio DESC;
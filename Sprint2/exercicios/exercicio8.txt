-- 8) Apresente a query para listar o codigo e o nome do vendedor com maior
-- número de vendas (contagem), e que estas vendas estejam com o status
-- concluida. As colunas presentes no resultado devem ser, portanto, cdvdde
-- nmvdd.

SELECT 
    vendedor.cdvdd, 
    vendedor.nmvdd
FROM tbvendedor AS vendedor
LEFT JOIN tbvendas AS vendas
ON vendedor.cdvdd = vendas.cdvdd
WHERE vendas.status = 'Concluído'
GROUP BY vendedor.cdvdd, vendedor.nmvdd
HAVING COUNT(vendas.cdven) = (
    SELECT MAX(qtd_vendas)
    FROM (
        SELECT COUNT(vendas.cdven) AS qtd_vendas
        FROM tbvendas AS vendas
        WHERE vendas.status = 'Concluído'
        GROUP BY vendas.cdvdd
    ) AS subconsulta
)


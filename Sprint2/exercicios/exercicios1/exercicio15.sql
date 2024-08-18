-- 15) Apresente a query para listar os codigos das vendas identificadas como
-- deletadas. Apresente o resultado em ordem crescente.

SELECT cdven
FROM tbvendas
WHERE deletado = true
ORDER BY cdven 

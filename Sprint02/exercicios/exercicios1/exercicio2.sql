-- 2) Apresente a query para listar os 10 livros mais caros. Ordenar as linhas 
-- pela coluna valor, em ordem decrescente. Atenção as colunas esperadas no
-- resultado final: titulo, valor.

SELECT titulo, valor
FROM livro
ORDER BY valor DESC
LIMIT 10
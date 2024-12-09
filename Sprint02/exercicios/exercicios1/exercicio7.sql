-- 7) Apresente a query para listar o nome dos autores com nenhuma
-- publicação. Apresenta-los em ordem crescente.

SELECT aut.nome
FROM autor AS aut
LEFT JOIN livro AS liv 
ON aut.codautor = liv.autor
WHERE liv.cod IS NULL
ORDER BY aut.nome

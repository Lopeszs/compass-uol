-- 4) Apresente a query para listar a quantidade de livros publicada por cada
-- autor. Ordenar as linhas pela coluna nome (autor), em ordem
-- crescente. Alem desta, apresentar as colunas codautor, nascimento e
-- quantidade (total de livros de sua autoria).

SELECT 
    aut.nome,
    aut.codautor,
    aut.nascimento,
    COALESCE(COUNT(liv.cod), 0) AS quantidade
FROM autor aut
LEFT JOIN livro liv
ON liv.autor = aut.codautor
GROUP BY aut.nome, aut.codautor, aut.nascimento
ORDER BY aut.nome  

-- 6) Apresente a query para listar o autor com maior numero de livros
-- publicados. O resultado deve conter apenas as colunas codautor, nome,
-- quantidade_publicacoes.

SELECT 
	aut.codautor,
	aut.nome,
	COUNT(cod) AS quantidade_publicacoes
FROM livro AS liv
LEFT JOIN autor AS aut
ON liv.autor = aut.codautor
GROUP BY aut.nome
ORDER BY quantidade_publicacoes DESC
LIMIT 1


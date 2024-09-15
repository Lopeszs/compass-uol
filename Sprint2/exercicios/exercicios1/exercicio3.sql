-- 3) Apresente a query para listar as 5 editoras com mais livros na biblioteca.
-- O resultado deve conter apenas as colunas quantidade, nome, estado e
-- cidade. Ordenar as linhas pela coluna que representa a quantidade de livros
-- em ordem decrescente.

SELECT 
	edi.nome,
	ende.estado,
	ende.cidade,
	COUNT(*) AS quantidade
FROM livro as liv
LEFT JOIN editora as edi
ON liv.editora = edi.codeditora
LEFT JOIN endereco as ende
ON edi.endereco = ende.codendereco
GROUP BY edi.nome
ORDER BY quantidade DESC
LIMIT 5


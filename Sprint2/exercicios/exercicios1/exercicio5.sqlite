-- 5) Apresente a query para listar o nome dos autores que publicaram livros
-- atraves de editoras NAO situadas na regiao sul do Brasil. Ordene o
-- resultado pela coluna nome, em ordem crescente. Não podem haver nomes
-- repetidos em seu retorno.

SELECT DISTINCT aut.nome
FROM autor AS aut
LEFT JOIN livro AS liv
ON aut.codautor = liv.autor
LEFT JOIN editora AS edi
ON liv.editora = edi.codeditora
LEFT JOIN endereco AS ende
ON edi.endereco = ende.codendereco
WHERE ende.estado NOT IN ('PARANÁ','SANTA CATARINA', 'RIO GRANDE DO SUL')
ORDER BY aut.nome


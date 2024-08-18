# Evidências
-- NORMALIZANDO

(1 FN) - A tabela já está na primeira forma normal, pois cada campo pssui 
um único valor atômico e não há atributos multivalorados ou compostos

(2 FN) - para deixar a tabela na segunda forma normal, eu identifiquei
todos os atributos que não dependem da chave primária da tabela (idLcacao) e
criei novas entidades para eles, assim, criei as entidades: tbCliente, tbCarro,
tbCombustivel e tbVendedor. Após criadas as novas tabelas, aloquei os atributos
em suas respectivas tabelas e identifiquei em cada uma a chave primária,
de modo que os atributos sejam funcionalmente dependentes dela.

(imagem1)


(3 FN) - a relação já se encontra na terceira forma normal, todos
os atributos não-chave dependem totalmente da chave primária, sem 
dependências transitivas

(4 FN) - a relação já se encontra na quarta forma normal, pois em nenhuma das
tabelas há dependências multivaloradas, portanto não há necessidade de criação
de novas tabelas

(5 FN) - também já está na quinta forma normal, pois não há join dependencies
complexas que necessitam de decomposição adicional.
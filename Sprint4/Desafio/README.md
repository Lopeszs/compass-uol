# Etapas

1. [Etapa 1](etapa-1/Dockerfile)<br></br>
2. [Etapa 2](etapa-2/etapa-2.md)<br></br>
3. Etapa 3  
[Arquivo python](etapa-3/mascarar-dados.py)  
[Dockerfile](etapa-3/Dockerfile)


Para iniciar a etapa 1, adicionei o arquivo carguru.py ao diretório de desenvolvimento do desafio e criei um Dockerfile que descreve o processo para criar uma imagem Docker que executa o script Python. (colocar imagem do Dockerfile)
Com o Dockerfile criado, utilizei o seguinte comando no terminal para construir a imagem: (colocar comando aqui)
Em seguida, usei o comando para rodar o container: (comando aqui)
Ao executar o container, o script imprime no terminal o nome de um carro aleatório, escolhido a partir de uma lista de vários nomes de carros contidos no script, utilizando a função random(): (resultado aqui)
Na etapa 2 do desafio, criei um arquivo Markdown para responder ao questionamento sobre a possibilidade de reutilizar containers. Respondi que é possível, pois o Docker preserva o sistema de arquivos e as configurações do container. Para reiniciar um container parado, basta utilizar o comando: (comando aqui)
Como exemplo, reiniciei o container gerado na etapa 1 usando o comando: (comando aqui) e o container iniciou novamente como esperado: (resultado aqui)
Por fim, na etapa 3 do desafio, criei um arquivo mascarar-dados.py que possui um loop que só se encerra se o usuário digitar 0. Caso o usuário insira qualquer outro texto, o script converte a entrada para bytes e calcula o hash SHA-1 usando hashlib.sha1(). O resultado é convertido para uma string hexadecimal com hexdigest() e impresso no terminal. O programa continua solicitando valores até que a entrada seja 0. (exibir código aqui)
Após criar o arquivo Python, criei o Dockerfile responsável pela construção da imagem e o executei no terminal: (comando aqui)
Também dei o comando para rodar o container de forma que os inputs fossem inseridos no próprio terminal: (comando aqui)
Ao iniciar, o container executa os scripts Python descritos acima: (resultado aqui)

O desafio consiste no desenvolvimento de dois jobs no AWS Glue para processar e padronizar dados armazenados no bucket S3. Um dos jobs foi configurado para processar arquivos CSV e o outro para arquivos JSON.

## Script para Processamento de Arquivos CSV

Para iniciar o desafio, o primeiro passo foi criar dois jobs no serviço AWS Glue: um para processar dados no formato CSV e outro para processar arquivos JSON.

![Evidencia 1](../evidencias/evidencia_23.webp)<br></br>

Com os jobs criados, comecei a desenvolver o script para processar e padronizar os dados CSV contidos na camada Raw do bucket S3. O código pode ser consultado [aqui](processa_csv.py)

Iniciei o código importando as bibliotecas necessárias para o desenvolvimento do script em PySpark, além das APIs do AWS Glue, que permitem processar e transformar dados no serviço. Também foram inicializados, por padrão do job, os argumentos e o contexto:

![Evidencia 2](../evidencias/evidencia_24.webp)<br></br>

Os caminhos de entrada e saída foram definidos de acordo com a estrutura do Data Lake. Também foi definida a estrutura dos dados com colunas e tipos, garantindo a leitura correta do CSV no formato desejado:

![Evidencia 3](../evidencias/evidencia_25.webp)<br></br>

Os dados foram carregados utilizando "|" como delimitador de colunas, e o esquema definido foi aplicado para estruturar os dados:

![Evidencia 4](../evidencias/evidencia_26.webp)<br></br>

Em seguida, os dados foram tratados. Primeiro, foram removidas as linhas duplicadas considerando uma combinação única de id e nome do artista, mantendo apenas registros exclusivos. Os valores ausentes ou nulos (\N) foram substituídos por None em todas as colunas. Por fim, os dados foram filtrados para reter apenas os filmes dos gêneros comédia ou animação, lançados após 1990:

![Evidencia 5](../evidencias/evidencia_27.webp)<br></br>

Por último, o número de partições foi reduzido para 1, a fim de gerar um único arquivo de saída, e então o DataFrame foi gravado no bucket S3 no formato Parquet:

![Evidencia 6](../evidencias/evidencia_28.webp)<br></br>

Após alguns testes o script foi executado com sucesso no Glue e o arquivo Parquet foi persistido corretamente no bucket S3 na camada Trusted:

Job do Glue:
![Evidencia 7](../evidencias/evidencia_29.webp)

Arquivo no bucket S3:
![Evidencia 8](../evidencias/evidencia_30.webp)<br></br>

Após concluir o processamento dos dados CSV, o próximo passo foi criar o script para processar e padronizar os dados JSON, também contidos na camada Raw do bucket S3.<br></br>

## Script para Processamento de Arquivos JSON

No script, iniciei com a importação das bibliotecas necessárias, incluindo as transformações do AWS Glue e funções do PySpark. Também foi configurado o contexto do Glue, definindo o job com os argumentos iniciais e o contexto Spark:

![Evidencia 9](../evidencias/evidencia_31.webp)<br></br>

Os caminhos de entrada e saída foram definidos de acordo com a estrutura do Data Lake e os dados JSON foram carregados com a opção multiline habilitada para facilitar a leitura de arquivos no formato JSON estruturado:

![Evidencia 10](../evidencias/evidencia_32.webp)<br></br>

Em seguida, os valores vazios foram transformados em nulos, garantindo uma estrutura uniforme para o processamento dos dados. E para padronizá-los foram selecionadas e transformadas colunas específicas, incluindo o id do filme, title, original_title, release_date, e outros campos relevantes para a análise que será realizada ao final da Sprint 10:

![Evidencia 11](../evidencias/evidencia_33.webp)<br></br>

Para garantir a consistência dos dados, foram removidos registros sem id e registros duplicados, mantendo apenas IDs únicos. Em seguida, os dados foram particionados em um único arquivo para otimizar o armazenamento e consulta, e o DataFrame final foi salvo em formato Parquet no bucket S3:

![Evidencia 12](../evidencias/evidencia_34.webp)<br></br>

Após alguns testes o job foi executado com sucesso no Glue e o arquivo Parquet foi persistido corretamente no bucket S3 na camada Trusted:

Job do Glue:
![Evidencia 13](../evidencias/evidencia_35.webp)

Arquivo no bucket S3:
![Evidencia 14](../evidencias/evidencia_36.webp)<br></br>

Com os arquivos Parquet gerados, eles foram catalogados no AWS Data Catalog, possibilitando análise com o Amazon Athena.

Tabela para dados CSV:
![Evidencia 15](../evidencias/evidencia_37.webp)<br></br>

Tabela para dados JSON:
![Evidencia 16](../evidencias/evidencia_38.webp)<br></br>



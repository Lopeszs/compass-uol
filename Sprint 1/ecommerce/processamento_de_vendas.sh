#!/bin/bash

###########################################################################
#
# processamento_de vendas.sh - Script para o desafio final da Sprint 1 
#
# Descrição: .....................
#
# Exemplo de uso: ./prcessamento_de_vendas
#
###########################################################################


# Cria o diretório "vendas" e copia o arquivo "dados_de_vendas.csv" para dentro dele
mkdir vendas
cp dados_de_vendas.csv /vendas


# Entra no diretório "vendas" e cria o subdiretório "backup"
cd vendas
mkdir backup

# Altera o formato da data para yyyymmdd e atribui a variável "date_f"
date_f=$(date +"%Y%m%d")

# Copia o arquivo "dados_de_vendas.csv" para dentro da pasta "backup" com a data de execução
# como parte do nome do arquivo
cp dados_de_vendas.csv backup/dados-${date_f}.csv

# Entra no diretório "backup" e renomeia o arquivo
cd backup
mv dados-${date_f}.csv backup-dados-${date_f}.csv

touch relatorio.txt



#shell separa os comando por ";"
#echo "escreva aqui" - imprime uma mensagem
#date - mostra a data
#sort - ordena informações e imprime

#./ ou .processamento_de_vendas - executa o script
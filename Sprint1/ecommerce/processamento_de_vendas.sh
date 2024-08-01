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

#Vai até o diretório ecommerce para gerar o relatório
cd Desafio_Sprint_1/Sprint1/ecommerce/

# Cria o diretório "vendas" e copia o arquivo "dados_de_vendas.csv" para dentro dele
mkdir vendas
cp dados_de_vendas.csv vendas/

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

# Guarda a data do sistema
data_sys=$(date +"%Y/%m/%d %H:%M")

# extrai somente a coluna de datas
somente_datas=$(cut -d',' -f5 "backup-dados-${date_f}.csv" | tail -n +2 )

# Guarda a data do primeiro registro de vendas
primeira_data=$(echo "$somente_datas" | head -n 1)

# Guarda a data do último registro de vendas
ultima_data=$(echo "$somente_datas" | tail -n 1)

# Guarda a quantidade de itens diferentes da lista
qtd_itens=$(cut -d',' -f2 "backup-dados-${date_f}.csv" | tail -n +2 | sort | uniq | wc -l ) 

# Cria o arquivo relatorio.txt e imprime as informações
{
    echo "Data do sistema: $data_sys"
    echo
    echo "Data da primeira venda: $primeira_data" 
    echo
    echo "Data da última venda: $ultima_data" 
    echo
    echo "Quantidade total de itens diferentes vendidos: $qtd_itens"
    echo
    echo " ===== Primeiras 10 linhas do arquivo de backup dos dados: ====="
    echo
} > relatorio.txt

head -n 10 backup-dados-${date_f}.csv ; head -n 10 backup-dados-${date_f}.csv >> relatorio.txt

# Comprime arquivo de backup dos dados para .zip
zip -r backup-dados-${date_f}.zip  backup-dados-${date_f}.csv

# Remove o arquivo de backup dos dados
rm backup-dados-${date_f}.csv

# Volta para o diretório de vendas e apaga o arquivo "dados_de_vendas.csv"
cd ..
rm dados_de_vendas.csv


#./ ou .processamento_de_vendas - executa o script
#!/bin/bash

###########################################################################
#
# consolidador_de_processamento_de vendas.sh - Script para o desafio final da Sprint 1 
#
# Descrição: Script que une todos os relatórios gerados em um relatório final
#
# Exemplo de uso: ./consolidador_de_processamento_de_vendas
#
###########################################################################

# Navega até o diretório backup, procura todos os arquivos que começam com "relatorio"
# no nome, os une e gera um relatorio_final.txt
find vendas/backup/ -type f -name "relatorio*" -exec cat {} + > relatorio_final.txt

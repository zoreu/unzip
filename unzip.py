import argparse
import os
import zipfile
import sys

# obtém o caminho da pasta local do script
pasta_local = os.path.dirname(os.path.abspath(__file__))

# encontra o primeiro arquivo zip no diretório de trabalho atual
arquivos_zip = [arquivo for arquivo in os.listdir('.') if arquivo.endswith('.zip')]
if arquivos_zip:
    arquivo_zip = arquivos_zip[0]
else:
    arquivo_zip = None

# cria o parser e adiciona os argumentos
parser = argparse.ArgumentParser(description='Extrai um arquivo zip para um diretório especificado.')
parser.add_argument('-o', '--arquivo', metavar='ARQUIVO_ZIP', default=arquivo_zip, help='o caminho do arquivo zip para extrair (padrão: primeiro arquivo zip encontrado no diretório de trabalho atual)')
parser.add_argument('-d', '--destino', metavar='DESTINO', default=pasta_local, help='o caminho do diretório onde o arquivo zip será extraído (padrão: pasta local do script)')

# analisa os argumentos da linha de comando
args = parser.parse_args()

# verifica se o arquivo zip especificado existe
if args.arquivo is None:
    print('Nenhum arquivo zip encontrado no diretório de trabalho atual.')
    sys.exit(1)

if not os.path.isfile(args.arquivo):
    print(f'O arquivo zip "{args.arquivo}" não existe.')
    sys.exit(1)

# extrai o arquivo zip para o diretório especificado
with zipfile.ZipFile(args.arquivo, 'r') as zip_ref:
    zip_ref.extractall(args.destino)

print(f'O arquivo {args.arquivo} foi extraído com sucesso para o diretório {args.destino}.')

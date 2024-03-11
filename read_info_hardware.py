import psutil
import csv
import datetime
import time
import os


# Obtém a data atual e armazena essa data numa variável
data_atual = datetime.datetime.now()

# Faz a formatação da data como parte do nome do arquivo
data_medicao = data_atual.strftime("%d%m%Y-%H")

# Obtém o nome do host
nome_host = os.uname().nodename

nome_arquivo = nome_host + data_medicao + ".csv"

pasta_destino = 'caminho passando também o IP da máquina destino'

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

caminho_completo = os.path.join(pasta_destino, nome_arquivo)


# Função para obter e formatar a data do sistema
def buscar_dados_do_sistema():
    ram_percent = psutil.virtual_memory().percent
    swap_percent = psutil.swap_memory().percent
    cpu_percent = psutil.cpu_percent()

    return ram_percent, swap_percent, cpu_percent


def escrever_no_csv(data):
    with open(caminho_completo, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


# Função principal para executar as operações
def main(intervalo_de_medicao, tempo_total):
    tempo_inicial_de_medicao = time.time()
    with open(caminho_completo, 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["ram (%)", "swap (%)", "cpu (%)"])

    while (time.time() - tempo_inicial_de_medicao) < tempo_total:
        escrever_no_csv(buscar_dados_do_sistema())

        # espera um intervalo de tempo
        time.sleep(intervalo_de_medicao)


# Função para executar o script pelo período especificado
if __name__ == "__main__":
    main(10, 600)


import psutil
import csv
import datetime
import time
import os


# get the actual date and store in a variable
data_atual = datetime.datetime.now()

# formats the date as a part of the archive's name
nome_host = os.uname().nodename
data_medicao = data_atual.strftime("%d%m%Y-%H")
nome_arquivo = nome_host + data_medicao + ".csv"

pasta_destino = 'caminho'

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

caminho_completo = os.path.join(pasta_destino, nome_arquivo)


# function to get and format the system data
def buscar_dados_do_sistema():
    ram_percent = psutil.virtual_memory().percent
    swap_percent = psutil.swap_memory().percent
    cpu_percent = psutil.cpu_percent()
    # clock = psutil.cpu_freq().current

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

        # wait an interval
        time.sleep(intervalo_de_medicao)


# Executar o dashboard pelo período de tempo especificado
if __name__ == "__main__":
    main(10, 600)


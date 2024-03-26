import psutil
import datetime
import platform
import time
import os
import csv

# Obtendo a data para colocar no nome do arquivo
get_measurement_date = datetime.datetime.now().strftime("%Y_%m_%d")

file_name = f'{get_measurement_date}.csv'
destination_folder = platform.node() # Obtém o nome do dispositivo/máquina

# Criando a pasta
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Obtendo o caminho completo do arquivo
complete_path = os.path.join(destination_folder, file_name)

# função para obter as métricas do sistema
def get_data_system() -> tuple:
    # MEMÓRIA
    # Utilização da memória RAM
    ram_percent = psutil.virtual_memory().percent
    # Utilização da swap
    swap_percent = psutil.swap_memory().percent
    # # Utilização da cache (Windows)
    # cache_percent = (psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
    # CPU
    # Utilização da CPU
    cpu_percent = psutil.cpu_percent()
    # # DISCO
    # # Taxa de transferência de dados no disco em bytes
    # disk_info = psutil.disk_io_counters()
    # disk_transfer_rate = disk_info.read_bytes + disk_info.write_bytes
    # # Latência de acesso ao disco em ms
    # disk_latency = disk_info.read_time + disk_info.write_time
    # # REDE
    # # Velocidade de upload e download da rede em bytes/s
    # net_info = psutil.net_io_counters()
    # net_upload_speed = net_info.bytes_sent
    # net_download_speed = net_info.bytes_recv
    # # Latência da rede em ms
    # net_latency = net_info.errin + net_info.errout
    # # Número de processos em execução
    # num_processes = len(psutil.pids())
    # # Prioridade de processos
    # process = psutil.Process()
    # priority = process.nice()
    # # Tempo de inicialização
    # boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    # # Tempo de resposta do sistema
    # uptime = datetime.datetime.now() - boot_time
    # # Tempo de execução do sistema
    # system_runtime = datetime.datetime.now() - boot_time
    return (
        ram_percent, swap_percent, cpu_percent
        # , 
        # cache_percent, disk_transfer_rate, disk_latency,
        # net_upload_speed, net_download_speed, net_latency,
        # num_processes, priority, boot_time, uptime, system_runtime
        )

def check_if_file_exists(datapath: str):
    if not os.path.exists(datapath):
        with open(datapath, 'w', newline='') as file:
            write = csv.writer(file)
            write.writerow(
                ("ram (%)", "swap (%)", "cpu (%)",
                # "cache (%)",
                # "transferencia do disco em bytes",
                # "latencia do disco em ms", "vel. upload da rede", 
                # "vel. download da rede", "latencia da rede em ms", 
                # "processos em execucao", "prioridade de processos",
                # "tempo inicializacao do sistema", "tempo de resposta do sistema",
                # "tempo de execução do sistema"
                )
            )

# Função para persistir dados em arquivo csv
def save_data_in_csv(datapath: str, data: tuple) -> None:
    check_if_file_exists(datapath)
    with open(datapath, 'a+', newline='') as file:
        write = csv.writer(file)
        write.writerow(data)

def main(measuring_range: int, total_time: int) -> None:
    initial_measerement_time = time.time()
    while True:
        if(time.time() - initial_measerement_time) >= total_time:
            break
    
        save_data_in_csv(complete_path, get_data_system())
        # esperando um intervalo de tempo
        time.sleep(measuring_range)

# Função para executar o script pelo perído especificado
if __name__ == "__main__":
    main(10, 600)
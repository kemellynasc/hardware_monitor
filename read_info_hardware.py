import psutil
import csv
import time

def get_system_data():
    cpu_percent = psutil.cpu_percent()
    ram_percent = psutil.virtual_memory().percent
    swap_percent = psutil.swap_memory().percent
    return cpu_percent, ram_percent, swap_percent

def write_to_csv(data):
    with open('system_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    # Escreve o cabeçalho do arquivo CSV
    with open('system_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['CPU (%)', 'RAM (%)', 'Swap (%)'])

    # Coleta dados e escreve no arquivo CSV a cada 5 segundos
    while True:
        data = get_system_data()
        write_to_csv(data)
        time.sleep(30)


if __name__ == "__main__":
    main()

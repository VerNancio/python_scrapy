# import sys
import json

# sys.path.append('./so')
# import socket

# # Criar um socket raw na camada de rede (Layer 3)
# sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# # Vincular o socket a todos os interfaces e portas
# sniffer.bind(("0.0.0.0", 0))

# # Configurar o socket para incluir cabeçalhos IP
# sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# print("Capturando pacotes TCP...")

# try:
#     while True:
#         # Receber pacotes
#         raw_packet, addr = sniffer.recvfrom(65535)
#         print(f"Pacote capturado de {addr}: {raw_packet}")
# except KeyboardInterrupt

with open('ramal_users_categ.json', 'r') as f:

    us = json.loads(f.read())

    for u in range(len(us)):

        print()

        for i in :
            print(i)
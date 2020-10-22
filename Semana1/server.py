#!/usr/bin/python3

import socket
from datetime import datetime, date

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',80))
    s.listen(2)

    while True:
        conS, clientAddr= s.accept()
        print(clientAddr)
        with conS:
            data = conS.recv(32)
            data= str(data)[2:-1]
            conS.send(b'Recebido')
            print(data)
            if data == "Dojo":
                dia = date.today().strftime("%b-%d-%Y")
                hora = datetime.now().strftime("%h-%M-%S")
                log = "log-" + dia + "-" + hora + clientAddr[0] + ".txt"
                with open(log, 'w+') as f:
                    f.write(data + "\n")
                    f.close()

            conS.close()
main()

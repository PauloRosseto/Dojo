#!/usr/bin/python3

import socket
import sys


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((socket.gethostname(), 80))
        s.listen(2)
        clientS, address = s.accept()
        while clientS:
            print("Conectado a", address)
            while True:
                data = s.recv(1024)
                if not data:
                    break
                s.send()

main()

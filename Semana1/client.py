import socket


def main():
    ip = input("Digite um IP: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, 80))
        msg = input("Digite uma Mensagem: ")
        msglen = s.send(bytes(msg, 'utf-8'))
        if msglen > 0:
            print("Message sent")
        data = s.recv(1024)
        print(data)

main()

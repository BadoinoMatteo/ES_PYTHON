import socket
import time
import turtle

localIP= "127.0.0.1"
localPort= 80
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dict={}
s.bind((localIP, localPort))
listaComandi=['forward', 'backward', 'left', 'right']


while True:
    ricevuto, addres = s.recvfrom(1024)
    dict[addres]=(turtle.Turtle())
    stringa=ricevuto.decode().split('_')
    if(addres in dict):
        while True:
            variabile = (int)(stringa[1])
            if (listaComandi[0] == stringa[0]):
                dict[addres].forward(variabile)
                break
            if (listaComandi[1] == stringa[0]):
                dict[addres].backward(variabile)
                break
            if (listaComandi[2] == stringa[0]):
                dict[addres].left(variabile)
                break
            if (listaComandi[3] == stringa[0]):
                dict[addres].right(variabile)
                break
    else:
        print("non presente")
    print("comando eseguito")


s.close()
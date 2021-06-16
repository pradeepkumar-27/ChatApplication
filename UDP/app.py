import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "0.0.0.0"
port = 7070

sock.bind((ip, port))

def receiveMsg():
    while True:
        data = sock.recvfrom(1024)
        print(data[1][0] + " : " + str(data[0]))

def sendMsg():
    while True:
        data = input()
        data = data.encode()
        sock.sendto(data, (client, port))

receiveThread = threading.Thread(target=receiveMsg)
sendThread = threading.Thread(target=sendMsg)

client = input("Enter client ip : ")

receiveThread.start()
sendThread.start()
import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip = "0.0.0.0"
port = 7070

sock.bind((ip, port))
sock.listen()

def receiveMsg(conn, addr):
    while True:
        data = conn.recv(256)
        print(data)

while True:
    conn, addr = sock.accept()
    receiveMsgThread = threading.Thread(target=receiveMsg, args=(conn, addr))
    receiveMsgThread.start()
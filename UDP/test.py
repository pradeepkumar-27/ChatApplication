"""import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(type(ip))"""

import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
port = 7070

sock.bind((ip, port))

data = sock.recvfrom(1024)
print(data)
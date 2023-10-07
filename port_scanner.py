import sys
import socket
import listener
from listener import *
from listener import key

import sys
import socket
import keyboard

objective = socket.gethostbyname(input("Nombre de la IP: "))

for port in range(1, 100):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((objective, port))
    if result == 0:
        print("Puerto abierto:", port)
    sock.close()

if keyboard.is_pressed("F11") or keyboard.is_pressed("F12"):
    sys.exit()
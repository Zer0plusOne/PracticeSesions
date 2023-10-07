import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("El nombre del equipo es:", hostname)

print("Tu IP es:", ip)
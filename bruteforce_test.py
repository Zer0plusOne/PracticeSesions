import random
import keyboard
import sys

data_list = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=,.?"
chardData = list(data_list)

password = str(input("Ingresa una contraseña: "))
myguess = ""

while myguess != password:
    myguess = "".join(random.choices(chardData, k=len(password)))
    print(myguess)

if keyboard.is_pressed("F11") or keyboard.is_pressed("F12"):
    sys.exit()
    
print("La contraseña es:", myguess)


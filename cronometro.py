from time import sleep
import os

os.system("clear")
hora = minuto = segundo = 0
form = "0"

while True:
    if segundo < 60:
        if segundo < 10:
            print(f"{hora}:{minuto}:0{segundo}")
            sleep(1)
            os.system("clear")
        else:
            print(f"{hora}:{minuto}:{segundo}")
            sleep(1)
            os.system("clear")
        segundo += 1
    if segundo == 60:
        segundo = 0
        minuto += 1
    if minuto == 60:
        minuto = 0
        hora += 1
        

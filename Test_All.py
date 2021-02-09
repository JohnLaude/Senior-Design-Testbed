# This checks all the pis in the system
import subprocess

# Parameters
Nodes = []
flag = [0]*5
def getName():
    for n in Nodes:
        print(str(n) + " hostname: ")
        args = "ssh pi@"+ str(n) +" hostname"
        subprocess.call(args, shell=True)

def ping_all():
    for n in Nodes:
        print(str(n) + " hostname: ")
        args = "ping "+ str(n)
        subprocess.call(args, shell=True)

def getIP():
    for n in Nodes:
        print(str(n) + " IP address: ")
        args = "ssh pi@"+ str(n) +" hostname -I"
        subprocess.call(args, shell=True)

# Sudo is used to give us access to the
def route():
    for n in Nodes:
        print(str(n) + " IP address: ")
        args = "ssh pi@"+ str(n)+ " sudo route -ne"
        subprocess.call(args, shell=True)

def speedtest():
        for n in Nodes:
            print("\n"+ str(n) + " speedtest: ")
            args = "ssh pi@"+ str(n) +" speedtest-cli --simple"
            subprocess.call(args, shell=True)

print("Please input nodes here")
num = int(input("Input number of nodes: "), base=10)
while num > 0:
    Nodes.append(input("Input node name: "))
    num -= 1


# List of flags and prompts
flag[0] = input("Ping devices? (Y/N) ")
flag[1] = input("Get hostname? (Y/N) ")
flag[2] = input("Get IP? (Y/N) ")
flag[3] = input("Get routing? (Y/N) ")
flag[4] = input("Run speedtest? (Y/N) ")

# Functions
if (flag[0] == "Y")or(flag[0] == "y"):
    ping_all()
if (flag[1] == "Y")or(flag[1] == "y"):
    getName()
if (flag[2] == "Y")or(flag[2] == "y"):
    getIP()
if (flag[3] == "Y")or(flag[3] == "y"):
    route()
if (flag[4] == "Y")or(flag[3] == "y"):
    speedtest()


import subprocess
##Parameter List##
# list of Nodes
Nodes = []
# Iperf values: default value interval 1 second, runtime 10 seconds
iperf_prm  = [1, 10]
# 5 Flags all set to 0
flag = [0]*5
input_flag = 1
#Get hostname
def getName():
    for n in Nodes:
        print(str(n) + " hostname: ")
        args = "ssh pi@"+ str(n) +" hostname"
        subprocess.call(args, shell=True)
#Get IP
def getIP():
    for n in Nodes:
        print(str(n) + " IP address: ")
        args = "ssh pi@"+ str(n) +" hostname -I"
        subprocess.call(args, shell=True)
#Iperf
def iperf(i, t):
    subprocess.call("ssh pi@Node1 iperf -s -i" + str(i), shell=True)
    print("Iperf results of Node: ")
    subprocess.call("ssh pi@Node2 iperf -c Node1 -i" + str(i)+ " -t" + str(t), shell=True)
#Speedtest
def speedtest():
        for n in Nodes:
            print("\n"+ str(n) + " speedtest: ")
            args = "ssh pi@"+ str(n) +" speedtest-cli --simple"
            subprocess.call(args, shell=True)

# Main code and testscript.
print("Please input nodes here")
num = int(input("Input number of nodes: "), base=10)
while num > 0:
    Nodes.append(input("Input node name: "))
    num -= 1
flag[0] = input("Get hostname? (Y/N) ")
flag[1] = input("Get IP? (Y/N) ")
flag[2] = input("Run Iperf (Y/N) ")
if (flag[2] == "Y")or(flag[2] == "y"):
    flag[4] = input("Change parameters?(Y/N) ")
    if (flag[4] == "Y")or(flag[4] == "y"):
        iperf_prm[0] = input("Interval time: ")
        iperf_prm[1] = input("Runtime: ")
flag[3] = input("run speedtest (Y/N) ")
if (flag[0] == "Y")or(flag[0] == "y"):
    getName()
if (flag[1] == "Y")or(flag[1] == "y"):
    getIP()
if (flag[2] == "Y")or(flag[2] == "y"):
    iperf(iperf_prm[0], iperf_prm[1])
if (flag[3] == "Y")or(flag[3] == "y"):
    speedtest()

# AUTHOR: John Carlo Laude
# Date: 10/21/2020
# Title: User Device Class Module
import subprocess
import os
##Parameter List##
name = "Node2"
iperf_prm  = [1, 10]
##"User Devices", "IP","RSS", "Routing", "BIT RATE", "ON/OFF"
class Station:
    # init method or constructor
    def __init__(self, Name):
        self.Name = Name
        self.IP = 0
        self.routing = " "
        self.Ping = 0
        self.Download = 0
        self.Upload = 0
        self.Date = " "
        self.Time = " "

    def get_name(self):
        return self.Name

    def get_IP(self):
        args = "ssh pi@"+ self.Name +" hostname -I"
        s = subprocess.check_output(args)
        s = str(s)
        out = s.split(" ")
        self.IP = out[0][2:]

    def ping(self):
        args = "ping google.com"
        subprocess.call(args, shell=True)

    def iperf(self, i, t, ap_IP):
        print("Iperf results of Node: ")
        subprocess.call("ssh pi@Node2 iperf -c "+ str(ap_IP) +" -i" + str(i)+ " -t" + str(t), shell=True)

    def update(self):
        self.get_name()
        self.get_IP()
        self.speedtest()
        #self.iperf(iperf_prm[0], iperf_prm[1])
        self.date()

    def speedtest(self):
        args = "ssh pi@"+ self.Name +" speedtest-cli --simple"
        s = subprocess.check_output(args)
        s = str(s)
        out = s.split(" ")
        self.Ping = out[1]
        self.Download = out[3]
        self.Upload = out[5]
    # The date is based on the raspberry pi
    def date(self):
        args = "ssh pi@"+ self.Name +" date"
        s = subprocess.check_output(args)
        out = str(s.decode('utf-8'))
        out = out.split(" ")
        str1 = " "
        self.Date = str1.join(out[0:4])
        self.Time = str1.join(out[4:6])

    def print(self):
        print(self.Name + " Hostname: ")
        print(self.Name)
        print(self.Name + " IP address: ")
        print(self.IP)
        print("Ping: ")
        print(str(self.Ping) + " ms")
        print("Download: ")
        print(str(self.Download)+ " Mbit/s")
        print("Upload: ")
        print(str(self.Upload) + " Mbit/s")
        print("Date: ")
        print(str(self.Date))
        print("Time: ")
        print(str(self.Time))


#g = Station(name)
#print("Initial:")
#g.print()
#g.update()
#print("Updated:")
#g.print()
# Main code and testscript.
#g.iperf(iperf_prm[0], iperf_prm[1], 10.3.141.1)
#g.ping()

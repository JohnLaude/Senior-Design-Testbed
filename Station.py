# AUTHOR: John Carlo Laude
# Date: 10/21/2020
# Title: User Device Class Module
import subprocess
import os
##Parameter List##
name = "10.1.1.4"
iperf_prm  = [10, 10, "10.1.101.1"]
##"User Devices", "IP","RSS", "Routing", "BIT RATE", "ON/OFF"
class Station:
    # init method or constructor
    def __init__(self, Name):
        self.Name = Name
        self.Control_IP = 0
        self.Test_IP = 0
        self.nodetype = "Station"
        self.cntrl_routing = "10.1.1.0"
        self.routing = "10.1.101.1"
        self.Ping = 0
        self.Download = 0
        self.Upload = 0
        self.iperf_trans = 0
        self.iperf_band = 0
        self.Date = " "
        self.Time = " "

    def get_name(self):
        return self.Name

    def get_routing(self):
        return self.routing

    def set_routing(self, routing):
        self.routing = routing
        return self.routing
    def get_IP(self):
        # Do a command
        args = "ssh pi@"+ self.Name +" hostname -I"
        # Take the output
        s = subprocess.check_output(args)
        # Parse and handle the values
        s = str(s)
        out = s.split(" ")
        self.Control_IP = out[0][2:]
        self.Test_IP =out[1]
        if len(self.Control_IP) > 9:
            self.Test_IP = self.Control_IP
            self.Control_IP = out[1]

    def ping(self):
        # Call the argument
        args = "ping google.com"
        s = subprocess.check_output(args)
        out = str(s.decode('utf-8'))
        out = out.split(" ")
        num = len(out)
        self.Ping = out[num -1][:1]
    # Default iperf. Uplink throughput. Client to server

    def iperf(self,port):
        args = "ssh pi@"+ str(self.Name)+" iperf -c " +str(self.routing)+ " -p " + str(port)
        s = subprocess.check_output(args)
        out = str(s.decode('utf-8'))
        out = out.split(" ")
        num = len(out)
        data1 = out[num -5:]
        return data1
        
    # Bidirectional Sequential. Uplink then downlink
    def iperf_r(self,port):
        args = "ssh pi@"+ str(self.Name)+" iperf -c " +str(self.routing)+ " -p " + \
        port+ " -r"
        s = subprocess.check_output(args)
        out = str(s.decode('utf-8'))
        out = out.split(" ")
        num = len(out)
        data1 = out[num -27:num -22]
        data2 = out[num-5:]
        return data1 + data2
    # Bidirectional Simultaneous. Downlink then uplink
    def iperf_d(self,port):
        args = "ssh pi@"+ str(self.Name)+" iperf -c " +str(self.routing)+ " -p " +\
        port+ " -d"
        s = subprocess.check_output(args)
        out = str(s.decode('utf-8'))
        out = out.split(" ")
        num = len(out)
        data2 = out[num -16:num -10]
        data1 = out[num-5:]
        return data1 + data2

    def tx_power(self,num):
        args = "ssh pi@" +self.Name+ " sudo iwconfig wlan0 txpower " + str(num)
        subprocess.call(args, shell=True)
    def update(self):
        self.get_name()
        self.get_IP()
        self.date()
        self.ping()

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

    def route(self):
        for n in Nodes:
            print(self.Name + " IP address: ")
            args = "ssh pi@"+ self.Name+ " sudo route -ne"
            subprocess.call(args, shell=True)
    def print(self):
        print("/////////////////////////////////")
        print(self.Name + " Hostname: ")
        print(self.Name)
        print(self.Name + " Control IP address: ")
        print(self.Control_IP)
        print("Test IP address: ")
        print(self.Test_IP)
        print("Ping: ")
        print(str(self.Ping) + " ms")
        #print("Download: ")
        #print(str(self.Download)+ " Mbit/s")
        #print("Upload: ")
        #print(str(self.Upload) + " Mbit/s")
        #print("Date: ")
        print(str(self.Date))
        print("Time: ")
        print(str(self.Time))
        print("Iperf Transfer: ")
        print(str(self.iperf_trans))
        print("Iperf Bandwidth: ")
        print(str(self.iperf_band))

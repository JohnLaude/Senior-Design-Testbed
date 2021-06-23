# AUTHOR: John Carlo Laude
# Date: 10/21/2020
# Title: User Device Class Module
import subprocess
import os
import re
##Parameter List##
name = "10.1.1.4"
iperf_prm  = [10, 10, "10.1.101.1"]
##"User Devices", "IP","RSS", "Routing", "BIT RATE", "ON/OFF"
class Station:
    # init method or constructor
    def __init__(self, Name):
        self.Control_IP = Name
        self.hostname = 0
        self.Test_IP = 0
        self.nodetype = 'Station'
        self.cntrl_routing = "10.1.1.0"
        self.routing = "10.1.101.1"
        self.SSID = "NA"
        self.Ping = 0
        self.Date = " "
        self.Time = " "

    def get_name(self):
        args = "ssh pi@"+ self.Control_IP +" hostname"
        # Take the output
        s = subprocess.check_output(args)
        out = str(s.decode('utf-8'))
        out= re.split('\s|(?<!\d)[,.](?!\d)\n',out)
        self.hostname = out[0]

    def get_routing(self):
        return self.routing

    def set_routing(self, routing):
        self.routing = routing
        return self.routing
    def get_IP(self):
        # Do a command
        args = "ssh pi@"+ self.Control_IP +" hostname -I"
        # Take the output
        s = subprocess.check_output(args)
        # Parse and handle the values
        s = str(s)
        out = s.split(" ")
        self.Control_IP = out[0][2:]
        self.Test_IP =out[1]
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
        args = "ssh pi@"+ str(self.Control_IP)+" iperf -c " +str(self.routing)+ " -p " + str(port)
        s = subprocess.check_output(args)
        out = str(s.decode('utf-8'))
        out = out.split(" ")
        num = len(out)
        #data1 = out[num -5:]
        data1 = out[num -5]
        return data1

    # Bidirectional Sequential. Uplink then downlink
    def iperf_r(self,port):
        args = "ssh pi@"+ str(self.Control_IP)+" iperf -c " +str(self.routing)+ " -p " + \
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
        args = "ssh pi@"+ str(self.Control_IP)+" iperf -c " +str(self.routing)+ " -p " +\
        port+ " -d"
        s = subprocess.check_output(args)
        out = str(s.decode('utf-8'))
        out = out.split(" ")
        num = len(out)
        data2 = out[num -16:num -10]
        data1 = out[num-5:]
        return data1 + data2

    def tx_power(self,num):
        args = "ssh pi@" +self.Control_IP+ " sudo iwconfig wlan0 txpower " + str(num)
        subprocess.call(args, shell=True)
    def update(self):
        self.get_name()
        self.get_IP()
        self.date()
        self.ping()

    def speedtest(self):
        args = "ssh pi@"+ self.Control_IP +" speedtest-cli --simple"
        s = subprocess.check_output(args)
        s = str(s)
        out = s.split(" ")
        self.Ping = out[1]
        self.Download = out[3]
        self.Upload = out[5]
    # The date is based on the raspberry pi
    def date(self):
        args = "ssh pi@"+ self.Control_IP +" date"
        s = subprocess.check_output(args)
        out = str(s.decode('utf-8'))
        out = out.split(" ")
        str1 = " "
        self.Date = str1.join(out[0:4])
        self.Time = str1.join(out[4:6])

    def route(self):
        for n in Nodes:
            print(self.Control_IP + " IP address: ")
            args = "ssh pi@"+ self.Control_IP+ " sudo route -ne"
            subprocess.call(args, shell=True)

    def switch_ap(self, network_id):
        args1 = "ssh pi@" + self.Control_IP + " sudo wpa_cli  select_network " + str(network_id)
        args2 = "ssh pi@" + self.Control_IP + " sudo wpa_cli save_config"
        args3 = "ssh pi@" + self.Control_IP + " sudo reboot"
        subprocess.call(args1, shell=True)
        subprocess.call(args2, shell=True)
        self.list_network()
        subprocess.call(args3, shell=True)

    def list_network(self):
        args = "ssh pi@" + self.Control_IP + " sudo wpa_cli list_network"
        s = subprocess.check_output(args)
        out = str(s.decode('utf-8'))
        return out

    def STATION_TO_AP(self):
        args = "ssh pi@" + self.Control_IP + " sudo sh CLIENT_TO_AP.sh"
        subprocess.call(args, shell=True)

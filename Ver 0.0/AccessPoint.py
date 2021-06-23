# AUTHOR: John Carlo Laude
# Date: 10/21/2020
# Title: User Device Class Module
import subprocess
import os
from Station import Station
import re
##Parameter List##
name = "Node1"
iperf_prm  = [1]
##"User Devices", "IP","RSS", "Routing", "BIT RATE", "ON/OFF"
class AccessPoint(Station):
    # init method or constructor
    def __init__(self, Name):
        super().__init__(Name) # Node/Station SuperClass
        self.Control_IP = Name
        self.hostname = 0
        self.Test_IP = 0
        self.nodetype = 'Access Point'
        self.routing = "NA"
        self.SSID = "NA"
        self.Ping = 0
        self.num_of_dev = 0

    def get_ap_IP(self):
        args = "ssh pi@"+ self.Control_IP +" hostname -I"
        s = subprocess.check_output(args)
        s = str(s)
        out = s.split(" ")
        self.Test_IP = out[1]
        self.Control_IP = out[0]

    def num_dev(self):
        print("Number of devices connected")
        args = "iw dev wlan0 station dump|grep Station|wc -l"
        s = subprocess.check_output(args)
        self.num_of_dev = s

    def iperf_start(self, port):
        args1 = "ssh pi@" + str(self.Control_IP) + " screen -d -m iperf -s -p " + str(port)
        subprocess.call(args1, shell = True)

    def iperf_stop(self,num):
        self.processes[num].terminate()

    def set_to_station(self):
        args1 = "ssh pi@" + str(self.Control_IP) + " screen -d -m iperf -s -p " + str(port)
        subprocess.call(args1, shell = True)
        pass

    def get_SSID(self):
        args = "ssh pi@"+ str(self.Control_IP)+" sudo iw wlan0 info"
        s = subprocess.check_output(args)
        out = str(s.decode('utf-8'))
        out = re.split('\s|(?<!\d)[,.](?!\d)',out)
        self.SSID = out[13]

    def AP_TO_STATION(self):
        args = "ssh pi@" + self.Control_IP + " sudo sh AP_TO_CLIENT.sh"
        subprocess.call(args, shell=True)

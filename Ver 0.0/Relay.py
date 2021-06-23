# AUTHOR: John Carlo Laude
# Date: 10/21/2020
# Title: User Device Class Module
import subprocess
import os
from Station import Station
##Parameter List##
name = "Node1"
iperf_prm  = [1, 10]
##"User Devices", "IP","RSS", "Routing", "BIT RATE", "ON/OFF"
class Relay(Station):
    # init method or constructor
    def __init__(self, Name):
        super().__init__(Name)
        self.Name = Name
        self.IP = 0
        self.ap_IP = 0
        self.nodetype = "Access Point"
        self.routing = "WiFi AP"
        self.Ping = 0
        self.Download = 0
        self.Upload = 0


    def get_ap_IP(self):
        args = "ssh pi@"+ self.Name +" hostname -I"
        s = subprocess.check_output(args)
        s = str(s)
        out = s.split(" ")
        self.ap_IP = out[1]

    def update_relay(self):
        self.get_name()
        self.get_IP()
        self.speedtest()
        self.get_ap_IP()
        print("\nUpated Relay Values ")

# Main code and testscript.
#g = Relay(name)
#print("Initial Values ")
#g.update_relay()
#g.print()
#g.update_relay()

# AUTHOR: John Carlo Laude
# Date: 10/21/2020
# Title: User Device Class Module
import subprocess
import os
from Station import Station
##Parameter List##
name = "Node1"
iperf_prm  = [1]
##"User Devices", "IP","RSS", "Routing", "BIT RATE", "ON/OFF"
class AccessPoint(Station):
    # init method or constructor
    def __init__(self, Name):
        super().__init__(Name) # Node/Station SuperClass
        self.Name = Name
        self.IP = 0
        self.routing = " "
        self.Ping = 0
        self.Download = 0
        self.Upload = 0

    def iperf_AP(self, i):
        try:
            subprocess.call("ssh pi@Node1 iperf -s -i" + str(i), shell=True)
        except:
            print("Server is ready")

    def update_AP(self):
        self.get_name()
        self.get_IP()
        self.speedtest()
        self.iperf_AP(iperf_prm[0])

# Main code and testscript.
#g = AccessPoint(name)
#print("Initial Values ")
#g.print()
#g.update_AP()
#print("\nUpated Values ")
#g.print()
#g.iperf(iperf_prm[0], iperf_prm[1])
#g.ping()

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
        self.Control_IP = 0
        self.Test_IP = 0
        self.nodetype = "Access Point"
        self.routing = "Wifi AP"
        self.Ping = 0
        self.Download = 0
        self.Upload = 0
        self.iperf_trans = "NA"
        self.iperf_band = "NA"
        self.num_of_dev = 0
        self.processes = []

    def iperf_AP(self, i):

        try:
            subprocess.call("ssh pi@"+str(self.Control_IP)+" iperf -s -i" + str(i), shell=True)
        except:
            print("Server is ready")

    def get_ap_IP(self):
        args = "ssh pi@"+ self.Name +" hostname -I"
        s = subprocess.check_output(args)
        s = str(s)
        out = s.split(" ")
        self.Test_IP = out[1]
        self.Control_IP = out[0]

    def wifi_on(self):
        subprocess.call("sudo service hostapd start")
        print("hostapd service is on")

    def wifi_off(self):
        subprocess.call("sudo service hostapd stop")
        print("hostapd service is off")

    def num_dev(self):
        print("Number of devices connected")
        args = "iw dev wlan0 station dump|grep Station|wc -l"
        s = subprocess.check_output(args)
        self.num_of_dev = s

    def iperf_start(self, port):
        args1 = "ssh pi@" + str(self.Name) + " iperf -s -p " + str(port)
        process = subprocess.Popen(args = args1, stdin=None, stdout=None, stderr=None,shell = True,close_fds=True)
        process.communicate()
        self.processes.append(process)

    def iperf_stop(self,num):
        self.processes[num].terminate()


    def update_AP(self):
        self.get_name()
        self.get_IP()
        self.get_ap_IP()
        #self.speedtest()
        #self.iperf_AP(iperf_prm[0])
        self.date()

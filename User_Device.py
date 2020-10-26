# AUTHOR: John Carlo Laude
# Date: 10/21/2020
# Title: User Device Class Module

##"User Devices", "IP","RSS", "Routing", "BIT RATE", "ON/OFF"
class User_Device:    
    # init method or constructor    
    def __init__(self, IP,RSS, routing, bitrate, ON_OFF):  
        # This is a string
        self.IP = IP
        # All the values are integers
        self.RSS = RSS
        self.routing = routing 
        self.bitrate = bitrate
        self.ON_OFF = ON_OFF

    def get_IP(self):
        return self.IP
    def function_whatever(self):
        pass

    def ssh(self):
        pass

    def iperf(self):
        pass

    def update(self, IP, RSS, routing, bitrate, ON_OFF):
        self.IP = IP
        self.RSS = RSS
        self.routing = routing 
        self.bitrate = bitrate
        self.ON_OFF = ON_OFF
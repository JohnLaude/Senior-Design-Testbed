# AUTHOR: John Carlo Laude
# Date: 10/21/2020
# Title: Relay Access Point Class Module

class Relay_AP:    
    # init method or constructor    
    def __init__(self, IP, routing, rate_tx, on, transmit_pow, power_rx, out_port):  
        # This is a string
        self.IP = IP
        # All the values are integers
        self.routing = routing
        self.rate_tx = rate_tx
        self.transmit_pow = transmit_pow
        self.power_rx = power_rx
        self.out_port = out_port
        # Boolean/Flags
        self.on = on
    
    # Returns the IP
    def get_IP(self):
        return self.IP

    # Change the rate
    def rate_change(self):
        # Use the linux command line to update the transfer
        pass
    
    # Switches the boolean on or off
    def on_off(self):
        # Inverses the flag
        self.on = not self.on

    # Check the number of devices connected
    def num_connected(self):
        # Use linux command line to check how many devcies are connect to access point 
        pass

    def set_transmit_pow(self):
        # Set the transmit power in Linux
        pass

   

    # Updates the values
    def update(self, IP, routing, rate_tx, on, transmit_pow, power_rx, out_port):
        self.IP = IP
        # All the values are integers
        self.routing = routing
        self.rate_tx = rate_tx
        self.power_rx = power_rx
        self.transmit_pow = transmit_pow
        self.out_port = out_port
        # Boolean/Flags
        self.on = on
        

    
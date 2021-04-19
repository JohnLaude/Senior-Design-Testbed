# AUTHOR: John Carlo Laude
# Date: 12/21/2020
# Title: User Device Class Module
# Description: This is the Testbed Controller class file in which everything is
# going to be controled in. All the classes will be imported here.
import subprocess
from multiprocessing import Process, Pipe
import os
import itertools
import csv
from AccessPoint import AccessPoint
from Station import Station
from Relay import Relay
import xlwt
from xlwt import Workbook


################ Parameter List ################
name = "10.1.1.2"
name1 = "10.1.1.3"
name2 = "10.1.1.4"
iperf_prm  = [1]
num_node = 2
filename = "data3.csv"

################ Parameter List ################

##"User Devices", "IP","RSS", "Routing", "BIT RATE", "ON/OFF"
class TB_controller:
    # init method or constructor
    def __init__(self):
        # List of nodes
        self.Node_List = []
        self.route_list = []
        self.m = 0
        self.row = 1
        self.data = []

    def add(self, name, num, routing):
        #name = input("Please input a Node ")
        #num = int(input("What tye of node? \n1.Station \n2.AccessPoint \n3.Relay \n"))
        if num == 'Station':
            c = Station(name)
        if num == 'Access Point':
            c = AccessPoint(name)
        if num == 'Relay':
            c = Relay(name)

        self.Node_List.append(c)
        c.set_routing(routing)
        self.route_list.append(c.routing)
        c.get_IP()
        output_val = [c.Name,c.Control_IP,c.Test_IP,c.nodetype,c.routing]
        return output_val

    def check_node(self):
        # Kind of like SSH.py but using
        pass
    def run_test(self):
        for n in self.Node_List:
            if n.nodetype == "Access Point":
                n.update_AP()
            else:
                n.update()
    def test_config(self):
        pass

    def save_data(self,data_out):
        with open(filename, 'w', newline = '') as csvfile:
        # creating a csv writer object
            csvwriter = csv.writer(csvfile)
        # writing the data rows
            csvwriter.writerows(data_out)

    def reset(self):
        pass

    def delete(self):
        pass

    def iperf_test(self,trials):
        for n in self.Node_List:
            if n.nodetype == "Access Point":
                n.iperf_start("12000")
            if n.nodetype == "Station":
                for i in range(trials):
                    print("Trial number "+ str(i))
                    self.data.append(n.iperf("12000"))

    def print(self):
        for n in self.Node_List:
            print("/////////////////////////////////")
            print(n.Name + " Hostname: ")
            print(n.Name)
            print("Test IP address: ")
            print(n.Test_IP)
            print("Date: ")
            print(str(n.Date))
            print("Time: ")
            print(str(n.Time))
            print("/////////////////////////////////")


# Main Test
#g = TB_controller()
#g.add('10.1.1.3', 'Access Point','10.1.101.0')
#g.add('10.1.1.4', 'Station','10.1.101.1')
#g.run_test()
#g.iperf_test(10)
#g.save_data(g.data)
#g.print()

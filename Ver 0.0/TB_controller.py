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
import re


################ Parameter List ################
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
        self.STN_LIST = []
        self.AP_LIST = []
        self.control_ip = []
        self.route_list = []
        self.test_prm = [10, 1, "n",10]
        self.m = 0
        self.row = 1
        self.data = {}

    def add(self, name, num):
        if num == 'Station':
            c = Station(name)
            self.STN_LIST.append(c)
        if num == 'Access Point':
            c = AccessPoint(name)
            self.AP_LIST.append(c)
            c.get_SSID()
        if num == 'Relay':
            c = Relay(name)
        c.get_name()
        self.Node_List.append(c)
        #c.set_routing(routing)
        self.route_list.append(c.routing)
        c.get_IP()
        self.control_ip.append(str(c.Control_IP))
        output_val = [c.hostname,c.Control_IP,c.Test_IP,c.nodetype, c.SSID]
        return output_val
    def current_val(self, node):
        output_val = [node.hostname,node.Control_IP,node.Test_IP,node.nodetype, node.SSID]
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
        self.Node_List.clear()
        return

    def delete(self, item):
        self.Node_List.remove(item)
        return

    def iperf_test(self,trials):
        data1 = []
        data2 = []
        flag = True
        for n in self.AP_LIST:
            n.iperf_start("12000")
        for i in range(trials):
            print("Trial number "+ str(i))
            for n in self.STN_LIST:
                if flag == True:
                    data1.append(n.iperf("12000"))
                    self.data[str(n.Control_IP)] = data1
                    flag = not flag
                else:
                    data2.append(n.iperf("12000"))
                    self.data[str(n.Control_IP)] = data2
                    flag = not flag

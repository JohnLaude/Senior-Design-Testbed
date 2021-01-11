# AUTHOR: John Carlo Laude
# Date: 12/21/2020
# Title: User Device Class Module
# Description: This is the Testbed Controller class file in which everything is
# going to be controled in. All the classes will be imported here.
import subprocess
import os
from AccessPoint import AccessPoint
from Station import Station
from Relay import Relay
import xlwt
from xlwt import Workbook


################ Parameter List ################
name = "Node1"
iperf_prm  = [1]
num_node = 2
xls_sheet = 'data.xls'

################ Parameter List ################

##"User Devices", "IP","RSS", "Routing", "BIT RATE", "ON/OFF"
class TB_controller:
    # init method or constructor
    def __init__(self):
        # List of nodes
        self.Node_List = []
        self.m = 0
        self.row = 1
        # Creat xls file

        self.wb = Workbook()

        # add_sheet is used to create sheet.
        self.sheet1 = self.wb.add_sheet('Sheet 1')
        self.sheet1.write(0, 0, 'Data Sheet')
        self.sheet1.write(0, 1, 'NAME')
        self.sheet1.write(0, 2, 'IP')
        self.sheet1.write(0, 3, 'ROUTING')
        self.sheet1.write(0, 4, 'PING')
        self.sheet1.write(0, 5, 'DOWNLOAD')
        self.sheet1.write(0, 6, 'UPLOAD')
        self.sheet1.write(0, 7, 'DATE')
        self.sheet1.write(0, 8, 'TIME STAMP')
        try:
            self.wb.save(xls_sheet)
        except:
            pass

    def add(self, name, num):
        #name = input("Please input a Node ")
        #num = int(input("What tye of node? \n1.Station \n2.AccessPoint \n3.Relay \n"))
        if num == 1:
            c = Station(name)
        if num == 2:
            c = AccessPoint(name)
        if num == 3:
            c = Relay(name)
        self.Node_List.append(c)

    def check_node(self):
        # Kind of like SSH.py but using
        pass
    def run_test(self):
        for n in self.Node_List:
            n.update()

    def test_config(self):
        pass

    def store(self):
        #Store data vlues from test
        n = self.Node_List[self.m]
        list = []
        list.append(n.Name)
        list.append(n.IP)
        list.append(n.routing)
        list.append(str(n.Ping))
        list.append(str(n.Download))
        list.append(str(n.Upload))
        list.append(str(n.Date))
        list.append(str(n.Time))
        self.m += 1
        return list

    def passing(self):
        # Write to an excel sheet
        for n in self.Node_List:
            self.sheet1.write(self.row, 1,n.Name)
            self.sheet1.write(self.row, 2,n.IP)
            self.sheet1.write(self.row, 3,n.routing)
            self.sheet1.write(self.row, 4,str(n.Ping))
            self.sheet1.write(self.row, 5,str(n.Download))
            self.sheet1.write(self.row, 6,str(n.Upload))
            self.sheet1.write(self.row, 7,str(n.Date))
            self.sheet1.write(self.row, 8,str(n.Time))
            self.row += 1
        self.wb.save('data.xls')
    def reset(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def print(self):
        for n in self.Node_List:
            print("/////////////////////////////////")
            print(n.Name + " Hostname: ")
            print(n.Name)
            print(n.Name + " IP address: ")
            print(n.IP)
            print("Ping: ")
            print(str(n.Ping) + " ms")
            print("Download: ")
            print(str(n.Download)+ " Mbit/s")
            print("Upload: ")
            print(str(n.Upload) + " Mbit/s")
            print("Date: ")
            print(str(n.Date))
            print("Time: ")
            print(str(n.Time))
            print("/////////////////////////////////")

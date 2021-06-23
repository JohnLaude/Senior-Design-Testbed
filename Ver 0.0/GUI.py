# AUTHOR: John Carlo Laude, Myles Toole, Haining Gao
# Date: 12/31/2020
# Title: Testbed Controller for Relay Testbed
# Description: This is a GUI class file meant to create an interface for our
# testbed with the main interface made from tkinter and sub packages from
# matplotlib and networkx. Class files are put in here so that they can be
# be used

import os
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import csv
from tkinter.filedialog import askopenfile
from matplotlib.figure import Figure # Download matplotlib
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import pandas as pd # Need to downloaded this
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from tkCanvasGraph import CanvasFrame, Vertex, Edge
from TB_controller import TB_controller
import re

######## Paramter List ##########
silver = '#C0C0C0'
bg_color = 'gray11'
title = "Testbed GUI"
btn_bg = 'lavender'
font_color = "white"
font = "Times"
btn_width = 20
pop_window = "200x95"
WINDOW_SIZE = "1200x800"
label_width = 16
window_title1 = "NEW DEVICE"
window_title2 = "UPDATE"
chng_w = 6
chng_h = 0
######## Paramter List ##########

####### Initialization ##########
root = Tk()
root.title(title)
root.geometry(WINDOW_SIZE)
tabControl = ttk.Notebook(root)

# Initializes the tabs
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Control Settings')
tabControl.add(tab2, text ='Test Configuration')
tabControl.add(tab3, text ='Control Network')
tabControl.add(tab4, text ='Test Network')
tabControl.add(tab5, text ='Run Test')
tabControl.add(tab6, text ='Graphs')
tabControl.pack(expand = 1, fill ="both")

# This is for testing purposes only for future code this is meant to be run
# with conjuction with testbed conrtoller class
list = ["Node1", "Node3"]
files = [('All Files', '*.*'),
         ('Python Files', '*.py'),
         ('Text Document', '*.txt'),
         ('XLS Document', '*.xls'),
         ('CSV Document', '*csv')]
headers = ["NAME", "IP","Node Type","Routing", "Ping(ms)", "Download(Mbit/s)", "Upload(Mbit/s)",
                                    "Iperf Transfer(MB)", "Iperf Bandwith", "Date", "Time"]


# Initialized Testbed Controller as a Global Variable.
g = TB_controller()
current_path  = "data1.csv"
current_file = None
####### Initialization ##########

### Label Loop that is global that can be reused #######
def label_loop_vert(tab ,values, row, column):
    m = row
    for i in range(len(values)):
        c = Label(tab, text = values[i], width = label_width, \
                                borderwidth=2, relief="groove",font="Times 12")
        c.grid(row= m, column= column, padx = 5, sticky=W)
        m += 1

def label_loop_horz(tab ,values, row, column):
    n = column
    for i in range(len(values)):
        c = Label(tab, text = values[i], width = label_width, \
                                borderwidth=2, relief="groove")
        c.grid(row= row, column= n, padx = 5, sticky=W)
        n += 1

def create_entry(tab, values, row, column, list):
    m = row
    for i in range (len(values)):
        e = tk.Entry(tab)
        e.insert(0,values[i])
        e.grid(row=m, column=column)
        list.append(e)
        m += 1

### Open Files
def open_file():
    file = askopenfile(mode ='r', filetypes =files)
    if file is not None:
        content = file.read()
        print(content)


### Save Files
def save():
    pass
def save_data(data_out):
    with open(current_path, 'w', newline = '') as csvfile:
    # writing the data rows with dictionary
        writer = csv.DictWriter(csvfile, fieldnames= g.control_ip)
        writer.writeheader()
        writer.writerow(data_out)

def update_save(new_row):
    if current_file is None:
        print("This file does not exist")
        return
    with open(current_file, 'w') as csvfile:
        csvwriter.writerow(new_row)
    csvfile.close()




################# Page Classes #################
class Page1:
    def __init__(self,tab, pg3, pg4):
        # Creates active device list
        self.tab = tab
        self.pg3 = pg3
        self.pg4 = pg4
        new_button = Button(self.tab, text="ADD NEW DEVICE", command=self.add,
            width = btn_width, bg = btn_bg, fg = "black",font="Times 9 bold")
        new_button.grid(row=0, column=0,sticky = W,padx = 1, columnspan = 2)

        a = Label(tab, text = "Active Devices", width = label_width,
                font="Times 12 underline",borderwidth=2, relief="groove")
        a.grid(row= 1, column= 0, sticky=W)
        self.ADrow = 2
        self.listnum = 0
        self.col = 2
        values = ["NAME", "CONTROL IP","TEST IP","Node Type", "SSID"]   # List of values
        # Initial list and active devices
        label_loop_vert(self.tab, values, 0, 1)

    def intake(self,e1,e2):
        a1 = e1.get()
        a2 = e2.get()
        # Error management
        list = g.add(a1,a2)
        label_loop_vert(self.tab, list, 0,self.col)
        num = len(g.Node_List)
        new_button = Button(self.tab, text=list[0], command=lambda:self.change(g.Node_List[num -1]),
            width = btn_width, bg = btn_bg, fg = "green",font="Times 9 bold")
        new_button.grid(row=self.ADrow, column=0,sticky = W,padx = 1, columnspan = 2)
        self.col += 1
        self.ADrow += 1
        self.pg3.update_graph()
        self.pg4.update_graph()

    def change(self, node):
        self.window = Toplevel(self.tab)
        self.window.geometry(pop_window)
        self.window.title(window_title1)
        tk.Label(self.window,
         text="Control IP").grid(row=0)
        tk.Label(self.window,
         text="Node Type").grid(row=1)

        e1 = tk.Entry(self.window)
        e1.insert(0,node.Control_IP)
        e1.grid(row=0, column=1)

        ### Drop Down Menu
        n = tk.StringVar()
        e2 = ttk.Combobox(self.window, width = label_width, textvariable = n)

        # Adding combobox drop down list
        e2['values'] = ('Station',
                                  'Access Point',
                                  'Relay')

        e2.grid(column = 1, row = 1)
        print(e2.current())
        a = 0
        if e2.current() == -1:
            a = 'Station'
        if e2.current() == 0:
            a = 'Access Point'
        if e2.current == 1:
            a = 'Relay'

        tk.Button(self.window,
                  text='Change',
                  command=lambda:self.update(a, node)).grid(row=4,
                                            column=0,
                                            sticky=tk.W + tk.E,
                                            pady=4)
        tk.Button(self.window,
                  text='Quit',
                  command=self.window.destroy).grid(row=4,
                                            column=1,
                                            sticky=tk.W + tk.E,
                                            pady=4)
    def update(self, e2, node):
        print(node.nodetype)
        print(e2)
        if (node.nodetype == 'Access Point'):
            node.AP_TO_STATION()
        if (node.nodetype == 'Station'):
            node.STATION_TO_AP()
        print(g.current_val(node))
        label_loop_vert(self.tab, g.current_val(node), 0,g.Node_List.index(node)+1)

    def add(self):
        ## Entry
        self.window = Toplevel(self.tab)
        self.window.geometry(pop_window)
        self.window.title(window_title1)
        tk.Label(self.window,
         text="Node Name").grid(row=0)
        tk.Label(self.window,
         text="Node Type").grid(row=1)

        e1 = tk.Entry(self.window)
        e1.insert(0,"10.1.1.")
        e1.grid(row=0, column=1)

        ### Drop Down Menu
        n = tk.StringVar()
        e2 = ttk.Combobox(self.window, width = label_width, textvariable = n)

        # Adding combobox drop down list
        e2['values'] = ('Station',
                                  'Access Point',
                                  'Relay')

        e2.grid(column = 1, row = 1)
        e2.current()

        tk.Button(self.window,
                  text='Add',
                  command=lambda:self.intake(e1,e2)).grid(row=4,
                                            column=0,
                                            sticky=tk.W + tk.E,
                                            pady=4)
        tk.Button(self.window,
                  text='Quit',
                  command=self.window.destroy).grid(row=4,
                                            column=1,
                                            sticky=tk.W + tk.E,
                                            pady=4)



class Page2:
    def __init__(self, tab):
        self.tab = tab
        ### First and Second Column ###
        # First
        values = ["Speedtest","Ping(ms)", "Iperf","Iperf Time(s)", \
                                "Iperf interval(s)","Type of Iperf","Number of trials"]

        self.entries_col_1 = []
        self.entries_col_2 = []
        self.checklist_col_1 = []
        self.var = []
        label_loop_vert(self.tab, values, 1, 0)

        # Second
        a = Label(self.tab, text = "Parameter List", width = label_width,
                font="Times 12 underline",borderwidth=2, relief="groove")
        a.grid(row= 0, column= 0, sticky=W)

        self.checklist_val = [1,1,1]
        self.create_checklist(self.tab, self.checklist_val, 1, 1, self.checklist_col_1 )
        # Entry list for clolumn 1
        create_entry(self.tab, g.test_prm, 4, 1, self.entries_col_1)

        # Third
        b = Label(tab, text = "Node List", width = label_width,
                font="Times 12 underline",borderwidth=2, relief="groove")
        b.grid(row= 0, column= 2, sticky=W)
        label_loop_vert(self.tab, list, 1, 2)

        self.checklist_val_1 = [1,1]
        self.create_checklist(self.tab, self.checklist_val_1, 1, 3, self.checklist_col_1 )

        # Fourth
        c = Label(tab, text = "Routing List", width = label_width,
                font="Times 12 underline",borderwidth=2, relief="groove")
        c.grid(row= 0, column= 4, sticky=W)
        label_loop_vert(self.tab, list, 1, 4)
        routing = ['Router','10.1.101.1']
        create_entry(self.tab, routing, 1, 5, self.entries_col_2)


        new_button = Button(self.tab, text="UPDATE VALUES", command=lambda:self.update_val(self.entries_col_1),
            width = btn_width, bg = btn_bg, fg = "Black",font="Times 9 bold")
        new_button.grid(row=0, column=6,sticky = W,padx = 1, columnspan = 2)

    ### Checklist
    def create_checklist(self,tab, values, row, column, list):
        m = row
        for i in range (len(values)):
            self.var.append(IntVar(value = values[i]))
            c = Checkbutton(tab, text = "", variable = self.var[len(self.var) -1], \
                    onvalue = 1, offvalue = 0).grid(row = m, column = column)
            list.append(c)
            m += 1

    def update_val(self, entry):
        i = 0
        for n in entry:
            g.test_prm[i] = n.get()
            i += 1
        print(g.test_prm)


class Page3:
    def __init__(self,tab):
        self.tab = tab
        self.output = 0
        self.mycanvas = Canvas(self.tab, width=1200, height=800)
        self.mycanvas.pack()
        self.frm_list = ["10.1.1.0"]
        self.to_list = ["10.1.1.1/Testbed Controller"]
    def update_graph(self):
        self.f = plt.figure(figsize=(10, 10))
        for a in g.Node_List:
            self.frm_list.append(a.Control_IP +"/" + a.nodetype)
            self.to_list.append(a.cntrl_routing)
        df = pd.DataFrame({ 'from':self.frm_list, 'to':self.to_list})
        # Build your graph
        plt.axis('off')
        H=nx.from_pandas_edgelist(df, 'from', 'to',create_using=nx.DiGraph())
        pos = nx.circular_layout(H)
        c =nx.draw(H, with_labels=True, node_size=400, node_color="skyblue",
            node_shape="o", alpha=0.5, linewidths=1, pos = pos, width = 1)
        # create matplotlib canvas using figure `f` and assign to widget `window`
        print(self.frm_list)
        print(self.to_list)
        self.output = FigureCanvasTkAgg(self.f, self.mycanvas)
        self.output.get_tk_widget().pack(fill='both')

class Page4:
    def __init__(self,tab):
        self.tab = tab
        self.frm_list_2 = ["10.1.101.3", "10.1.101.2"]
        self.to_list_2 = ["10.1.101.1","10.1.101.1"]
        self.mycanvas = Canvas(self.tab, width=1200, height=800)
        self.mycanvas.pack()

    def update_graph(self):
        self.f2 = plt.figure(figsize=(10, 10))
        for a in g.Node_List:
            self.frm_list_2.append(a.Test_IP)
            self.to_list_2.append(a.routing)
        df_2 = pd.DataFrame({ 'from':self.frm_list_2, 'to':self.to_list_2})
        # Build your graph
        plt.axis('off')
        K=nx.from_pandas_edgelist(df_2, 'from', 'to',create_using=nx.DiGraph())
        pos_2 = nx.circular_layout(K)
        d =nx.draw(K, with_labels=True, node_size=400, node_color="red",
            node_shape="o", alpha=0.5, linewidths=1, pos = pos_2, width = 1)
        print(self.frm_list_2)
        print(self.to_list_2)
        # create matplotlib canvas using figure `f` and assign to widget `window`
        self.output1 = FigureCanvasTkAgg(self.f2, self.mycanvas)
        self.output1.get_tk_widget().pack(fill='both')

class Page5:
    def __init__(self, tab):
        self.tab = tab
        new_button = Button(self.tab, text="RUN TEST", command=self.run_test,
            width = btn_width, bg = btn_bg, fg = "Black",font="Times 9 bold")
        new_button.grid(row=0, column=0,sticky = W,padx = 1, columnspan = 2)
        a = Label(tab, text = "RESULTS:", width = label_width,
                font="Times 12 underline",borderwidth=2, relief="groove")
        a.grid(row= 1, column= 0, sticky=W)

        exp_button = Button(self.tab, text="OPEN FILES", command=open_file,
            width = btn_width, bg = btn_bg, fg = "Black",font="Times 9 bold")
        exp_button.grid(row=0, column=1,sticky = W,padx = 1, columnspan = 2)
        a = Label(tab, text = "RESULTS:", width = label_width,
                font="Times 12 underline",borderwidth=2, relief="groove")
        exp_button_1 = Button(self.tab, text="SAVE FILES", command=save,
            width = btn_width, bg = btn_bg, fg = "Black",font="Times 9 bold")
        exp_button_1.grid(row=0, column=3,sticky = W,padx = 1, columnspan = 2)
        a = Label(tab, text = "RESULTS:", width = label_width,
                font="Times 12 underline",borderwidth=2, relief="groove")

    def run_test(self):
        # This is to run the test
        g.iperf_test(int(g.test_prm[3]))
        save_data(g.data)
        self.read_file()

    def read_file(self):
        num = []
        y = []
        x = []
        with open('data1.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            i = 0
            for row in plots:
                x = row[1]
                y = row[2]
        x = self.parser(x)
        x = self.str_to_flt(x)
        y = self.parser(y)
        y = self.str_to_flt(y)
        count = 0
        for i in range(g.test_prm[3]):
            count += 1
            num.append(count)
        print(x)
        print(y)
        print(num)
        pg6 = Page6(tab6,num,x,y)
    def parser(self,x):
        x = x[1:len(x) -1]
        x = re.split('\s|(?<!\d)[,.](?!\d)',x)
        while '' in x:
            x.remove('')
        return x
    def str_to_flt(self, x):
        new = []
        for i in x:
            new.append(float(i[1:len(i)-1]))
        return new



class Page6:
    def __init__(self,tab,num,x,y):
        list = []
        self.tab = tab
        fig = Figure(figsize = (6,8))
        a = fig.add_subplot(211)
        a.plot(num,x, label='Throughput Test')
        a.plot(num,y)
        a.set_xlabel('Trials')
        a.set_ylabel('Throughput(Mbit/sec)')
        a.set_title('Trial vs Throughput')
        for c in g.STN_LIST:
            list.append(c.hostname)
        a.legend(list, loc ="lower right")
        a1= FigureCanvasTkAgg(fig, self.tab)
        a1.get_tk_widget().pack(fill='both')


## This is where the classes are initialized to create the tabs
pg2 = Page2(tab2)
pg3 = Page3(tab3)
pg4 = Page4(tab4)
pg1 = Page1(tab1, pg3, pg4)
pg5 = Page5(tab5)

root.mainloop()

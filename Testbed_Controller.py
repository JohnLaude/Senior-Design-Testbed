# AUTHOR: John Carlo Laude
# Date: 10/21/2020
# Title: Testbed Controller for Relay Testbed 

from Relay_AP import *
from User_Device import *
from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH


# Configure File
silver = '#C0C0C0'
bg_color = 'LightSteelBlue2'
title = "Testbed GUI"
btn_bg = 'lavender'
btn_width = 24
pop_window = "200x200"
label_width = 10
window_title1 = "NEW DEVICE"
window_title2 = "UPDATE"
chng_w = 6
chng_h = 0

class Testbed_Controller:
    def __init__(self):
        # Testbed controller/Back end coding 
        pass
    def ssh(self):
        pass

class GUI:
        # GUI/Front end coding 
    def __init__(self, master):
        self.master = master
        master.title(title)
        master['background'] = bg_color
        # Button Initialization
        self.new_button = Button(master, text="ADD NEW DEVICE", command=self.create_window, width = btn_width, bg = btn_bg)
        self.update_button = Button(master, text="UPDATE", command=self.update, width = btn_width, bg = btn_bg)
        self.collect_button = Button(master, text="COLLECT", command=self.print_node, width = btn_width, bg = btn_bg)
        self.reset_button = Button(master, text="RESET", command=self.reset, width = btn_width, bg = btn_bg)


        #Label Values
        self.AP_label = ["AP NUM", "IP","Routing", "TX RATE", "TX POW", "POW RX", "OUT PORT", "ON/OFF"]
        self.DV_label = ["DEVICE NUM", "IP","RSS", "Routing", "BIT RATE", "ON/OFF"]
        self.VALUES = [None] # Temporary
        self.e = [None]
        # Increments the rows. n is the variable for each new row. j is the location of each new NODES element 
        self.n = 3
        self.NODES = [None] # Data Base for all my classes
        self.j = 0


        # Initiates the the starting window
        # Buttons
        self.new_button.grid(row=1, column=0,sticky = W,padx = 1, columnspan = 2)
        self.update_button.grid(row=1, column=2,sticky=W, padx = 1,columnspan = 2)
        self.collect_button.grid(row=1, column=4, sticky=E,padx = 1, columnspan = 2)
        self.reset_button.grid(row=1, column=6, sticky=E, padx = 1,columnspan = 2)

        # Labels
        self.label_loop(self.AP_label, 2, 0)
        self.label_loop(self.VALUES, 3, 0) # Empty lines
        self.label_loop(self.DV_label,4 , 0)
        self.label_loop(self.VALUES, 5, 0) # Empty lines

    # Creates a loop for labels
    def label_loop(self, values, row, column):
        m = column
        for i in range(len(values)):
            c = Label(self.master, text = values[i], background = bg_color, width = label_width)
            c.grid(row= row, column= m, padx = 5, sticky=W)
            m += 1
        if (values[0] !="AP NUM") and (values[0] !="DEVICE NUM") and (values[0] != None):
            self.chng = Button(self.master, text="Change", command=lambda: self.change(self.j, row),
                               width = chng_w, height =chng_h, bg = btn_bg)
            self.chng.grid(row= row, column=m, padx = 1,columnspan = 1, sticky=W)
            self.j += 1
    
    # Creat a loop for parameters entry 
    def prm_loop(self, window, label):
        x = len(label)
        self.e = [None]*x
        self.VALUES = [None]*x
        for i in range(len(label)):
            c = Label(window,text = label[i], background = bg_color)
            c.grid(row= i, column= 0, sticky=W)
            self.e[i] = Entry(window)
            self.e[i].grid(row = i, column = 1)

    # Update the values
    def update(self, node, row):
        for i in range(len(self.e)):
            self.VALUES[i] = self.e[i].get()
        self.label_loop(self.VALUES, row, 0)
        # Need to create code that changes 
        # the values of what's inside the NODES list 
        y = self.VALUES[0]
        self.VALUES.remove(y)
        if row < 4:
            self.NODES[node].update(self.VALUES[0],self.VALUES[1],self.VALUES[2],self.VALUES[3],self.VALUES[4]
                                    ,self.VALUES[5],self.VALUES[6])
        else:
            self.NODES[node].update(self.VALUES[0], self.VALUES[1], self.VALUES[2], self.VALUES[3], self.VALUES[4])
        # Closes the window
        self.window.destroy()

    # Initialize AP and Devices
    def new(self):
        for i in range(len(self.e)):
            self.VALUES[i] = self.e[i].get()
        self.label_loop(self.VALUES, self.n, 0)
        y = self.VALUES[0]
        self.VALUES.remove(y)
        if self.n < 4:
            a = Relay_AP(self.VALUES[0],self.VALUES[1],self.VALUES[2],self.VALUES[3],self.VALUES[4],self.VALUES[5],self.VALUES[6])
        else:
            a = User_Device(self.VALUES[0], self.VALUES[1], self.VALUES[2], self.VALUES[3], self.VALUES[4])
        self.NODES.append(a)
        self.n += 1
        if self.n == 4:
            self.n += 1
        # Closes the window
        self.window.destroy()

    # Opens/Creates the change window 
    def change(self, node, row):
        self.window = Toplevel(self.master)
        self.window['background'] = bg_color
        self.window.geometry(pop_window)
        self.window.title(window_title2)
        if row < 4:
            self.prm_loop(self.window, self.AP_label)
        else:
            self.prm_loop(self.window, self.DV_label)
        self.enter_button = Button(self.window, text="UPDATE", command=lambda: self.update(node,row),width = 8, bg = btn_bg)
        self.enter_button.grid(row=8, column=0, sticky=W, padx = 1,columnspan = 1)
        self.resets_button = Button(self.window, text="RESET", command=self.update, width = 8, bg = btn_bg)
        self.resets_button.grid(row=8, column=1, sticky=W, padx = 1,columnspan = 1)

    # Creates a windows that can input values and create new classes
    def create_window(self):
        self.window = Toplevel(self.master)
        self.window['background'] = bg_color
        self.window.geometry(pop_window)
        self.window.title(window_title1)
        if self.n < 4:
            self.prm_loop(self.window, self.AP_label)
        else:
            self.prm_loop(self.window, self.DV_label)
        self.enter_button = Button(self.window, text="ENTER", command=lambda: self.new(),width = 8, bg = btn_bg)
        self.enter_button.grid(row=8, column=0, sticky=W, padx = 1,columnspan = 1)
        self.resets_button = Button(self.window, text="RESET", command=self.update, width = 8, bg = btn_bg)
        self.resets_button.grid(row=8, column=1, sticky=W+E, padx = 1,columnspan = 1)

    # Connected to the collect button. Helps check the values in NODES list
    def print_node(self):
        for b in self.NODES:
            if b != None:
                members = [attr for attr in dir(b) if not callable(getattr(b, attr)) and not attr.startswith("__")]
                for text in members:
                    print(text+ ": " + str(getattr(b,text)))
                print("\n")

    def reset(self):
        self.VALUES = [None]*9
        i = 0
        while i <= self.n:
            if (i > 2) and (i != 4):
                self.label_loop(self.VALUES, i, 0)
            i += 1
        self.NODES.clear()
        self.chng.destroy()
        self.n = 3
        self.j = 0

# Running the GUI 
root = Tk()
my_gui = GUI(root)
root.geometry("780x300")
#GUI.NODES[2].IP
root.mainloop()
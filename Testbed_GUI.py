# AUTHOR: John Carlo Laude, Myles Toole, Haining Gao
# Date: 12/31/2020
# Title: Testbed Controller for Relay Testbed

from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH
from TB_controller import TB_controller

################ Parameter List ################
# Configure File
silver = '#C0C0C0'
bg_color = 'gray11'
title = "Testbed GUI"
btn_bg = 'lavender'
font_color = "white"
font = "Times"
btn_width = 28
pop_window = "200x200"
WINDOW_SIZE = "1600x300"
label_width = 14
window_title1 = "NEW DEVICE"
window_title2 = "UPDATE"
chng_w = 6
chng_h = 0

# TB Controller
num_node = 2
################ Parameter List ################
class GUI:
        # GUI/Front end coding
    def __init__(self, master, tb_control):
        self.master = master
        self.tbc = tb_control
        master.title(title)
        master['background'] = bg_color
        # Button Initialization
        self.new_button = Button(master, text="NEW DEVICE", command=self.add, width = btn_width, bg = btn_bg)
        self.test_config = Button(master, text="TEST CONFIG", command=self.create_window, width = btn_width, bg = btn_bg)
        self.run_test = Button(master, text="RUN TEST", command=self.update, width = btn_width, bg = btn_bg)
        self.reset_btn = Button(master, text="RESET ALL", command=self.create_window, width = btn_width, bg = btn_bg)
        self.motion_settings = Button(master, text="MOTION SETTINGS", command=self.create_window, width = btn_width, bg = btn_bg)
        self.graph_inter = Button(master, text="SHOW GRAPH", command=self.create_window, width = btn_width, bg = btn_bg)
        self.label = ["NAME", "IP","Routing", "Ping(ms)", "Download(Mbit/s)", "Upload(Mbit/s)", "Date", "Time"]
        self.label2 = ["NAME", "Type of Node"]
        self.values = []
        self.n = 0
        self.e = [None]
        # Button locations
        self.new_button.grid(row=1, column=0,sticky = W,padx = 1, columnspan = 2)
        self.test_config.grid(row=1, column=2,sticky=W, padx = 1,columnspan = 2)
        self.run_test.grid(row=1, column=4, sticky=E,padx = 1, columnspan = 2)
        self.reset_btn.grid(row=1, column=6, sticky=E, padx = 1,columnspan = 2)
        self.motion_settings.grid(row=1, column=8, sticky=E,padx = 1, columnspan = 2)
        self.graph_inter.grid(row=1, column=10, sticky=E, padx = 1,columnspan = 2)


        self.label_loop(self.label, 2, 0)


    # Creates a loop for labels
    def label_loop(self, values, row, column):
        m = column
        for i in range(len(values)):
            c = Label(self.master, text = values[i], fg = "white", font = font_color, background = bg_color, width = label_width)
            c.grid(row= row, column= m, padx = 5, sticky=W)
            m += 2


    def prm_loop(self, window, label):
        x = len(label)
        self.e = [None]*x
        self.values = [None]*x
        for i in range(len(label)):
            c = Label(window,text = label[i], background = bg_color, font = font_color, fg = "white" )
            c.grid(row= i, column= 0, sticky=W)
            self.e[i] = Entry(window)
            self.e[i].grid(row = i, column = 1)

    def create_window(self):
        self.window = Toplevel(self.master)
        self.window['background'] = bg_color
        self.window.geometry(pop_window)
        self.window.title(window_title1)
        self.prm_loop(self.window, self.label2)
        self.enter_button = Button(self.window, text="ENTER", command=lambda: self.add,width = 8, bg = btn_bg)
        self.enter_button.grid(row=8, column=0, sticky=W, padx = 1,columnspan = 1)
        self.resets_button = Button(self.window, text="RESET", command=self.update, width = 8, bg = btn_bg)
        self.resets_button.grid(row=8, column=1, sticky=W+E, padx = 1,columnspan = 1)

    def update(self):
        self.tbc.run_test()
        for n in self.tbc.Node_List:
            gui.values.append(self.tbc.store())
        n = 3
        for val in gui.values:
            self.label_loop(val, n, 0)
            n += 1
        self.tbc.passing()

    def add(self):
        g.add("Node1",2)
        g.add("Node2",1)
        #g.add(self.e[0].get(), self.e[1].get())

# Main loop that starts the GUI 
g = TB_controller()
#while len(g.Node_List) < num_node:
    #g.add()
g.print()
root = Tk()
gui = GUI(root, g)
root.geometry(WINDOW_SIZE)
root.mainloop()

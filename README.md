# Senior-Design-Testbed
Repository for Senior Design Project for Fall 2020

Hello, if you are reading this then you are downloading Senior Design Testbed made by UMass Boston student to help people with VLC and OWC research. 

This testbed code is under the assumption of a few different things: 
  - SSH is enabled in the raspberry pi
  - RaspAP has been downloaded on nodes that we will act as Relays and Access Points
  - Passwordless authorization for raspberry pis for testbed controller device
  - Speedtest client 
  
--------------------------------------------------------------------------------------------------------- 
**Headless SSH:** 

After downloading and imaging the rasoian OS file into your micro-SD card, you can go into the boot file 
and save an SSH file into it. Make sure there is nothing on the file extension when this is saved. To 
check the file extension, go to view and check the fil extension checkbox. 

You can find the raspberrypi IP by inputing this into the command line. 
```
ping raspberrypi.local
```
For more information, pleas head to the raspberry pi website to learn more:
https://www.raspberrypi.org/documentation/configuration/wireless/headless.md

--------------------------------------------------------------------------------------------------------- 
**Access Point:** 

You can configure an Access Point by following this link: 
https://www.raspberrypi.org/documentation/configuration/wireless/access-point-routed.md 

--------------------------------------------------------------------------------------------------------- 
**Speedtest Download**

You can download the speedtest client using the command below
```
sudo apt install speedtest-cli
```
---------------------------------------------------------------------------------------------------------
**Passwordless SSH** 

You can follow the steps to make your raspberry pi passwordless from the link below: 
https://endjin.com/blog/2019/09/passwordless-ssh-from-windows-10-to-raspberry-pi

---------------------------------------------------------------------------------------------------------
**Using pwr_swp1.py**

Make sure that you are in the correct directory first before you run the file. The file would be a python file and is meant to test out all the raspberry pi at once and make sure they are connected. 

__Windows__
The windows command is as follows
```
py pwr_swp1.py 
```
__Linux__
The linux command is as follows
```
python pwr_swp1.py
```

Open file a change list of parameters
```
# Parameters
Nodes = ["10.1.1.2"]
flag = [0]*5
iperf_prm  = [10, 10]
Static_IP = []
Wifi_IP = []
Wifi_IP.append("10.1.101.1")
results = []
results2 = []
filename = "data1.csv"
trials = 20
power_sweep = 31
min_power = 31
interval = 2
```
You will then need to go to line 74 to change which iperf test you want to do. You change this to iperf_r or iperf_d accordingly
```
        iperf(iperf_prm[0], iperf_prm[1], a)
```
This will save into a csv file automatically. Waning: Please do not leave csv file open or it will not be able to 

---------------------------------------------------------------------------------------------------------
**Testbed GUI**

This will be the command that you need to run to use the testbed: 

__Windows__

This is the command on windows
```
py GUI.py
```

To run the initial test to create test the network press "Add New Device" to add new device into the control network. A new window will pop up that will prompt for IP addess and nodetype. You can navigate through the tabs to see how the testbed system looks like. 

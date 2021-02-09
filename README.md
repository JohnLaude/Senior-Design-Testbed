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
**RaspAP Download:** 

Install RaspAP from your device’s shell prompt using the command below:
```
curl -sL https://install.raspap.com | bash
```
For more information, pleas head to this website to learn more about RaspAP:
https://raspap.com/

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
**Using Test_All.py**

Make sure that you are in the correct directory first before you run the file. The file would be a python file and is meant to test out all the raspberry pi at once and make sure they are connected. 

__Windows__
The windows command is as follows
```
py Test_All.py 
```
__Linux__
The linux command is as follows
```
python Test_All.py
```

You will be given a few prompts to add the nodes to the testscript
```
Please input nodes here
Input number of nodes: 
Input node name: 
```
This will be the other prompts given after all the nodes have been added
```
Ping devices? (Y/N)
Get hostname? (Y/N) 
Get IP? (Y/N)
Get routing? (Y/N)
run speedtest (Y/N) 
```

---------------------------------------------------------------------------------------------------------
**Testbed GUI**

This will be the command that you need to run to use the testbed: 

__Windows__

This is the command on windows
```
py Testbed_GUI.py
```

To run the initial test to create test the network press "New Device" followed by "Run Test"

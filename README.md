# Senior-Design-Testbed
Repository for Senior Design Project for Fall 2020

Hello, if you are reading this then you are downloading Senior Design Testbed made by UMass Boston student to help people with VLC and OWC research. 

This testbed code is under the assumption of a few different things: 
  - RaspAP has been downloaded on nodes that we will act as Relays and Access Points
  - Passwordless authorization for raspberry pis for testbed controller device
  - Speedtest client 
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
**Using SSH.py**

Make sure that you are in the correct directory first before you run the file. The file would be a python file and is meant to test out all the raspberry pi at once and make sure they are connected. 

__Windows__

The windows command is as follows
```
py SSH.py 
```
You will be given a few prompts to add the nodes to the testscript
```
Please input nodes here
Input number of nodes: 
Input node name: 
```
This will be the other prompts given after all the nodes have been added
```
Get hostname? (Y/N) 
Run Iperf (Y/N) 
run speedtest (Y/N) 
```

---------------------------------------------------------------------------------------------------------
**Testbed GUI**

This will be the command that you need to run to use the testbed: 

__ Windows__

This is the command on windows
```
py Testbed_GUI.py
```

To run the initial test to create test the network press "New Device" followed by "Run Test"

# This checks all the pis in the system
import subprocess
import itertools
import csv
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
# Functions
def iperf(i, t, nums):
    for n in Nodes:
        args = "ssh pi@"+ str(n)+" iperf -c " + str(Wifi_IP[0]+ " -p 12000")
        s = subprocess.check_output(args)
        out = str(s.decode('utf-8'))
        out = out.split(" ")
        num = len(out)
        data1 = [nums] + out[num -5:]
        results.append(data1)

def iperf_r(i, t, nums):
    for n in Nodes:
        args = "ssh pi@"+ str(n)+" iperf -c " + str(Wifi_IP[0] + " -p 12000 -r")
        s = subprocess.check_output(args)
        out = str(s.decode('utf-8'))
        out = out.split(" ")
        num = len(out)
        data1 = [nums] + out[num -27:num -22]
        data2 = [nums] + out[num-5:]
        results.append(data1)
        results2.append(data2)
def iperf_d(i,t,nums):
    for n in Nodes:
        args = "ssh pi@"+ str(n)+" iperf -c " + str(Wifi_IP[0] + " -p 12000 -d")
        s = subprocess.check_output(args)
        out = str(s.decode('utf-8'))
        out = out.split(" ")
        num = len(out)
        data2 = [nums] + out[num -16:num -10]
        data1 = [nums] + out[num-5:]
        results.append(data1)
        results2.append(data2)

def tx_power(num):
    args = "ssh pi@" +Nodes[0]+ " sudo iwconfig wlan0 txpower " + str(num)
    subprocess.call(args, shell=True)

def save_data(data_out, data_out2):
    with open(filename, 'w', newline = '') as csvfile:
    # creating a csv writer object
        csvwriter = csv.writer(csvfile)
    # writing the data rows
        csvwriter.writerows(data_out)
        csvwriter.writerows(data_out2)
# Main
tx_power(power_sweep)
count = 1
print("Trials have started")
while(1):
    print("Currently on test " + str(count))
    results.append(["TX"+ str(power_sweep),"UPLINK","","",""])
    results2.append(["TX"+ str(power_sweep),"DOWNLINK","","",""])
    for j in range(trials):
        a = str(power_sweep)
        iperf(iperf_prm[0], iperf_prm[1], a)
        print("Currently on throughput test " + str(j + 1))
    power_sweep -= interval
    tx_power(power_sweep)
    count += 1
    if power_sweep <= min_power:
        break
save_data(results, results2)
print(str(trials))
print("Trials are done")

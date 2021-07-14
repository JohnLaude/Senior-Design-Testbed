#!/bin/bash
# Variables
ip_server="10.1.1.2"
iperf_serv=$1
shift
base_port=5000
ip_prefix="10.1.1"
# List of available IP
num=($(seq 2 $1))
shift
# Type of iperf
type=$1
shift
# number of sequences
trial=$1
shift
# Duration
dur=$1
shift
# Scenario
scenario=$1
shift
# Filename
Filename=$1
shift
# Iperf test for loop with number of tets and types
ssh pi@$ip_server screen -d -m iperf -s
counter=0
until [ $counter -ge $trial ]
do
	((counter++))
	echo "This is trial " $counter
	for i in "${num[@]}"; do
		server_port=$(($base_port+$i));
		ssh pi@"$ip_prefix.$i" iperf $type $iperf_serv -t $dur | awk 'END{print '$ip_prefix.$i'","$5","$7}'>> $scenario/$Filename.csv &
	done
	sleep 15
done
echo "Test is finished"

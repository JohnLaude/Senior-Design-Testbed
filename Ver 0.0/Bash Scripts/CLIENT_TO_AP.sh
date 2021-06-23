#!/bin/bash

sudo systemctl restart dnsmasq.service
sudo systemctl restart hostapd.service
sudo sed -i '/nohook wpa_supplicant/s/^#//g' /etc/dhcpcd.conf
sudo rfkill unblock wlan
sudo reboot

#1/bin/bash

sudo systemctl stop hostapd.service
sudo systemctl stop dnsmasq.service
sudo sed -e '/nohook wpa_supplicant/ s/^#/#/g' -i /etc/dhcpcd.conf
sudo rfkill unblock wlan
sudo reboot

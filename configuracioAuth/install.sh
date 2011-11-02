#!/bin/sh
sudo cp -R  ./etc /etc
sudo cp -R ./usr /usr
sudo cp -R ./var /var
sudo -u gdm gconftool-2 --set --type boolean /apps/gdm/simple-greeter/disable_user_list true
sudo ln -s /usr/share/local/telestany/enviaapaga /etc/rc0.d/K09_enviaapaga


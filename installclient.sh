#!/bin/sh
sudo apt-get install screenlets
sudo apt-get install privoxy
sudo apt-get install gxmessage
sudo apt-get install python-soappy
sudo mkdir /etc/telestany
sudo cp -R ./telecentreuser /etc/telestany/telecentreuser
sudo chmod 775 /etc/telestany/telecentreuser
sudo adduser telecentreuser
sudo chown -R telecentreuser:users /etc/telestany/telecentreuser
sudo cp privoxy/shalla_update.no_funciona.sh /etc/telestany/shalla.sh
sudo sh /etc/telestany/shalla.sh &
sudo cp -Rf  ./configuracioAuth/etc /
sudo cp -Rf ./configuracioAuth/usr /
sudo cp -Rf ./configuracioAuth/var /
sudo chmod +x /etc/gdm/Init/Default
sudo chmod +x /etc/gdm/PostSession/Default
sudo chmod +x /etc/gdm/PostLogin/Default
sudo chmod +x /etc/gdm/PreSession/Default
sudo chmod +x /usr/share/local/telestany/*
sudo -u gdm gconftool-2 --set --type boolean /apps/gdm/simple-greeter/disable_user_list true
sudo ln -s /usr/share/local/telestany/enviaapaga /etc/rc0.d/K09_enviaapaga
sudo ln -s /usr/share/local/telestany/updateScreenlet.sh /etc/rc2.d/S20_updateScreenlet
sudo update-rc.d TelestanyRespostes defaults
sudo /usr/bin/python /usr/share/local/telestany/users.py
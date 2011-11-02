#!/bin/sh
/usr/bin/wget http://update:update@telestany.plaestany.cat/updates/ControlTempsScreenlet.py
mv ControlTempsScreenlet.py /etc/telestany/telecentreuser/.screenlets/ControlTemps/
chown telecentreuser.users /etc/telestany/telecentreuser/.screenlets/ControlTemps/ControlTempsScreenlet.py
rm /usr/share/local/telestany/updateScreenlet.sh
/usr/bin/wget http://update:update@telestany.plaestany.cat/updates/updateScreenlet.sh
mv updateScreenlet.sh /usr/share/local/telestany
sudo chmod +x /usr/share/local/telestany/updateScreenlet.sh
chown root.root /usr/share/local/telestany/updateScreenlet.sh
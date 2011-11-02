#!/bin/sh
cp -R etc/ /
cp -R usr/ /
chmod +x /usr/share/local/telestany/TelestanyWeb
chown root:root /etc/init.d/TelestanyWebService
chmod 755 /etc/init.d/TelestanyWebService
update-rc.d TelestanyWebService defaults
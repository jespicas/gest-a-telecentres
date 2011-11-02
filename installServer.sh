#!/bin/sh
cp -R ./webService/etc/ /
cp -R ./webService/usr/ /
chmod +x /usr/sbin/TelestanyWeb
chmod +x /usr/share/local/telestany/TelestanyWeb
chown root:root /etc/init.d/TelestanyWebService
chmod 755 /etc/init.d/TelestanyWebService
update-rc.d TelestanyWebService defaults
cp -R ./Web /var/www/telestany.plaestany.cat/httpdocs
chown telestany.www-data -R /var/www/telestany.plaestany.cat/httpdocs


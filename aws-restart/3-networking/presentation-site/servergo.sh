#!/bin/sh

# Install Apache web server from repository
yum install httpd -y

# Start httpd service with systemd
systemctl enable httpd
systemctl start httpd

# Pull down important files from the internet
wget -q https://perscholas.org/wp-content/uploads/2020/07/38AFB89C-1314-4BAC-9BEE-8002DEB2076B-Roberto-Santos-905x1000.jpeg &&
mv 38AFB89C-1314-4BAC-9BEE-8002DEB2076B-Roberto-Santos-905x1000.jpeg /var/www/html/image.jpg
wget -qP /var/www/html/ https://raw.githubusercontent.com/narodn1k/learning/main/aws-restart/3-networking/presentation-site/index.html
wget -qP /var/www/html/ https://raw.githubusercontent.com/narodn1k/learning/main/aws-restart/3-networking/presentation-site/index.css

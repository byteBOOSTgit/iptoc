# iptoc
This project is a simple tool to convert IP address to country code. It uses Maxmind GeoIP databases.  This tool was created to demonstrate leveraging Apple Shortcuts to execute a Python script with arguments retrieved from the GUI.  In addition, the Apple Shortcuts below take the output of the Script and launch an Apple application using the output from the Python script as input arguments to the application launched (Apple Maps in this case).  Screenshots of the Apple Shortcuts are below.
## Installation

### Install Maxmind GeoIP Databases
https://dev.maxmind.com/geoip/geolite2-free-geolocation-data

### Create "Quick Action" Apple Shortcut

![iptomap-quick.png](doc%2Fiptomap-quick.png)

### Select IP
Using your cursor, highlight an IP address in any application and right-mouse click.  Select the "Services > IP to Map" context menu selections.  The Apple Shortcut will execute, send the IP address as a parameter to the python script to return Lat/Lon coordinates.  That output will be sent to the Apple Maps application.

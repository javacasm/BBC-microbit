Close Chrome
Create a file at
/etc/udev/rules.d/50-microbit.rules
 with the following content:
SUBSYSTEM=="usb", ATTR{idVendor}=="0d28", MODE="0664", GROUP="plugdev"
Add your user to the plugdev group (replace with your username): 
sudo adduser your_username plugdev 
Restart the udev rules 
sudo udevadm control --reload-rules 
Open Chrome and try to pair again 

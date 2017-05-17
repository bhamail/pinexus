OS Setup
========
  
  Once you have an SD Card with the Raspian OS Image, you can setup the operating system as follows:
  
  1. Insert the card into your RaspberryPI.
  2. Connect the following items:
    *  video (HDMI)	
    *  network
    *  USB keyboard (optional)
    *  USBmouse (optional)
    *  USB power cable
  3. Note: Current versions of Raspian default to booting into a graphical desktop UI. You 
    should probably change this to boot to the command line (CLI) instead, as this will leave
    more memory available to Nexus. You may also have to enable `ssh` in newer Raspian images, 
    as it is disabled by default.
   
    You can use  [raspi-config](https://www.raspberrypi.org/documentation/configuration/raspi-config.md) to set configuration options such as:
     
    a. Expand Filesystem - Resize partition to fill SD Card.  
    b. Internationalisation Options - Change the settings for Locale, Timezone, and Keyboard:

       * *i18n, locale* to `en_US.UTF-8`,
       * *Timezone* to your local timezone
       * *Keyboard* to: `Generic 104-key PC`.				
  
  4. Reboot to allow changes to take effect.
  5. If you are connected to a network, the Pi console displays the ip
    address of the machine. **Make a note of this address** so you can perform the
    following steps via `ssh` if you like. The default userId is `pi`, and password is `raspberry`.
    
        my-pc$ ssh pi@the-Pi-IP-address
    
    Update to latest OS packages:
  
        pi@raspberrypi:~ $ sudo apt-get update && sudo apt-get upgrade

    Update to latest firmware:
    
        pi@raspberrypi:~ $ sudo rpi-update


Next step: [Nexus Setup](nexussetup.html)

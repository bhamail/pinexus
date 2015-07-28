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
  3. Your Pi should boot up and display the [raspi-config](https://www.raspberrypi.org/documentation/configuration/raspi-config.md) screen (at first boot).
   At this point, you can use  [raspi-config](https://www.raspberrypi.org/documentation/configuration/raspi-config.md) to set configuration options such as:
     
     a. Expand Filesystem - Resize partition to fill SD Card.  
     b. Internationalisation Options - Change the settings for Locale, Timezone, and Keyboard:

       * *i18n, locale* to `en_US.UTF-8`,
       * *Timezone* to your local timezone
       * *Keyboard* to: `Generic 104-key PC`.				
  
  4. Reboot to allow partition resize to occur.
  5. If you are connected to a network, the Pi console displays the ip
    address of the machine. Make a note of this address so you can perform the
    following steps via `ssh` if you like. The default userId is `pi`, and password is `raspberry`.
    
        my-pc$ ssh pi@the-Pi-IP-address
    
    Update to latest OS packages:
  
        pi@raspberrypi ~ $ sudo apt-get update && sudo apt-get upgrade

    Update to latest firmware:
    
        pi@raspberrypi ~ $ sudo rpi-update


  Pre-requisites:
  
   1. Verify java version is at least:
   
        pi@raspberrypi ~ $ java -version
        java version "1.8.0"
        Java(TM) SE Runtime Environment (build 1.8.0-b132)
        Java HotSpot(TM) Client VM (build 25.0-b70, mixed mode)

Next step: [Nexus Setup](nexussetup.html)

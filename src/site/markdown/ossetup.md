OS Setup
========

  Steps after first boot (in [raspi-config](https://www.raspberrypi.org/documentation/configuration/raspi-config.md)).
  
  Once you have your SDCard with the Raspian OS Image, insert the card into your RaspberryPI. Then connect your HDMI, network, 
  (and optionally USB Keyboard and Mouse), and finally USB power cable. Your Pi should boot up. The original Raspian image brings
  you to the [raspi-config](https://www.raspberrypi.org/documentation/configuration/raspi-config.md) screen at first 
  boot. Here are the actions I performed at this point:
  
   1. Expand Filesystem - Resize partition to fill sdcard.
   2. Internationalisation Options - Change *i18n, locale* to `en_US.UTF-8`, default to that too. 
     Also change *Timezone*. *Keyboard* to: `Generic 104-key PC`.
    
     Reboot to allow partition resize to occur.
 
  If you are connected to a network, the Pi console will display the ip address of the machine. Make a note of this 
  address so you can perform the following steps via `ssh` if you like. 
  The default userId is `pi`, and password is `raspberry`.
  
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

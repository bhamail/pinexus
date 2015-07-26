Setup
=====

SD Card Setup
-------------

  1. Install RaspianOS on a SDCard. See: https://www.raspberrypi.org/documentation/installation/installing-images/

    You could also review the python program in [pysdcard](https://github.com/bhamail/pinexus/tree/master/pysdcard) for ways to create 
    bootable SDCard images.
    
   
OS Setup
--------

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
  
      my-pc$ ssh pi@<the Pi IP address>
   
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

Nexus Setup
-----------

  Download the Nexus bundle from (@todo add link).

  Copy the nexus bundle to the pi, in new “nexus” folder: /home/pi/nexus

      pi@raspberrypi ~ $ pwd
      /home/pi
      pi@raspberrypi ~ $ mkdir nexus
      
  then: 
  
      my-pc$ scp ~/sonatype/dev/pi/nx3-alpa-bundle/nexus-3.0.0-SNAPSHOT-bundle.tar.gz pi@<the Pi IP address>:/home/pi/nexus/
      
  unzip/untar:
  
      pi@raspberrypi ~ $ cd nexus
      pi@raspberrypi ~/nexus $ tar -zxvf nexus-3.0.0-SNAPSHOT-bundle.tar.gz

  Start nexus. Move into the nexus bin dir and run:
    
      pi@raspberrypi ~/nexus/nexus-3.0.0-SNAPSHOT/bin $ ./start
  
  While Nexus is starting, you can watch the Pi system load using `top`. Wait for the `java` process to ease up on 
  the cpu (well below 100% CPU in `top`).  Then from your PC, open the link below to Nexus running on the Pi:
  
      http://<the Pi IP address>:8081

   The default Nexus administrator credentials are user: `admin`, password: `admin123`. 
   Huzzah! Nexus is running on your Pi.  
   
Nexus deamon setup
------------------
   
   To enable Nexus to launch automatically at system boot time, make the following changes:
   
   1. Create a new init.d script in order to install Nexus as a system service: 
   
        pi@raspberrypi ~ $ cd /etc/init.d/
        pi@raspberrypi /etc/init.d $ sudo vi nexus
        
      Paste the following content into this new file, and save the file:
   
        #!/bin/sh
        ### BEGIN INIT INFO
        # Provides:          nexus
        # Required-Start:    $remote_fs $syslog
        # Required-Stop:     $remote_fs $syslog
        # Default-Start:     2 3 4 5
        # Default-Stop:      0 1 6
        # Short-Description: Start nexus daemon at boot time
        # Description:       Enable nexus as a system service provided by daemon.
        ### END INIT INFO
      
        NEXUS_HOME="/home/pi/nexus/nexus-3.0.0-SNAPSHOT"
        NEXUS_USER="pi"
        
        exec sudo -u "$NEXUS_USER" -- "$NEXUS_HOME/bin/nexus" "$@"
        
      Here's a file with the same content you could just copy into `/etc/init.d/`: [nexus](scripts/nexus)
        
   3. Add execute permission to the new init.d script:

        pi@raspberrypi /etc/init.d $ sudo chmod +x nexus        

   4. Setup init scripts using `update-rc.d`:
   
        pi@raspberrypi /etc/init.d $ sudo update-rc.d nexus defaults
        
   5. Test the function of the init scripts:
   
        pi@raspberrypi ~ $ service nexus start
        
      or, just reboot the Pi and see if nexus is running after reboot:
      
        pi@raspberrypi ~ $ service nexus status
        ...
        Running ...
        
   ----------------
   
Next step: [Doc docs](docdocs.html)
   
 ----------------
 
 Old Steps for JSW - for NX2 (no longer required)
 
 ---------------------------
   
   To compile ARM compatible JSW service binary for ARM:
    
   see:
    http://honnix.com/technology/raspberry%20pi/java/2013/07/14/sonatype-nexus-on-raspberry-pi/

   and:
    http://ti57.blogspot.se/2013/05/apache-archiva-on-raspberry-pi.html

   Build notes: Worked with wrapper_3.5.25_src.
   
   - use jsw `build32.sh` script
   
   Edits to: nexus/nexus-3.0.0-SNAPSHOT/etc/nexus3-wrapper.conf 
   
   ------------------------------------------------------------
   
   Fix/avoid error: `fatal error: jni.h: No such file or directory` by setting java home: 
   
      $ export JAVA_HOME=/usr/lib/jvm/jdk-8-oracle-arm-vfp-hflt
   
   

   
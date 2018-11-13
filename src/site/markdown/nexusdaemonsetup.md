Nexus Deamon Setup
==================
   
   To enable Nexus to launch automatically at system boot time, make the following changes:
   
   1. Create a new init.d script, named: `nexusd`, in order to install Nexus as a system service: 
   
        pi@raspberrypi:~ $ cd /etc/init.d/
        pi@raspberrypi:/etc/init.d $ sudo vi nexusd
        
      Paste the following content into this new file, and save the file:
   
        #!/bin/sh
        ### BEGIN INIT INFO
        # Provides:          nexusd
        # Required-Start:    $remote_fs $syslog
        # Required-Stop:     $remote_fs $syslog
        # Default-Start:     2 3 4 5
        # Default-Stop:      0 1 6
        # Short-Description: Start nexus daemon at boot time
        # Description:       Enable nexus as a system service provided by daemon.
        ### END INIT INFO
      
        NEXUS_HOME="/home/pi/nexus/nexus-3.14.0-04"
        NEXUS_USER="pi"
        
        . /lib/lsb/init-functions
        log_daemon_msg "Nexus daemon called with: $@" "nexusd"
        
        exec sudo -u "$NEXUS_USER" -- "$NEXUS_HOME/bin/nexus" "$@"
        
        log_end_msg $?       

      Here's a file with the same content you could just copy into `/etc/init.d/`: [nexusd](scripts/nexusd)
      
      Be sure to edit the path if your NEXUS_HOME is different (e. g. using a different version).
        
   3. Add execute permission to the new init.d script:

        pi@raspberrypi:/etc/init.d $ sudo chmod +x nexusd        

   4. Setup init scripts using `update-rc.d`:
   
        pi@raspberrypi:/etc/init.d $ sudo update-rc.d nexusd defaults
        
   5. Test the function of the init scripts:
   
        pi@raspberrypi:~ $ sudo service nexusd start
        
      or, just reboot the Pi and see if nexus is running after reboot:
      
        pi@raspberrypi:~ $ sudo service nexusd status
        ...
        Running ...
        
      If for any reason, you want to remove the deamon, run this command:
      
        pi@raspberrypi:~ $ sudo update-rc.d nexusd remove -f
        

   
Next step: [Repository Test](repotest.html)



-----------------

 Old Steps for JSW - for NX2 (no longer required)

 ---------------------------
   
 - To compile ARM compatible JSW service binary for ARM:
    
    see: http://honnix.com/technology/raspberry%20pi/java/2013/07/14/sonatype-nexus-on-raspberry-pi/
    
    and: http://ti57.blogspot.se/2013/05/apache-archiva-on-raspberry-pi.html

    Build notes: Worked with wrapper_3.5.25_src.
   
    - use jsw `build32.sh` script
   
    - Fix/avoid error: `fatal error: jni.h: No such file or directory` by setting java home: 
   
        $ export JAVA_HOME=/usr/lib/jvm/jdk-8-oracle-arm-vfp-hflt



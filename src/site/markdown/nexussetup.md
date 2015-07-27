Nexus Setup
===========

  Download the Nexus bundle from (@todo add link).

  Copy the nexus bundle to the pi, in a new “nexus” folder: /home/pi/nexus

      pi@raspberrypi ~ $ pwd
      /home/pi
      pi@raspberrypi ~ $ mkdir nexus
      
  then: 
  
      my-pc$ scp ~/sonatype/dev/pi/nx3-alpa-bundle/nexus-3.0.0-SNAPSHOT-bundle.tar.gz pi@the-Pi-IP-address:/home/pi/nexus/
      
  unzip/untar:
  
      pi@raspberrypi ~ $ cd nexus
      pi@raspberrypi ~/nexus $ tar -zxvf nexus-3.0.0-SNAPSHOT-bundle.tar.gz

  Start nexus. Move into the nexus bin dir and run:
    
      pi@raspberrypi ~/nexus/nexus-3.0.0-SNAPSHOT/bin $ ./start
  
  While Nexus is starting, you can watch the Pi system load using `top`. Wait for the `java` process to ease up on 
  the cpu (well below 100% CPU in `top`).  Then from your PC, open the link below to Nexus running on the Pi:
  
      http://the-Pi-IP-address:8081

   The default Nexus administrator credentials are user: `admin`, password: `admin123`. 
   Huzzah! Nexus is running on your Pi.  
   
Next step: [Nexus Deamon](nexusdaemonsetup.html)
   

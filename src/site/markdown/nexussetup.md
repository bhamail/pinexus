Nexus Setup
===========
 
 To install Nexus:
  
  1. Verify your java version is at least 1.8.0 or higher:
    
        pi@raspberrypi ~ $ java -version
        java version "1.8.0"
        Java(TM) SE Runtime Environment (build 1.8.0-b132)
        Java HotSpot(TM) Client VM (build 25.0-b70, mixed mode)

  2. Download the Nexus bundle from (@todo add link).

  3. Create a new "nexus" folder at /home/pi/nexus and copy the Nexus bundle into it: 

        pi@raspberrypi ~ $ pwd
        /home/pi
        pi@raspberrypi ~ $ mkdir nexus
      
     then: 
  
        my-pc$ scp ~/sonatype/dev/pi/nx3-alpa-bundle/nexus-3.0.0-SNAPSHOT-bundle.tar.gz pi@the-Pi-IP-address:/home/pi/nexus/
      
  4. Unzip/untar the Nexus bundle:
  
        pi@raspberrypi ~ $ cd nexus
        pi@raspberrypi ~/nexus $ tar -zxvf nexus-3.0.0-SNAPSHOT-bundle.tar.gz

  5. Start nexus. Move into the nexus bin dir and run:
    
        pi@raspberrypi ~/nexus/nexus-3.0.0-SNAPSHOT/bin $ ./start
  
  While Nexus is starting, you can watch the Pi system load using `top`. Wait for the `java` process to ease up on 
  the cpu (well below 100% CPU in `top`).  Then from your PC, open the link below to Nexus running on the Pi:
  
      http://the-Pi-IP-address:8081

   The default Nexus administrator credentials are user: `admin`, password: `admin123`. 
   
   Huzzah! Nexus is running on your Pi.  
   
Next step: [Nexus Deamon](nexusdaemonsetup.html)
   

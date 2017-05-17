Nexus Setup
===========
 
 To install Nexus:
  
  1. Verify your java version is at least 1.8.0 or higher:
    
        pi@raspberrypi:~ $ java -version
        java version "1.8.0"
        Java(TM) SE Runtime Environment (build 1.8.0-b132)
        Java HotSpot(TM) Client VM (build 25.0-b70, mixed mode)

  2. Download the Nexus bundle from [Nexus 3 Releases](https://support.sonatype.com/hc/en-us/articles/218637467-Download-Nexus-Repository-Manager-3).

  3. Create a new "nexus" folder at /home/pi/nexus and copy the Nexus bundle into it: 

        pi@raspberrypi:~ $ pwd
        /home/pi
        pi@raspberrypi:~ $ mkdir nexus
      
     then: 
  
        my-pc$ scp ~/Downloads/nexus-3.3.1-01-unix.tar.gz pi@the-Pi-IP-address:/home/pi/nexus/
      
  4. Unzip/untar the Nexus bundle:
  
        pi@raspberrypi:~ $ cd nexus
        pi@raspberrypi:~/nexus $ tar -zxvf nexus-3.3.1-01-unix.tar.gz

  5. If you try to launch Nexus now, you will likely see an error like the one below:
  
        Java HotSpot(TM) Server VM warning: INFO: os::commit_memory(0x28e00000, 419430400, 0) failed; error='Cannot allocate memory' (errno=12)
        #
        # There is insufficient memory for the Java Runtime Environment to continue.
        # Native memory allocation (mmap) failed to map 419430400 bytes for committing reserved memory.
        # An error report file with more information is saved as:
        # /home/pi/nexus/nexus-3.3.1-01/hs_err_pid1755.log
        
     A Pi currently only has 1GB of RAM, so you need to configure Nexus to use less RAM than
     normal, and allocate more to direct memory for use by the 
     [database](https://support.sonatype.com/hc/en-us/articles/115007093447-Optimizing-OrientDB-Database-Memory-).
     Move into the nexus bin dir, and edit the `nexusvm.options` file:
     
        pi@raspberrypi:~/nexus/nexus-3.3.1-01/bin vi nexus.vmoptions
        
     Change:
     
        -Xms1200M
        -Xmx1200M
        -XX:MaxDirectMemorySize=2G
        
     to:
     
        -Xms256M
        -Xmx256M
        -XX:MaxDirectMemorySize=512M
        
  6. Start nexus.
    
        pi@raspberrypi:~/nexus/nexus-3.3.1-01/bin $ ./nexus start
  
    Startup can take a while. The command above will print messages to the console while Nexus is
    starting. Watch for a message like:
    
        -------------------------------------------------
        
        Started Sonatype Nexus OSS 3.3.1-01
        
        -------------------------------------------------

    While Nexus is starting, you can monitor the system work load using `top`. Wait for the `java` process to ease up on 
    the cpu (well below 100% CPU in `top`).  Then from your PC, open the link below to Nexus running on the Pi:
  
        http://the-Pi-IP-address:8081

     The default Nexus administrator credentials are user: `admin`, password: `admin123`. 
   
     Huzzah! Nexus is running on your Pi.  
   
Next step: [Nexus Deamon](nexusdaemonsetup.html)
   

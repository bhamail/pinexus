Repository Test
===============

 Perform the steps below to test the Nexus repository running on the Pi. 
 You'll need the `IP Address` of the Pi you found earlier when you setup the OS.
 
  1. Create a simple maven settings file (`mysettings.xml`) that will redirect to your Pi to resolve any required 
   libraries.
  
        <settings>
            <mirrors>
                <mirror>
                    <id>mirror-central</id>
                    <mirrorOf>central</mirrorOf>
                    <url>http://the-Pi-IP-address:8081/repository/maven-central/</url>
                </mirror>
            </mirrors>
        </settings>
  
    Here's a file you can use: [mysettings.xml](scripts/mysettings.xml) Don't forget to replace `the-Pi-IP-address` 
    with actual IP address of your Pi.
   
  2. Run any maven build with a custom settings file to use your Nexus repo. Just add the `-s` parameter to use this 
     settings file:
  
        mvn -s mysettings.xml package

  3. You should see maven resolve various dependencies via your Nexus repo on the Pi.
  
Next step: [Doc docs](docdocs.html)
  

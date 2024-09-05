import os 
import subprocess 

services = ["sshd", "mysql", "apache2"] 

def service_monitor(services):
   
    try: 
        for service in services: 
            if subprocess.run(["systemctl", "is-active", "--quiet", service], check=True) == 0:
                print(f"{service} is active") 
            else:
                print(f"{service} is inactive, bring {service} back online") 
                subprocess.run(["systemctl", "restart", service], check=True)

service_monitor(services) 

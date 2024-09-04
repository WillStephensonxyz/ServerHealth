import os 

services = ["sshd", "mysql", "apache2"] 

def service_monitor(services):
    
    for service in services: 
        if os.system(f"systemctl is-active --quiet {service}") == 0:
            print(f"{service} is active") 
        else:
            print(f"{service} is inactive") 

service_monitor(services) 

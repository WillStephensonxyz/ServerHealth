import psutil 
import logging 


def cpu_usage(): 
    cpu_usage = psutil.cpu_percent(interval=5) 
    cpu_cores_logical = psutil.cpu_count() 
    cpu_cores_physical = psutil.cpu_count(logical=False)
    cpu_usage_per_core = psutil.cpu_percent(percpu=True)

    print(f"CPU total usage: %{cpu_usage}")
    print(f"Number of logical threads: {cpu_cores_logical}") 
    print(f"Number of physical cores: {cpu_cores_physical}")
    print(f"CPU usage by core: {cpu_usage_per_core} \n")

def memory_usage(): 
    memory = psutil.virtual_memory()
    total_memory = memory.total / (1024 ** 3)
    available_memory = memory.available / (1024 **3) 
    used_memory = memory.used / (1024 ** 3) 
    memory_usage_percent = memory.percent 

    print(f"Total memory: {total_memory:.2f} GB") 
    print(f"Available memory usage: {available_memory:.2f} GB ") 
    print(f"Used memory {used_memory:.2f} GB")
    print(f"Memory usage percent: %{memory_usage_percent} \n")

def disk_usage(): 
    disk = psutil.disk_usage('/') 
    total_disk = disk.total / (1024 ** 3) 
    used_disk = disk.used / (1024 ** 3) 
    free_disk = disk.free / (1024 ** 3) 
    disk_usage_percent = disk.percent

    print(f"Total hard drive space: {total_disk:.2f} GB") 
    print(f"Hard drive space used: {used_disk:.2f} GB") 
    print(f"Free hard drive space: {free_disk:.2f} GB") 
    print(f"Hard drive usage: %{disk_usage_percent}")

def system_temperature(): 
    pass 

cpu_usage() 
memory_usage() 
disk_usage() 

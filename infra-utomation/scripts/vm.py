# set up vm invoirment
import json 
# Function to get user input for VM configuration   

def get_user_input():
    machine_name = input("Enter the machine name: ")
    machine_os = input("Enter the machine Operating System: ")
    machine_cpu = input("Enter the machine CPU: ")  
    machine_ram = input("Enter the machine RAM: ")
    return machine_name, machine_os, machine_cpu, machine_ram

machine_name, machine_os, machine_cpu, machine_ram = get_user_input()
def create_vm_config(machine_name, machine_os, machine_cpu, machine_ram):
    vm_config = {
        "name": machine_name,
        "os": machine_os,
        "cpu": machine_cpu,
        "ram": machine_ram
    }
    return vm_config

# Save the VM configuration to a JSON file
with open('vm_config.json', 'w') as config_file:
    json.dump(create_vm_config(machine_name, machine_os, machine_cpu, machine_ram), config_file, indent=4)
print("VM configuration saved successfully.")

    ## class structure for VM representation
class VM:
    def __init__(self, name, os, cpu, ram):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram

    def __str__(self):
            return f"VM(Name: {self.name}, OS: {self.os}, CPU: {self.cpu}, RAM: {self.ram})"
    
    # Function to log VM creation
    def log_vm_creation(vm):
        with open('vm_creation_log.txt', 'a') as log_file:
            log_file.write(f"Created VM: {vm}\n")
        print("VM creation logged successfully.")
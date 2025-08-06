# This script allows users to create a virtual machine configuration and log its creation.
#collect user input for VM configuration
import json

# Function to get user input for VM configuration   
do you want to create a virtual machine configuration? (yes/no):
if input("Do you want to create a virtual machine configuration? (yes/no): ").strip().lower() != 'yes':
    print("Exiting the script.")
    exit()  
    
def get_user_input():
    machine=[]
    while True:
        machine_name = input("Enter the machine name (or type 'exit' to finish): ")
        if machine_name.lower() == 'exit':
            break
        machine_os = input("Enter the machine Operating System:(e.g., Linux, Windows):  ")
        machine_cpu = input("Enter the machine CPU:(e.g.,2vCPUs, 4vCPUs): ")  
        machine_ram = input("Enter the machine RAM:(e.g.,4GB or 8GB):  ")
        # Create a VM instance and append to the machine list
        
        instance_data = {
            "name": machine_name,
            "os": machine_os,
            "cpu": machine_cpu,
            "ram": machine_ram
        }

    # validate the input (to be implemented by the user)
    # Example: validation_instance = validate_input(instance_data) 
        if not machine_name or not machine_os or not machine_cpu or not machine_ram:
            print("All fields are required. Please try again.")
            continue     

        machine.append((machine_name, machine_os, machine_cpu, machine_ram))
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
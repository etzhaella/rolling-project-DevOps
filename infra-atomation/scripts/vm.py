# This script allows users to create a virtual machine configuration and log its creation.
#collect user input for VM configuration
import json

# Function to get user input for VM configuration  
# do you want to create a new VM? (yes/no):
def save_vm_data(vm_data, filename='vm_config.json'):
    try:
        with open(filename, 'w') as file:
            json.dump(vm_data, file, indent=4)
        print(f"VM configuration saved to {filename}")      
    except Exception as e:
        print(f"Error saving VM configuration: {e}")                

def get_user_input():
    while True:
        machine_name = input("Enter the machine name: ").strip()
        machine_os = input("Enter the machine Operating System (e.g., Linux, Windows): ").strip()
        machine_cpu = input("Enter the machine CPU (e.g., 2vCPUs, 4vCPUs): ").strip()
        machine_ram = input("Enter the machine RAM (e.g., 4GB or 8GB): ").strip()
        if not machine_name or not machine_os or not machine_cpu or not machine_ram:
            print("All fields are required. Please try again.")
            continue
        return machine_name, machine_os, machine_cpu, machine_ram

## **2. class structure for VM representation 
# basic class structure for managing VM objects

    def __init__(self, name, os, cpu, ram, class_name=None):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram

    # Function to convert VM instance to dictionary for JSON serialization  
    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram,
        }

    def __str__(self):
        return f"VM(Name: {self.name}, OS: {self.os}, CPU: {self.cpu}, RAM: {self.ram})"
def create_vm_config(machine_name, machine_os, machine_cpu, machine_ram):
    vm_config = {
        "name": machine_name,
        "os": machine_os,
        "cpu": machine_cpu,
        "ram": machine_ram
    }
    return vm_config

import logging
# Configure logging
def setup_logging():
    logging.basicConfig(
        filename='vm_creation.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

def main():
    if input("Do you want to create a new VM  ? (yes/no): ").strip().lower() != 'yes':
        print("Exiting the script. No VM created.")
        exit()
    machine_name, machine_os, machine_cpu, machine_ram = get_user_input()
    vm = VM(machine_name, machine_os, machine_cpu, machine_ram)
    logger = setup_logging()
    logger.info(f"Creating VM: {vm}")
    print(vm.to_dict())
    save_vm_data(vm.to_dict())

if __name__ == "__main__":
    main()

## **next steps**
# Extend validation logic 
# integrate more services 
# replace mocked provisioning with actual cloud provider APIs
# Add error handling and logging
# module are learned from the user input and saved to a JSON file.
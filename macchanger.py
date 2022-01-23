#!/usr/bin/env python3

#Importing libraries
import optparse
import subprocess
import re

print("   _____                      .__                                         ") 
print("  /     \ _____    ____  ____ |  |__ _____    ____    ____   ___________  ")
print(" /  \ /  \\__  \ _/ ___\/ ___\|  |  \\__  \  /    \  / ___\_/ __ \_  __ \ ")
print("/    Y    \/ __ \\  \__\  \___|   Y  \/ __ \|   |  \/ /_/  >  ___/|  | \/ ")
print("\____|__  (____  /\___  >___  >___|  (____  /___|  /\___  / \___  >__|    ")
print("        \/     \/     \/    \/     \/     \/     \//_____/      \/        ")
print("*******************Design and developed by bhanugoud**********************")
print("******************Use it for Educational purpose only*********************\n")
print("Usage: macchanger.py --help\n")

#Using parser to provide arguements & options
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Enter interface name")
parser.add_option("-m", "--mac", dest="mac", help="Enter the new mac address you want to asign")
(options, arguments) = parser.parse_args()

#Running commands with subprocess
ifconfig_input = str(subprocess.check_output(["ifconfig", options.interface]))
subprocess.call(["ifconfig", options.interface, "down"])
subprocess.call(["ifconfig", options.interface, "hw", "ether", options.mac])
subprocess.call(["ifconfig", options.interface, "up"])
ifconfig_output = str(subprocess.check_output(["ifconfig", options.interface]))

#Regex method 
mac_address_out = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_output)
mac_address_in = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_input)
mac_out = mac_address_out.group(0)
mac_in = mac_address_in.group(0)

#mac address comparing
if (mac_in == mac_out):
    print('[+] Your mac address is unchanged, your prasent mac', mac_in )
    print('     * Please read usage')
    print('     * Provide sudo privileges')
    print('     * Your providing prasent mac address as input')
else:    
    print('[+] Your mac address is successfully changed to: ',mac_out)

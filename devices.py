import json
file = open("devices.json")
rac_struc = json.load(file)

#exercise 1:
firstdevice_name = rac_struc["rack"][0]["device"]["dev_name"]
print("Name of the first device is " + firstdevice_name + ".")
print("Ip addresses of the first device are:")
for i in rac_struc["rack"][0]["device"]["interfaces"]:    
    print(" " + i["ipaddress"] + ".")

#exercise 2:
print("")
print("List of device names, interfaces and ip addresses:")
for i in rac_struc["rack"]:
    print(" Device name is " + i["device"]["dev_name"] + ":")
    print("  Interfaces and ip addresses are:")
    for j in i["device"]["interfaces"]: 
        print("   " + j["interface"] , j["ipaddress"] + ".")

#exercise 3:
print("")
print("List of interfaces and ip addresses of device R1:")
for i in rac_struc["rack"][0]["device"]["interfaces"]:
        print(" " + i["interface"] , i["ipaddress"] + ".")

file.close()
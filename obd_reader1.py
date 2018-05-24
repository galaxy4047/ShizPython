import obd,time
#from obd import OBDCommands

# OBD setup
obd.logger.setLevel(obd.logging.DEBUG)

# Connect to OBDII adapter
ports = obd.scan_serial()
print("Ports: ")
#print(ports)

connection = obd.OBD("/dev/rfcomm0",baudrate=9600,fast=False)
print("Connection status: ")
print(connection.status())
# Print supported commands
commands = connection.supported_commands
#print("Supported commands: ")
#connection.print_discovered()
#for command in commands:
#    print(command.name)
# Send a command
while True:
    
  #command = input("Enter command (type 'quit' to exit): ")
  #if (command == "quit"):
   #   break
    try:
        res1 = connection.query(obd.commands.RPM,force=True)
        #print(res.value)
        res2 = connection.query(obd.commands.SPEED,force=True)
        rpm_str=str(res1.value)
        rpm_list=rpm_str.split(' ')
        rpm_float=rpm_list[0].split('.')
        print "Integer RPM = "
	print rpm_float
        
        speed_str=str(res2.value)
        speed_list=speed_str.split(' ')
        speed_float=speed_list[0].split('.')
        print "Integer SPEED = "
	print  speed_float
        #print(res.unit)
    except Exception as ex:
        print("Error: " + str(ex))
    time.sleep(3)
# Close the connection
#connection.close()

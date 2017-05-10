#!/usr/bin/env python
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import cisco_xr
def main():
        device_list = [cisco_xr]
        start_time = datetime.now()
        print
        for a_device in device_list:
             net_connect  = ConnectHandler(**a_device)
             output = net_connect.send_command("show arp")
             output1 = net_connect.send_command("show hosts")
             output2 = net_connect.send_command("show ip traffic")
             output3 = net_connect.send_command("show ip int brief")
             print "\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_device['device_type'])
             print output
             print ">>>>>>>>> End <<<<<<<<<"
             print "\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_device['device_type'])
             print output1
             print ">>>>>>>>> End <<<<<<<<<"
             print "\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_device['device_type'])
             print output2
             print ">>>>>>>>> End <<<<<<<<<"
             print "\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_device['device_type'])
             print output3
             print ">>>>>>>>> End <<<<<<<<<"
        print "Time elapsed: {}\n".format(datetime.now() - start_time)

if __name__ == "__main__":
        main()


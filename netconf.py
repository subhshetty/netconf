from datetime import datetime
from netmiko import ConnectHandler
cisco_xr = {
    'device_type': 'cisco_xr',
    'ip': '172.17.0.2',
    'username': 'vrnetlab',
    'password': 'VR-netlab9',
}
cisco_xrv = {
    'device_type': 'cisco_xr',
    'ip': '172.17.0.3',
    'username': 'vrnetlab',
    'password': 'VR-netlab9',
}
def main():
    device_list = [cisco_xr, cisco_xrv]
    start_time = datetime.now()
    print
    for a_device in device_list:
        net_connect = ConnectHandler(**a_device)
        output = net_connect.send_command("show arp")
        print "\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_device['device_type'])
        print output
        print ">>>>>>>>> End <<<<<<<<<"
    print "Time elapsed: {}\n".format(datetime.now() - start_time)

if __name__ == "__main__":
    main()
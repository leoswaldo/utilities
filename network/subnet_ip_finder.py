#!/python3/bin/python3

import argparse
import socket


## Function: validate_subnet
#  Description: validate the parameter subnet has the correct format
#  Paramenters: subnet
#      subnet: subne to validate format
def validate_subnet(subnet):
    segments = subnet.split(".")

    # the subnet must have 3 segments, and every segment be in range of 0-255
    if(len(segments) == 3):
        for index in range(0, 3):
            if(not (int(segments[index]) > 0 and int(segments[index]) < 255)):
                return False
    else:
        return False

    return True


## Function: find_free_ips
#  Description: main function to find ips (IPV4), iterate in the subnet
#  Parameters: subnet
#      subnet: subnet to look
def find_free_ips(subnet):
    error_message = ('\tSubnet does not match correct format: <segment>.<segment>.<segment>\n'
                     '\tEvery segment must be in range greater than 0 and less than 255\n'
                     '\tExample: 10.27.15')

    '''if the subnet has valid format, then iterate through all possible ipv4 in
       the subnet
    '''
    if(validate_subnet(subnet)):
        ip_index = 1
        while(ip_index < 255):
            ip = subnet + "." + str(ip_index)
            try:
                socket.gethostbyaddr(ip)
            except:
                print("Possible free, ipv4 Not responding: %s" % (ip))
            ip_index += 1
    else:
        print(error_message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--subnet',
        help='sunet to search free IP Addresses e.x.: 10.27.15', required=True)

    args = parser.parse_args()
    find_free_ips(args.subnet)
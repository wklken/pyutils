#!/usr/bin/env python
# encoding: utf-8

import socket
import struct

#source https://github.com/kennethreitz/requests/blob/master/requests/utils.py
def dotted_netmask(mask):
    """
    Converts mask from /xx format to xxx.xxx.xxx.xxx
    Example: if mask is 24 function returns 255.255.255.0
    """
    bits = 0xffffffff ^ (1 << 32 - mask) - 1
    return socket.inet_ntoa(struct.pack('>I', bits))


#source https://github.com/kennethreitz/requests/blob/master/requests/utils.py
def is_ipv4_address(string_ip):
    try:
        socket.inet_aton(string_ip)
    except socket.error:
        return False
    return True


if __name__ == '__main__':
    print dotted_netmask(24)
    print is_ipv4_address("127.0.0.1")


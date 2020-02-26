import subprocess
import mmap
import ipaddress
import binascii

ip_result = subprocess.run('ipconfig', shell=True, stdout=subprocess.PIPE)
ip_result_list = ip_result.stdout.split(b'\n')

for ip_info in ip_result_list:
    ip_info = ip_info.strip()
    ip = ip_info.split(b": ")
    if b"IPv4" in ip_info:
        ip_addr = ip[1].decode()
        
        addr = ipaddress.ip_address(ip_addr)
        print(addr)
        print(f" IP version : {addr.version}")
        print(f" is private : {addr.is_private}")
        print(f"packed form : {binascii.hexlify(addr.packed)}")
        print(f"    integer : {int(addr)}")
        print()

        # net = ipaddress.ip_network(ip_addr)
        # print(net)
        # print(f"   is private : {net.is_private}")
        # print(f"    broadcast : {net.broadcast_address}")
        # print(f"   compressed : {net.compressed}")
        # print(f" with netmask : {net.with_netmask}")
        # print(f"with hostmask : {net.with_hostmask}")
        # print(f"num addresses : {net.num_addresses}")

        print()

        

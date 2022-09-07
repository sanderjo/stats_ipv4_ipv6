#!/usr/bin/env python3

def ipv4_octets():
    with open("/proc/net/netstat", "r") as fp:
        for line in fp:
            if line.startswith("IpExt"):
                try:
                    octets = int(line.split()[7])
                    return(octets)
                except:
                    pass


def ipv6_octets():
    with open("/proc/net/snmp6", "r") as fp:
        for line in fp:
            if line.startswith("Ip6InOctets"):
                return(line.strip().split("\t")[-1])



if __name__ == '__main__':


    print(ipv4_octets())
    print(ipv6_octets())

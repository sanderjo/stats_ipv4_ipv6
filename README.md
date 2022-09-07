# stats_ipv4_ipv6
shows ipv4 versus ipv6 statistics on Linux


```
$ ./stats_ipv4_ipv6.sh 
Traffic, down resp up, in MB:
IPv4: 730 49
IPv6: 1633 94
```

Internals

```
$ cat /proc/net/netstat | grep IpExt | awk '{ print $8 }'
InOctets
1450276689
```

```
$ cat /proc/net/snmp6 | grep Ip6InOctets
Ip6InOctets                     	2618863762
```


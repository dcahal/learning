# nmap

This is the nmap scan from OverTheWire's bandit16:   

> First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

```
bandit16@bandit:~$ nmap -A -T4 -p 31000-32000 localhost

Starting Nmap 7.40 ( https://nmap.org ) at 2021-10-15 01:28 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00024s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
| ssl-cert: Subject: commonName=localhost
| Subject Alternative Name: DNS:localhost
| Not valid before: 2021-09-30T04:46:02
|_Not valid after:  2022-09-30T04:46:02
|_ssl-date: TLS randomness does not represent time
31691/tcp open  echo
31790/tcp open  ssl/unknown
| fingerprint-strings:
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq:
|_    Wrong! Please enter the correct current password
| ssl-cert: Subject: commonName=localhost
| Subject Alternative Name: DNS:localhost
| Not valid before: 2021-09-30T04:46:02
|_Not valid after:  2022-09-30T04:46:02
|_ssl-date: TLS randomness does not represent time
31960/tcp open  echo
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31790-TCP:V=7.40%T=SSL%I=7%D=10/15%Time=6168BD3E%P=x86_64-pc-linux-
SF:gnu%r(GenericLines,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20c
SF:urrent\x20password\n")%r(GetRequest,31,"Wrong!\x20Please\x20enter\x20th
SF:e\x20correct\x20current\x20password\n")%r(HTTPOptions,31,"Wrong!\x20Ple
SF:ase\x20enter\x20the\x20correct\x20current\x20password\n")%r(RTSPRequest
SF:,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20password
SF:\n")%r(Help,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\
SF:x20password\n")%r(SSLSessionReq,31,"Wrong!\x20Please\x20enter\x20the\x2
SF:0correct\x20current\x20password\n")%r(TLSSessionReq,31,"Wrong!\x20Pleas
SF:e\x20enter\x20the\x20correct\x20current\x20password\n")%r(Kerberos,31,"
SF:Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\n")%
SF:r(FourOhFourRequest,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20
SF:current\x20password\n")%r(LPDString,31,"Wrong!\x20Please\x20enter\x20th
SF:e\x20correct\x20current\x20password\n")%r(LDAPSearchReq,31,"Wrong!\x20P
SF:lease\x20enter\x20the\x20correct\x20current\x20password\n")%r(SIPOption
SF:s,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20passwor
SF:d\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 88.68 seconds
```

### The prompt gives important clues as to how to interpet the scan.
* Don't want the `echo` services
* Only some support SSL
* The service we want returns some relevant output in plain text.

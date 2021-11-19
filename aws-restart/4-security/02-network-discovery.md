# Prevention: Network Discovery
* Avoiding network discovery is one of the first security controls to implement
* Many vulnerabilities discovered from evaluating protocols in use
* Footprinting, scanning, enumeration used to discover:
    * Online presence
    * Open ports
    * Active services
#### Modern networks offer high availability. As availability inscreases, so does the need for confidentialiy and integrity.
## Network Vulnerabilities
* Early protocols considered only dedicated networks and low-risk security events
* Crypography adds unjustifiable additional overhead
* Ubiquitous access increases risk
* ARP, DHCP, CDMA
### Devices vulnerable both physically and administratively
* AAA server
    * Autentication, Authorization, Accounting
## Layered Defense
### Defense in Depth
* Several layers outside party must penetrate
* Castle
    * Moat, Outer wall, Inner wall, Keep
* Each OSI layer implements defenses or security controls
    * Cryptography
    * Firewalls
    * IDS/IPS
## OSI Security
### Physical
* Equipment protected from physical access
### Data Link
* Filters applied to switches to help prevent attacks based on MAC address
### Network and Transport
* Firewalls and ACLs mitigate unauthorized access
### Session and Presentation
* Authentication and encryption
### Application
* Virus scanner and IDS
## Layered Security Example
### Perimeter
* Firewalls
* IDS or IPS
* DMZ — secure perimeter networks
### Network
* NAC — network access control
* Enterprise IDS or IPS
* Web proxy content filtering
### Endpoint
* Desktop firewall
* Host IDS or IPS
* Antivirus — Content security
### Application
* Dynamic application testing
* WAF — web application firewall
* Database monitoring and scanning
### Data
* IAM
* DLP — data loss prevention
* Data wiping
## Network Discovery Tools
#### Footprinting
* Collecting as much info as possible
#### Scanning
* Searching for weaknesses in system
### Auditing and port scanning
* nmap
* Zenmap (GUI)
* SuperScan (Windows)
### Sniffer
* Wireshark
* OmniPeek
### Vulnerability scanner
* Nessus
* Retina
### ICMP
* ping
* traceroute
### SNMP
* PowerSNMP
* SNMP Traffic Grapher
* Sensor SNMP CPU load
## Finding Info
* ICMP tools
* IANA lookup
* ARIN lookup
    * Shows IP blocks and governing organizations in North America
* Whois
#### Consider blocking ICMP
## Protocol analyzers (Sniffers)
* Mostly passive
* Review and share stored packet captures
* Mitigate utility by using switched networks and encryption
* Policies block users from running these on network
## SNMP tools
* Commonly used in network operations center (NOC) or help desk
* Harden against SNMP detection by outside parties
## Resources
* CVE
    * MITRE Corporation
    * National Cyber Security Division
* Cyberthreat Real-time Map
## Security Policies
* Administrative control to enforce security measures
* Defined by senior management based on risk management decisions * Who is allowed access
* How much use each person is given
* Where personnel might go
* What may or may not be attached

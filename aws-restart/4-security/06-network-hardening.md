# Prevention: Network Hardening
* Principle of least privilege
* Limit protocols used to remote in
* Limit locations to remote in from
## AAA Solution
* Granular authorization
* Log access, commands, changes to network devices
* Enforce change control
    * Processes for managing change requests
## Firewall Placement
* Use as many as make sense for your topology and requirements
    * Number of devices
    * Access requirements
    * Vulnerability risk
* Position firewalls at junction points of network
    * Close to the source to identify or stop bad traffic
## Segmentation
* Different resources on different networks
* Depending on service type
### Why?
* Easier management
* Granular access control
* Less broadcasts
* Better scalability of logical addresses
### Office building analogy
* Segmentation is like having secured areas
* Chemical lab, clean room, electrical room
* Each room has its own swipe card and specific rules
## Disable discovery protocols
* Prevents leaking info about the network
* Protocols often not closely monitored
### Examples
* Link Layer Discovery Protocol (LLDP)
* Cisco Discovery Protoclol (CDP)
## Secure access
* Disable insecure protocols
    * Telnet, HTTP,  SNMP v1
* Require authentication, authorization, accounting (AAA)
* Limit subnets which can be origin of management traffic
* Drop all traffic attempting direct access to device
* Log all access (accountability)
## Traffic best practices
* Deny all
* Allowlist
* Drop all traffic to network control devices
    * Unless originating from trusted network
* Filter as close to the source as possible
    * Internet
    * Internal segments
* Firewalls as primary filters. Other devices as appropriate
    * Defense in depth
    * Defense in diversity
* Log all exceptions



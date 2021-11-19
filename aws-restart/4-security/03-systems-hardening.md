# Prevention: Systems Hardening
## Hardening
* Reduce number of running services
* Change default configuration often
* Security vs. Usability
## Security baselines
Normal conditions on the network
#### Without baseline, you cannot identify security deviations
* Relies on up to date documentation
* Starting point
* What and how secure
* Gets updated to reflect changes made
* Include enhancements
## How to Harden
* Turn off services
* Implement policies
* Patch and update regularly
    * Firmware, OS, apps, other software
* Security mindful software development
### Servers
* Restrict physical access
* Use edicated roles
* Secure filesystems
* Use encryption and PKI
* Use alerts
* Apply updates
* Limit admin access
### Clients
* Antivirus and firewalls
* Run fewer applications
* Apply updates
* Limit removable media
* Control downloads
* Restrict terminal
* Monitor environment
## Mobile Device Management (MDM)
* Enforces company policy on mobile devices
* Especially important if company allows BYOD
## Hardening the Network
Prevention techniques to protect against:
* Man in the middle events
* Session hijacking
* Credential hijacking
* Remote connectivity malware
#### Techniques
* Switch config and port limitations
    * Switches segment the network
* Decoy networks
    * Honeypot devices
    * Honeynets
    * Deflect attack
    * Gain information about attacker
* Firewalls and ACLs
## Analysis Tools
Choose tools based on company size and needs. SOHO vs Enterprise.
### Wireshark
* Free network sniffer
* View traffic
    * Transactions, protocols
    * IP, MAC
* Identify unencrypted or rogue communications
#### Commercial sniffers
* IBM Security AppScan
* Colasoft Capsa Network Analyzer
### Vulnerability Scanners
* Nessus
* Nexpose
* Acunetix
#### Using vulnerability scanner
* Passive tools
* Run against system or network
* Check against database of vulnerabilities and exposures
* Generate report with potential fixes
## AAA
### Authentication
* You are who you say you are
### Authorization
* You have permission to access this resource
### Accounting
* Collects usage info used for auditing or billing
## Physical security
* The base of all security principles
* Restrict access
* Durable building design
#### Most vulnerability is at the human level


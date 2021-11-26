# Detection
After prevention fails
## Malware
* Malicious software
* Designed to harm
* Interrupting CIA triad
    * Confidentiality
    * Integrity
    * Availability
### Infection vectors
* Websites
* Unpatched software
* Removable devices
* Social engineering
* Email
* Lax permissions
* Weak protection
* Software from untrusted source
## Types of malware
#### Virus
* Takes over system application
* Runs every time normal program runs
#### Worm
* Gains remote access
* No executable
* Exploits app vulnerabilities
#### Bot
* Takes control of system
* Performs task
#### Trojan
* Server stealing client info
* Gain system access
* Found by monitoring network and system activity
#### Rootkit
* Replaces system files capable of revealing it
* Becomes part of the OS
* Recovery often requires reformat
#### Spyware
* Embedded in application
* Violated privacy
#### Adware
* Similar to spyware
* Ads, interactive elements
#### Ransomware
* Locks down system until paid
## Viruses
### Direct action
* Immediately infect files or programs when run
### Polymorphic
* Self-encrypted to avoid detection
* Duplicates slightly changed copies of itself
### Logic bomb
* Code injection
* Triggers function when requirements met
### Memory-resident virus
* Hides in RAM
* Looks for other files and programs to infect
### Cluster
* Linked to implementation of other software
### Cavity
* Installed to empty bits of infected file
## Countermeasures
* User awareness program
* User permissions
* Firewall
* Monitor network
* Verify file integrity
* Harden system
* Establish policies
* Implement baseline
* Intrusion tests
* Physical security
* Scan incoming communications
* Update antivirus
* Regular scans
## IDS
* Monitoring
* Notification
* Reporting
    * Source address
    * Victim address
    * Type of attack
## Social Engineering
* Circumvent controls through deception
### Goals
* Sensitive company or personal data
* Physical location or assets
* Systems (physical and electronic)
### Why does it work?
* Lazy habits
* Lack of penalties
* Inability to trace security leaks
* Lack of enforcement for existing policies
* Lack of training or mature tools
### Direct
* Onsite attack from unauthorized person
### Indirect
* Attacker not with onsite target
* May not be actively attacking when target divulges info
### [PhishTank.com](https://www.phishtank.com/)
* Monitors phishing threats
* API
## Cyber Awareness
* Train on policies
* Policies come first
* Management on board
* Consequences for noncompliance
## Software Development security
* Change management and communication
* Separation of duties
* Peer reviews
* Production and Development team relationship
* QA
* Background checks
* Prioritize maintenance (code escrow)
## Software Vulnerabilities
### Buffer overflow
* App not secured with boundary checks
* Infect code into running program
### Database injection
* DB altered using frontend
* Missing or incomplete input validation
* Counter:
    * Code review
    * fuzz testing
    * Web application firewall
### Cross site scripting (XSS)
* Code injection from third party web resource
* Runs every time page loads
* Counter:
    * Restrict running scripts
    * Harden browser
    * Secure forms through firewall or IDS
    * Pen testing
### Directory traversal
* User gets loose on web server
* Attack relies on malformed URL
* Counter:
    * Security updates
    * Limit input URL formatting
### Security misconfiguration
* Secure at web-server and web-app level
* Open Webb Application Security Project (OWASP)
### Lax permissions
* Use ACLs to secure application directories
    * "Directory browsing" — risk info disclosure
### Session hijacking
* MITM attack on HTTP requests
* Take over session
* Impersonate authenticated user
    * Session ID
    * Session cookie
* Counter:
    * Transient cookies
    * Short session timeouts
    * Don't reuse session IDs
* Prinicple of least privilege


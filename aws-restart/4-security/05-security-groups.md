# Security Groups
* Firewall for EC2
* Rules determine who has access to instances
* Stateful
## VPC and Security Groups
* SG applies to EC2 instances in a subnet
* Network ACL firewalls associated subnets
* EC2 uses key pairs
    * Public key on server
    * Create key pair
    * Specify name when launching instance
    * Provide private key at login
    * Windows keypairs grant admin password for RDP
### Stateful SG vs. Stateless NetACL
* Stateful
    * Computer tracks state of interaction by setting values in storage
* Stateless
    * No info retained by sender or receiver. Each request must be handled based entirely on info that comes with it.
## Three tier web app architecture
### Web tier
* SG accepts traffic from anywhere
* Intranet SSH
    * 0.0.0.0/0 : 80/443
    * Allow intranet IPs : 22
### Application tier
* Accept only HTTPS traffic from web tier
* Intranet SSH and RDP
    * Web tier : 443
    * Allow intranet IPs : 22/3389
### Database tier
* Accept only HTTPS traffic from app tier
* Intranet SSH and RDP
    * App tier : 443
    * Allow intranet IPs : 22/3389

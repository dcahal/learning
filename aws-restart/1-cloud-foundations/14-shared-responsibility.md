# Shared Responsibility Model
AWS and customer are both responsible for customer and user data.

## AWS: Security OF the Cloud
* Data Centers
    * Guards, 2FA, access logging, surveillance, disk degaussing
* Hardware: servers, storage, other appliances
* Software: Host OS, hypervisor, service apps
* Network: Routers, switches, load balancers, firewalls, cabling
    * Monitoring external boundaries, access points. Redundant infrastructure
* Virtualization: instance isolationi

## Customer: Security IN the Cloud
* Secure your resources and applications
* Configure network, security groups, users, firewalls
* IAM settings

### Complete control and liability for content
* Encrypt your own data
* What content goes in AWS
* Which AWS services are used with what content
* Access rights management

### Customer secures IaaS
* EC2, EBS, VPC
* Customer handles security patches, OS updates, etc.

### AWS secures PaaS
* Lambda, RDS, Elastic Beanstalk
* Customer still sets permissions

## Q: Who handles upgrades and patches?
* A customer uses an Oracle instance
* AWS if running as RDS
* Customer if running on EC2


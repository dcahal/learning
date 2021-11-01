# AWS Virtual Private Cloud
* Provision logically isolated section of AWS cloud
* Virtual network that you define
* Control networking resources
    * IP range
    * Subnets
    * Route tables and network gateways
* Customize its network configuration
* Multiple layers of security
#### Foundational service. Works with many other AWS services.
## VPC Features
* Logically isolated from other VPCs
* Attached to an AWS account
* Multiple VPCs per account
* Belongs to a single region
* Can span multiple AZs
* Can create subnets
## IP addressing
* Specify IPv4 CIDR block
* Max size `/16` (65,536 IPs)
* Min size `/28` (16 IPs)
* Address range cannot be changed later
* IPs should not overlap with addresses in other networks VPC connects to
## VPC Components
### Subnets
* AWS reserves first four and last four IPs of every subnet
#### Public subnet
* Accessible from within VPC and from internet
#### Private subnet
* Accessible from within VPC only
### Route table
* Routes used to determine where network traffic is directed
* Every subnet needs association with a route table
* 1 route table assigned to 1  VPC
* Multiple VPCs per route table
### Security group
* Virtual, stateful firewall
* Controls traffic to AWS resources and EC2 instances
### Network ACL
* Optional layer of security
* Stateless firewall for controlling traffic in/out of 1+ subnets


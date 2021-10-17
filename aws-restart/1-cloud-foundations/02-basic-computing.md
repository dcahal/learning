# Basic Computing

## Servers
* Provide data and services to other computers
* Take requests from clients over the network
* Redundant power supplies or UPS

### Data Center
Has all the servers, storage, routers, switches, hubs, cooling, and UPS

### Web app: how it works
1. Client sends request
2. Web server directs request to application
3. Application accesses app data from database management system (DBMS)
4. Database server returns app data to web server
5. Web server serves page to client

### Outsourced to cloud
* Data Center
* Buy, configure hardware and software
* Staffing
* Maintenence

## VMs
Host: physical system
Hypervisor: software provides access to and distributes system resources
    1. KVM, Hyper-V, Proxmox, Xen, VMWare ESXi
    2. VirtualBox, QEMU, VMWare Workstation

### Why VMs?
* Cost savings
* Efficient utilization
* Reusability and portability

> For example, creating multiple copies of the same VM to respond to incoming requests can improve your applications’ performance when the number of requests increases.


### AMI ➡ EC2
Amazon Machine Image (AMI) is launched as an Elastic Cloud Compute instance (EC2).
* Provision instance resources as needed
* Scalable


## Software Development Lifecycle (SDLC)
### Plan
What is the problem? What resources are needed to solve it?
* Project plan
* Evaluate costs, HR, operational, technical considerations
* Plan for QA
### Analyze
What do we want from a solution?
* Software Requirement Specification (SRS)
* Customer approval
### Design
How will we build what we want?
* Design specification document
* Evaluate possible architecture
* Describe functions, GUI, etc.
* Risk, budget, time review
### Develop
Build it!
* Write code to design specification
* Choose language
### Test
Did we get what we want?
* Automated testing: code to test the code
* Common types of test:
    * Unit test: test application components at the program level.
    * Integration test: test combinations of multiple components to verify they work together.
    * Security: probe for vulnerabilities, internal or external.
    * Performance: benchmark and check against needs
### Implement
Deploy to production
### Maintain
Improve it! Types of maintenance include:
* Corrective: squash bugs
* Adaptive: respond to changes in the app's runtime environment (e.g. broken dependency)
* Perfective: new or revised functionality
* Preventative: avoid future issues (e.g. refactoring, improve portability)




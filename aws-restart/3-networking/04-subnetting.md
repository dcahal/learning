# IP Subnetting
Creating smaller networks by dividing an address block into contiguous subdivisions.
* Useful for managing multiple networks (e.g. multiple offices, public + private networks)
## Subnet
* Creates multiple logical networks with different address ranges
* CIDR notation specifies subnet range
* Classless Inter-Domain Routing
* Devices in the same subnet can communicate without routers
* Networks with Class A, B, or C addresses can be subnetted
## IP Address Record Classes
* Based on size and subnetting capabilities of the supported network
* Determines potential for division of organization's network space
### Class A (0.0.0.0 to 127.255.255.255)/8
Extremely large networks like ones built by ISPs
* Record provides for up to 126 networks
    * 16,777,214 addresses each
* Rare for a single organization to own a Class A record
    * Apple: `17.0.0.0/8`
    * MIT: `18.0.0.0/8`
### Class B (128.0.0.0 to 191.255.255.255)/16
Medium to large networks like enterprises
* Record provides for up to 16,384 networks
    * 65,000 adresses each
### Class C (192.0.0.0 to 223.255.255.255)/24
Small networks such as home or small business
* Record provides 2,097,150 networks
    * 254 addresses each
## Reserved IPs
### Unknown: 0.0.0.0
* Generally not assignable
* Usually means unknown or unroutable
* May mean any address on a server
### Loopback: 127.0.0.1
* Returns message home to origin
* Used for testing and debugging
* Allows specific config of inter-domain routing between routers
### All Broadcast: 255.255.255.255
* All devices on the network
* Send to every device at once
* Reduced routing workload
## Purpose of Subnetting
* Isolate different parts of the network
* Apply different levels of security to those parts
* Relieve network congestion
### Subnet Mask
Defines which part of address identifies the network and which identifies the hosts
#### Users connect out through router or default gateway
## Classless Inter-Domain Routing (CIDR) Notation
* `x.x.x.x/n`
* IP divided into **network prefix** and **host identifier**
* `n` is length of the network prefix in bits
* Larger `n` means smaller subnet
    * Amazon: `17.0.0.0/8`
    * House: `192.168.10.0/24`

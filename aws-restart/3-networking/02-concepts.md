# Networking Concepts
### LAN
* Ethernet and wifi
* High transfer rate
* Floor, building, campus
### WAN
* Used to connect LANs
* Fiber or satellite
* Multiple cities or countries
* Internet is largest WAN
## Management Models
* How data is managed and applications are hosted
### Client-server
* Data and app are centralized in server
* Clients must access server for information
* Clients won't work if server down
### P2P
* Every node has its own data and apps
* Equal privilege
* Each node responsible for management and security
* Use case: low security, limited peers
## Topologies
* Pattern of how nodes connect to each other
    * `Physical`: layout of wires in network
    * `Logical`: how data moves through the network
### Bus (old)
#### Physical
* aka Backbone
* All devices along a single cable
* Single direction
#### Logical
* Moves in one direction
* One computer at a time sends signal
* Network collisions can bring down network
### Star (old)
#### Physical
* Every node directly connected to one switch
#### Logical
* Central switches manages data transmission
* Switch can act as repeater to prevent loss
### Mesh
* Nodes interconnected
    * `Full`: all nodes
    * `Partial`: each node connected to two others
* Expensive
* Multiple cables and adapters
* Used in WAN
### Hybrid
* Combines two or more different topologies
* Large enterprises with different departments
* Star-bus most common
## [OSI model](./osi-model.md)
* Standard for how computers share information over a network
## Protocols
* Rules for formatting and transmitting data
* Layer 3 and 4 (network and transport)
### Connection-oriented protocols
* Like a phone call
* TCP
* Establishes connection
* Waits for response
* Creates session between parties
* Synchronous communication
### Connectionless protocol
* Like mailing a letter
* UDP
* Sends message from one endpoint to another
* No handshake before sending
* Does not require a session
* Asynchronous communication
### IP — Internet Protocol
* Rules for relaying and routing data in the internet
### TCP — Transmission Control Protocol
* Reliable and ordered delivery of bitstreams over IP network
### UDP — User Datagram Protocol
* Simple, minimum set of functions to communicate over IP
* No guarantee of orderly delivery or successful delivery
* Faster and lower overhead than TCP


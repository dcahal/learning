# Open Systems Interconnection model
Defines a standard for how computers share information over a network
## 7. Application
* Provides interface enabling applications to access network services
## 6. Presentation
* Ensures data is in usable format. Encrypt and decrypt
## 5. Session
* Maintains distinction between data of separate applications
## 4. Transport
* Establish connection between source and destination
* Specify which transmission protocol to use
## 3. Network
* Decides physical path the data will take
## 2. Data Link
* Defines format of the data on the network
## 1. Physical
* Transmits raw bitstream over the physical network
## Packet Flow
* Data from source computer is processed and transformed down layers
* Optionally encrypted
* `Headers`: transmission-related info added to data in route
* Data becomes `packet` ready to move through physical network
* Target computer unpacks data in reverse order. Layer 1-7

# Prevention: Public Key Infrastructure
* Distribution and implementation of keys
* Certificate authorities (CA)
* Certificates
* Revocation lists
* Registration authorities (RA)
* Certificate templates
* Entities, users
## Certificate Authorities
* Issue certificates to entities
### Certificate template
* CA name
* CA type
* CA integration
* Key specs
* Database properties
### Other documents issued
* Certificate practices statement (CPS)
    * Standards, practices, algorithms of CA
* Certificate policy for customers of CA
    * Revocable offenses
### Root CA
* Top of hierarchy
* Stores root keys
* Kept offline and isolated
* Does not directly service entities
### Subordinate CA (Registration Authority)
* Verifies and validates entity requests
* Issues certificates
* Not required in small environment
### Internal CA
* Can be used if protected resource is not published externally
## Trust
* Prevents rogue systems from intercepting secure communications
* Key pair exchange validates identities
### Public keys
* Attached to certificate
* Ensure trust throughout hierarchy
* For system requesting certificate
* For system offering service
## Certificates
* Represent online identities
* CA vs. self-signed
* Public and private key for encryption and decryption
* Using only public key, certificate establishes trust
### TLS/SSL
* Issued by CA
* Key pair unique to organization requesting cert
### Code signing
* Authenticate publisher of software 
* Author signs with cert's private key
## Issuance
### Certificate Signing Request (CSR)
* Used by external CA
* Create CSR file on server
    * Details about organization
* Submit CSR and receive certificate from CA
* Install certificate
#### Creating CSR
* Open source and vendor-specific tools available
### AWS Certificate Manager
* AWS internal CA
* AWS Certificate Manager Private Certificate Authority
## Certificate Revocation List (CRL)
* Lists expired and revoked certs
* Checked when cert is used
* Must be published and accessible
    * Especially for internal CA
* Maintaining multiple CRLs is big effort
### OCSP — Online Certificate Status Protocol
* Used to get revocation status of cert
## Cert Storage
* Local computer
* TPM
* Smart Card (credit card chip)
### Common Access Card (CAC)
* Smart Card
* ISO 7816 chip
    * gold square
    * can hold multiple certs
* Can hold other ID and authorization data
#### Other technologies in CAC
* Optical area on front
* Magnetic strip
* Photo ID
* RFID
    * transmit signal to nearby device
    * electronic door locks

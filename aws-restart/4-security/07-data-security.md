# Prevention: Data Security
* Data in motion
* Data in rest
## Cryptography
* Principles and techniques for providing data security
* Collection of best practices
* Ensure confidentiality and data integrity
* Encryption is only a piece
## Symmetric Encryption
* Same key is used to encrypt and decrypt
* Key is a shared secret
* Fast, reliable
* For bulk data
### Block cipher
* Key and algorithm that are applied to a block of data at once
### AES — Advanced Encryption Standard
* 3x 128-bit block ciphers
* Key sizes: 128, 192, 256 bits
* Amazon EFS uses AES-256 to encrypt data at rest
#### IDEA
* Patented
* Block cipher with 128 bit key
#### Twofish
* Slower than AES
## Asymmetric Encryption
* Private-public key pair
* Every user has a key pair
* Slower and more complex
* More key management capabilities
### RSA — Rivest-Shamir-Adleman
* Algorithm based on prime number factorization
* Significant time and processing power
* Standard for important data sent over internet
#### DH
* Key exchange over a public channel
* Numbers raised to powers to produce keys
#### ElGamal
* Uses algorithm based on DH method
## Hybrid encryption
* Uses both methods
### Steps
* Use shared key to encrypt message
* Use destination public key to encrypt again
* Destination uses private key to decrypt
* Use shared key to fully decrypt
### TLS and SSL are hybrid encryption
## Practical Examples
### Data in motion
* TLS
* Kerberos
* IPsec
    * Used by VPNs
* Email
    * PGP
    * S/MIME
### Data at rest
* LVM
* VeraCrypt
* Bitlocker
## Hashing
* Generate a unique hash value of content
    * Message digest
* Ensures data integrity
* SHA1
* MD5
## Permissions
* Specific type of access to a resource
### Discretionary Access Control
* User assigned level of access
* Level information stored in ACL
* Decentralized access
* Auditing
* Dynamic access control
#### Access control entries
* Demarked permissions in an ACL
* ro, rw, rwx
### Role-based
* Role assigned level of access
* Users assigned to role groups
* Low level of interaction needed to change
* Customizability
* Granularity

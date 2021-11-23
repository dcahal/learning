# Prevention: Identity Management
## Secure login steps
### Identification 
* Prove who you are
* Uniqueness
### Authentication
* Verification
* Check face against photo
### Authorization
* Validation
* Issue visitor badge
### Accounting
* Tracking
* Sign visitor log, date/time, badge number, reason
## PII — Personally identifiable information
* Alone or with other data can identify individual
* Direct identifiers
    * Passport
* Indirect identifiers
    * Birthday
    * System info
## Authentication Factor Types
### Something you KNOW
* Password, PIN
* Simple
* Least secure
### Something you HAVE
* Usually second factor
* Physical key, card, dongle
* Token, certificate
### Something you ARE
* Biometrics
* Fingerprint, facial recognition, retinal scanner
* Validates unique human property
* Expensive
* Accuracy is paramount for reliablity
## Password policy
* Minimum size
* Complexity
* Maximum age
* Max failed attempts
#### Do NOT use group accounts
### Attacks
* Dictionary attacks
* Rainbow table attack
    * Table stores hashes of possible passwords
    * Compared against stolen hashes to find password
    * Passwords easily cracked when attacker knows algorithm used for hashing
### Password managers
* Centralized authentication system
* Require extra login steps
* Allow password resets
* Manage services used with specific credentials
* Store personal passwords on local system
#### On Server:
* Password consolidation
* Security questions
* Reset
* Permitted services
### Single sign-on (SSO)
* Password synchronized between two independent systems
* Common, trusted credentials across systems
* Systems not in a trust relationship
* Systems do not belong to same directory structure
* Users log in once and gain access to multiple applications
#### Federated Users
* Token-based SSO implementation used between web identities
* User verifies between distinct systems using token
    * Sign into Facebook using Google account
## Identity Providers
#### Amazon Cognito is AWS identity provider
* IDaaS creates and controls access levels for users
    * "SSO for the cloud"
* Remote database of user records
* Creates single set of credentials for all platforms, networks, apps
* Systems check with identity provider to verify access rights

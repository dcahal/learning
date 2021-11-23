# AWS Identity and Access Management (IAM)
* Securely manage access to AWS services and resources
* AWS users and groups
* Allow/deny permissions
## IAM Features
* Free feature of AWS accounts
* Global, all-region service
* Create users, groups, roles
* Apply policies to entities to control access
### Authentication
* Who can access resources
* User authentication
* Applications and services for access
### Authorization
* Defined through policies
* Which resources users can access
* What they can do with it
#### Policy object
* Associated with identity or resource
* Defines its permissions
#### IAM benefits
* Reduced sharing of passwords or keys to other systems
* Easy to enable or disable a user's access
* Centrally manage access re: who can
    * Launch, configure, manage, terminate resources
* Granular control over entities who might make API calls
## Account Root user
* New account starts as root
* Full access to everything
* Sign in with email and password of AWS account
    * **DO NOT USE** day to day
* Cannot control permissions of root user
### Create additional users
* Principle of least privilege
* Can create admin users with full access
    * Or read-only users
* Unique credentials for each user
## BEST PRACTICES
* Delete root user access keys
* Create IAM user with admin rights
* Enable MFA
* Use this account for administration
## AWS Credentials
### Email and password
* Account root user
### IAM username and password
* AWS Management Console
### Access keys and secrets
* AWS CLI
* APIs
* SDK
### MFA
* Root and IAM users
* Hardware or OAuth
* AWS STS (Security Token Service)
    * Web service
    * Issue temporary, limited credentials
### Key pairs
* EC2
* Other specific services
## IAM: Authorization
* Create IAM policy to assign permissions
* Permissions are allow list
* Deny all by default
* Explicit deny trumps allow
## IAM Users
* No credentials or permissions by default
* Only an identity + permissions
* Can represent an application making requests to AWS
* Think users for daemons in Linux
## IAM Groups
* Collection of IAM users
* Apply permissions to whole group
    * "Developers" group
* No default group
* No nested groups
## IAM Roles
* Grants temporary access
* Permissions not attached to user or group
* Apps and services assume role at runtime
### Benefits
* Allows app to user to make API calls
* No need for long-term credentials or new IAM user
* Use case: federated users with no permanent identity
### Creating roles
* Trust policy
    * Who can assume the role
* Access policy
    * Permissions the principal can access
* Principal can be
    * AWS account
    * AWS service (like EC2)
    * SAML provider
    * Identity provier
    * IAM user, group, role from **other account**
## IAM Permissions
* Policies stored in JSON
    * Use version control
* Principle of least privilege
* Customize with authorization policy
* Implicit deny
## IAM Policies
* Attach policy to any IAM entity
* Authorize actions that may be performed by entity on specific resources
* Single policy can be attached to multiple entities
* Single entity can have multiple policies attached
#### Attach policy to group instead of many users
## Types of Policies
### Identity-based 
* Attach to principal or identity
* What they can do on what resources under what conditions
* Managed policy
    * Standalone identity policy can be attached to multiple entities
* Inline policy
    * Embedded directly into single entity
### Resource-based
* JSON documents attached to resource (e.g. S3 bucket)
* Controls what specified principal can do on that resource
* Only inline policies
### IAM Policy Simulator
* Test, troubleshoot IAM and resource-based policies


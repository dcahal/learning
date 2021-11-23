# Security Best Practices for Creating AWS Account
## Stop using account root user
1. Create IAM user for yourself
2. Create an IAM group with admin permissions
3. Add your user to the group
4. Securely store account root user login credentials
5. Sign in with your IAM credentials

## Require MFA for access
* On all AWS root user and IAM users
* Use MFAs to control access to AWS service APIs 
### Software MFA
* AWS virtual MFA
* OAuth
* SMS
### Hardware MFA
* YubiKey
* Gemalto

## Enable CloudTrail
1. Create a trail in CloudTrail console
    * Give trail a name
    * Apply trail to all regions
    * Enter name of new S3 log bucket
2. Restrict access to log bucket

## Enable a billing report: AWS Cost and Usage Report
* Provides info about your resource usage and estimated costs
* Daily or hourly report delivered to S3 bucket of your choice

## IAM Best Practices
### Delete root user access keys
### IAM users
* Create individual IAM users
* Prune unnecessary users and credentials
### Use groups to assign permissions to IAM users
### IAM roles
* Make roles for applications running on EC2
* Delegate using roles instead of sharing credentials
### Hardware access control
* Principle of least privilege
* Strong password policy
* Enable MFA for privileged users
* Use policy conditions
* Rotate credentials regularly
* Monitor activity on AWS account

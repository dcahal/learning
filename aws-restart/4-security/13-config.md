# AWS Config
* Assess, audit, evaluate your AWS resource configuration
* Fully managed
* Nearly continuous monitoring
* Nearly continuous assessment
* Change management
* Troubleshooting
#### Simplfy compliance auditing, security analysis, change management, and operation troubleshooting.
## Features
* AWS resource inventory
* Config history
* Config change notification
* Details of all config changes
* Combine with CloudTrail
* Export your AWS setup with all config details
## Security Benefits
### Detection
* Create detection controls
* Identify anomalies
### Compliance
* Create rules assessing compliance
* Assist with aligning with SOC certifications
* Review config changes
* Review relationship between AWS resources
### Access Control
* Create IAM roles to grant Config access to resources like S3
* Config can call other services on user's behalf
    * Create service-link roles linked to Config with all necessary permissions
### Config configuration item
* Created whenever Config detects change to a resource
* Metadata
* Attributes
* Relationships
* Current configuration
* Related events
## AWS Config Rules
* Check change records against Config rule
* Displays result on dashboard
* Can be sent to Amazon SNS
### Making rules
* Define custom rules using Lambda
* Use rules from AWS and AWS Partners
* Target rules at tags, specific resources, or types of resources
* Evaluate rules when target is created or changed
    * Or on recurring schedule
### Use case
* Verify config changes are recorded
### Dashboard
* Visualize compliance
* See important results
## Example rules
* Rule is any condition
* EBS volumes are encrypted
* Instances are using only approved AMIs
* Elastic IPs are attached to instances
* EC2 instances are properly tagged

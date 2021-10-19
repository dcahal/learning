# AWS Pricing Fundamentals
* Compute
    * charged per second (Linux)
    * charged per hour (Windows)
    * Varies by instance type
* Storage
    * charged per GB
* Data transfer
    * Outbound data aggregated as *AWS Data Transfer Out*
    * **Some** inbound data billable (moving data across AWS regions)
    * charged per GB
* Custom pricing for some clients

### Pay for what you use
Billed monthly for all resources used in that time. Modify resources any time. No licensing.

### Pay for what you reserve
#### Reserved capacity discounts for services like EC2 and RDS.
* AURI - All Upfront Reserved Instance
* PURI - Partially Upfront Reserved Instance
* NURI - No Upfront Payments Reserved Instance
* On demand instance (no discount)
<br>
Minimize risk, predictable budgets, compliance with long-term commitments

### Pay less for using more
* Tiered pricing (builk discounts) on volume-based services like S3, EBS, EFS.
* Further reduce costs by choosing effective use of storage services based on storage performance and access frequency.
    * Glacier vs. S3

### Pay less as AWS grows

## Pricing Calculator
#### Helps you estimate and budget.
* Prices for all services, all regions
* Itemized by region
* Create templates for deployment models
* Access sample data

## Total Cost of Ownership (TCO)
#### Direct and indirect costs of service and associated expenses
* Direct costs of data center
    * Electricity
    * Facilities
    * Floor space
    * Labor
* Indirect costs
    * Network infrastructure
    * Storage infrastructure

## AWS Free Tier
### One Year
* EC2 T2
* S3
* EBS
* ELB
* Data transfer
        
### Always Free
* Consolidated billing
    * One bill for multiple accounts
    * Combine useage for discounts
    * Track all charges
* Automatic Scaling
    * Up and down according to demand
* VPC
    * Define virtual private network for your resources
* IAM
    * Control user access to resources and services    
* Elastic Beanstalk
    * Quickly deploy and manage apps    
* Cloud Formation
    * Create a collection of AWS resources and deploy in orderly fashion
* OpWorks
    * Application management for easier deployment


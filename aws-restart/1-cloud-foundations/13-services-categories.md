# AWS Services and Categories
Compute, Networking, Storage

## Storage
* S3: object storage
    * data for web, app, backup, analytics
* EBS: high performance block storage
    * databases, containers, file systems, analytics engines
* EFS: Network File System scales to petabytes on demand
* S3 Glacier: Extreme durability and security. Near-100% durability, "Eleven nines"
    * Long term archival and backup

## Compute
* EC2: Resizable VM using KVM
* EC2 Autoscaling: Add or remove capacity based on your defined conditions
* Elastic Beanstalk: Deploy web apps on Apache or Microsoft IIS
* Lambda: Serverless deploy. Only pay for ran compute time.

## Containers
* ECS: Orchestration service supporting Docker containers
* Fargate: Compute engine for ECS. Run containers without managing cluster
* ECR: Docker image registry
* EKS: Deploy on Kubernetes


## Database
* RDS: Relational database. Automates provisioning and configuration.
* Aurora: Relational database. MySQL and Postgres compatible
* Redshift: Run analytic queries against data stored in Redshift or S3.
* DynamoDB: Key-value and document DB. <10ms performance

## Networking and Content Delivery
* VPC: Provision logically isolated AWS resources
* Elastic Load Balancing: Automatically distribute incoming traffic to multiple targets
* CloudFront: CDN
    * APIs can run over a CDN
* Transit Gateway: Single gateway for VPC and on-prem
* Route 53: DNS
* Direct Connect: Dedicated private connection between your data center and AWS
* AWS VPN

## Security, Identity and Compliance
* IAM: users, groups, permissions
* Organizations: restrict access to services and actions for your accounts
* Cognito: add user sign-in and access control functionality to your web app
* Artifact: view security and compliance reports
* KMS: Create and manage keys
* Shield: Managed DDoS protection

## AWS Cost Management
* Cost and Usage Report: includes metadata about AWS services, pricing, and reservations
* Budgets: Set custom budget alerts
* Costs Explorer: Visualize and manage costs over time

## Management and Governance
* AWS Management Console: web console for AWS
* AWS CLI
* Config: Track resource inventory and changes
* CloudWatch: Monitor resources and apps
* Auto Scaling: scale multiple resources
* Trusted Advisor: helps optimize performance and security
* Well-Architected Tool: helps review and improve your workloads
* CloudTrail: tracks user activity and API usage

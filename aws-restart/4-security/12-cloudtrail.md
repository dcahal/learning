# AWS CloudTrail
* Logs API calls for the account
* Everything in AWS is an API call
* Simplfy governance, compliance, risk audiiting
* Global, all-regions
* CLI, SDK, GUI, or direct API calls
### Examples
* Start or stop EC2 instances
* Create or modify RDS database
* Upload a file to S3 bucket
## Benefits
* Eye into user and resource activity
* Identify blame
* Simplfy compliance audits
    * Search through data
    * Identify noncompliant actions
* Comprehensive history
## CloudTrail event
* Who performed request
* Date and time
* Source IP
* How request was made
* Action performed
* Region where action was taken
* Response
### Managing logs
* Kept 7 days by default
* Can send to other AWS services
* Effectively permanent history
## BEST PRACTICES
* Turn on log file validation
* Send logs to one S3 bucket
* Enable CloudTrail globally
* Restrict access to log bucket
    * Validate log integrity
    * Require MFA to delete
### Integrate with CloudWatch
* Run actions when CloudTrail logs certain events
* Cron jobs
* Comprehensive, secure, searchable history
#### CloudWatch
* Monitoring service
* Collect and track metrics and log files
* Set alarms
* Automatically react to resource changes

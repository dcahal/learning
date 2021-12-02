# AWS RDS
* Managed relational database
* Spin up takes up to 20 min
## Backup
### Automatic
* Daily snapshot, transaction logs
* Delta updates
* Specify backup retention time
### Manual
* Full Storage volume snapshots
## Instances
* Can contain multiple DBs
### Instance class
* CPU
* Memory
* Network performance
### Instance storage
* HDD
* SSD
* Provisioned IOPS
### Software
* MySQL
* MariaDB
* Postgres
* Amazon Aurora
* Microsoft SQL
* Oracle
## Replication
* Deploy in Multi-AZ configuration
    * Automatically generate a standby copy of the instance
    * App in both AZs spreak to primary DB
    * Transactions replicated to standby in sync
* Enhanced availability during maintenance
* Protect against DB failure and AZ disruptions
### Failover
* Standby automatically starts if primary goes down
* RDS DNS Endpoint
    * Reroutes to standby seamlessly
    * Applications reference DB by name
* No need to change application code
### Read Replicas
* Async replication to replica
    * NOT MS or Oracle
* Offload read queries to replica 
* Can promote replica to primary
* Scale beyond capacity of one instance
* Can be in another region
    * Disaster recovery
    * Latency improvements
## Scaling 
* Change instance class (downtime)
* Scale storage in existing instance
* Read replicas
## Deep Dive
### Basic Use Case
* Complex transactions and queries
* High Durability
### DO NOT USE
* Simple GET and PUT requests
* Queries a NoSQL DB can handle
    * DynamoDB
* Customized DBMS
    * Run your own on EC2
### Best Practices
* Enable auto backups
* Test failover for multi-AZ deployments
    * Check time it takes
    * Check app connects
## More Use Cases
### Webapps
* High throughput
* Huge storage scalability
* High availability
### Ecommerce apps
* Low cost
* Data security
* Fully managed
### Games
* Rapidly grow capacity
* Autoscaling
* DB monitoring
## CLI Commands
### Create snapshot
```
aws rds copy-db-snapshot --source-db-snapshot-identifier mydbsnapshot --target-db-snapshot-identifier mydbsnapshot-copy --copy-tags
```
### Restore snapshot
```
aws rds create-db-snapshot --db-instance-identifier mytestdb --db-snapshot-identifier mydbsnapshot
```
#### Restored snapshots must be added to the security group


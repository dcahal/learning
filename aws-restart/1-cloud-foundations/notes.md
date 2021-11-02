CloudWatch will not monitor memory by default. Needs a custom rule.
Kinesis show you product popularity changing in real time.
S3 is global. Stays up when your VPC and AZ are down.
Autoscale: EC2, ECS, DynamoDB, Aurora
EBS is 1:1, EFS is 1:1000
10 EFS per acccount
AWS Storage Gateway: Volume, File, Tape
DB: Transactional vs Analytiical
RDS is OLTP: online transaction processing
    Cross-AZ replication
Aurora: Structured with multi-AZ data store. Serverless option
    Two copies of data in each AZ (minimum 3).
    5x faster than MySQL. 3x faster than Postgres
    Proprietary "MySQL and Postgres in one"
    Import from MySQL
    Cross-Region replication
DynamoDB: NoSQL
    Global Tables: Cross-Region replication
    Automatic main (master) replication - WRITABLE
    Conflicts can arise if applications update the same item in different Regions at about the same time. 
ElastiCache: Fully managed Redis and Memcached
    Popular in-memory data stores
    improve latency & throughput for read-heavy and compute
    OLAP
Redis: Persistent, single-threaded, Multi-AZ
Memcache: Not persistent, multi-threaded, no multi-AZ
Redshift: Managed data warehouse. SQL, OLAP. Data lake

---
> Kahoot
Shield Advanced is a PAID service. Shield Standard is free.
ALL LOGS ARE ENCRYPTED BY DEFAULT, such as CloudTrail
---


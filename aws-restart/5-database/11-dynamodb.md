# DynamoDB
* Fully managed NoSQL
* Redundant data storage
    * Multiple DC in Region
    * Fault-tolerant architecture
* Auto partition data
## Benefits
* Fully managed
* Low latency queries
    * >10 ms
* Data as JSON
    * Store, queue, update
* Fine-grained access control
* Flexibility
    * User permissions with IAM
## Understanding DynamoDB
* Some tables have billions of items
* Items in same table can have different attributes
    * No need for scheme migrations
    * New data format and old format can exist side by side
* Provision needed I/O throughput
* Autoscaling
### Global Tables
* Auto replication across regions
### Optional
* Encryption at rest
* Item time-to-live (TTL)
## NoSQL Concepts
* Tables with zero or more items
### Item
* Group of attributes (1+)
* Unique among items
### Attribute
* Fundaental data element
* Can't break down further
    * First name
    * Last name
    * Phone number
### Schemaless
* Attributes do NOT need to be defined beforehand
    * Nor their data types
* Items can have their own
## Global Tables
* Table(s) owned by one account
    * Replica tables
* One replica per region
* Same table name
* Same primary key
* Propagates ongoing changes
### Use case
* Large scale app
* Global audience
* Maintain availibility
## NoSQL Concepts: Keys
* Primary Key: two types
    * Uniquely identifies each item in table
### Partition Key
* Simple primary key
* One attribute
### Composite Key
* Primary key with two attributes
    * Combination of these two must be unique in table
    * Both must exist
* Partition key
    * *Hash value*
    * Creates unordered index of items
* Sort key
    * To store all items with same partition key close together
    * Orders them physically on the partition
## How It Works
### Partitions
* Data stored here on SSDs
* Multi-AZ replication
* One region
### Storage and Retrieval
* Based on partition key value
### Writes
* Partition key value is input to hash function
* Output determines which partition stores item
### Reads
* Partition key value is input to hash function
* Output tells partition location
## Partitioning
* Table partitioned and indexed by primary key as it grows
### Retrieval
#### Query
    * Uses PK and partitons to effectively locate items
#### Scan
    * Locate items by matching non-key attributes
    * Scans all items in the table
    * Flexible, inefficient


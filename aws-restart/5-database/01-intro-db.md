# Intro to Databases
* Data organized into tables
## Data Models
* Logical structures of DB
* Determines how data is stored and organized
### Relational model
* Based on relational algebra
* Improves bulk data handling
* Fields = columns
* Records = rows
## Relational DB
* Predefined relationship between items
* Rigid schema
* SQL — structured query language
* Data in multiple tables
* Run transactional or analytical queries
* Fields provide quick naviation to particular record
* Scales vertically (add resources on system)
## NoSQL DB
* No table structure
* Built to purpose for specific data models
* Relaxed restrictions on data consistency
* Scales horizontally (add systems)
### Optimized for:
* Large data volumes
* Low Latency
* Flexible data models
    * Graph
    * Document
    * Key-value
## Use cases
### Relational
* Traditional applications
* Enterprise resource planning (ERP)
* Customer relationship management (CRM)
### Key-value
* High traffic web apps
* Gaming
* E-commerce systems
### In-memory
* Caching
* Session management
* Geospatial applications
* Gaming leaderboards
### Document
* Industrial applications
* Equipment maintenance
* Fleet management
* Route optimization
## DBMS — Database Management System
* DB software or DBaaS
* Single user access
    * Microsoft Access
* Multiuser access
    * Oracle DB
    * MySQL
## DBaaS
* Hosted by third party
    * On VM
    * As cloud platform service
* Fully managed
    * Provisioning, patching, configuration, backup, recovery
* Cheaper
* Faster
    * Large data sets
    * Server region, latency
## Data Interaction
### Direct
* Entering SQL commands to make changes on server
* User required to know how to issue command in their DBMS
### Client-server
* Client applications use SQL to request data
### Embeded in application
* SQL statements in app source code (e.g. Java)
* App performs database tasks
* End user doesn't know SQL
### Three-Tier WebApp
#### Presentation tier
* Static content
* Browser requests web page
* Web server displays data output
#### Application tier
* Static content
* Web server receives request from application and DB servers
#### Data tier
* Dynamic content
* Database server
## Data Lake
* Centralized repository
* Unstructured
* Stores, manages, distributes all data in the org
    * All data which is created, stored, or operated on
### "Cloud memory bank"
* Analytics
* Dashboards
* Visualizations
* Big Data
* Real-time analytics
* Machine learning
* On prem data movement

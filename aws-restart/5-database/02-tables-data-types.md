# Tables and Data Types
## Relational DB
### Database
* Collection of data structured to enable useful tasks
### Tables
* Collection of related info about particular concept
### Records
* Rows
* Information for one entity in table
### Fields, Attributes, Columns
* Columns
    * One for each type of information
* Field
    * Stores value of an attribute
## SQL
* For querying and manipulating data
* Defining structure in databases
* Creating tables
* Implementing data types
* Sublanguages: SQL statement groups of actions
### Data manipulation language (DML)
* View, change, manipulate data
* Used by Data analysts, app developers
#### Commands
* `SELECT`
    * Fetch data from table
* `UPDATE`
    * Modify rows
* `INSERT`
    * Add rows
* `DELETE`
    * Delete rows
### Data definition language (DDL)
* Creates and defines DB and objects
* Used by DB admins and programmers
#### Commands
* `CREATE`
    * Creates DB or table
* `DROP`
    * Deletes object (table, constraint)
* `ALTER TABLE`
    * Add, del, modify columns
    * Add, del constraints
### Data control language (DCL)
* Controls access to data in DB
* Used by DB admins and programmers
#### Commands
* `REVOKE`
    * Revoke user permissions
* `GRANT`
    * Grants permissions to user
## Data Types
* Used to manipulate data in DB
* Determines
    * Storage format
    * Data's values
    * Data's operations
### Predefined
* Built-in data types
### Constructed
* Specified using constructors of a SQL data type
### User-defined
* Defined by a standard
### Proprietary
* DBMS additional data types
* Not standard SQL
* Not portable
## Identifiers
* Items user creates
* NOT language statements or keywords
### Capitalization
* In AWS re/Start, use lower case
* IBM and Oracle convert to upper case
    * "" to retain case
* MySQL is case sensitive
## Numeric Data Types
* `INTEGER`
    * Identify the smallest range you need
    * Don't over-allocate
    * `SMALLINT`: Different range? DBMS dependent
    * `BIGINT`: Different range? DBMS dependent
* `DECIMAL`(p,s)
    * Exact numeric (not binary)
    * precision,scale
    * p = total digits
    * s = digits after decimal point
* `NUMERIC`(p,s)
    * Identical to `DECIMAL` in Postgres and MySQL
    * Exact numeric (not binary)
    * Strict type
    * Max precision depends on DBMS
* `FLOAT`(p)
* `REAL`
    * Like `FLOAT` but DBMS defines precision
#### Use DECIMAL for money
* Use exact numerics for money
* Binaries like `FLOAT` or `REAL` for scientific calc
    * Stored more efficiently
    * Processed faster than `DECIMAL`
* Some DBMS have money types (MySQL)
## Date and Time
* `DATE`
    * YYYY-MM-DD
* `TIME`
    * hh:mm:ss
* `TIMESTAMP`
    * Date and time
* `INTERVAL`
    * 
## Character string
* `CHAR`
    * Fixed length character string
    * Must be single quoted ''
* `VARCHAR`
    * Variable length
    * Max length fixed
* `CLOB`
    * Character Large Object
    * Collection of character data
    * Often stored in separate location and referenced in table
### Use
* Understand how text storage is allocated in your system
* Fixed length for consistent items like zip code or phone number
* Make sure variable length columns are not wider than needed
## Keywords and Identifiers
* Keywords are built-ins with predefined data types
    * SELECT, GRANT, DELETE, CREATE
* Identifiers are names for DB objects or items
    * Tables, columns, aliases, indexes, views
## Constraints
* Rule limiting the type of data that can go in a table
* Enforces reliability of DB
* Declared at table creation
* `UNIQUE`
    * The column uniquely identifies each row
* `NOT NULL`
    * Ensures no null values across all rows
* `DEFAULT`
    * If undefined, a value is provided when recorded inserted
* Required
    * Row cannot be saved until valid value in column
* No duplicates
    * Row cannot be saved if column value is identical on another row
    * Often set alongside setting index on column
## Primary Keys and Foreign Keys
### Primary Key
* Column with unique value for each row
* Usually numeric
### Foreign Key
* Column with primary key from another table
### PK automatic constraints
* Depends on DBMS
* Define input mask (aka picture)
    * Guides user
    * Ensures consistent values
    * Enforce format (dashes in correct places)
* Prohibit editing after entry
## Tables
* Purposeful names (identifiers)
* Verify names with `IF NOT EXISTS`
### Example
```sql
CREATE TABLE employees (
 employee_id INTEGER NOT NULL PRIMARY KEY,
 first_name varchar(20) DEFAULT NULL,
 last_name varchar(25) NOT NULL,
 dept_id INTEGER NOT NULL
);
```
Named fields are columns
### Columns
* Each has data type
* Each has max length
* When adding, separate with space and comma
### Referential integrity
* Every non-null FK value matches an existing PK value

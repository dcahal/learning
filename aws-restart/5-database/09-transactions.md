# Transactions and Tables
* Database Transaction
* Reproduction of changes performed on a database
## Transactions
* Run complete set of operations
    * DB never contains result of partial operations
* Denote any alteration in DB
* Will never complete unless each operation successful
### Enables
* Isolation between programs accessing DB simultaneously
* DB never tainted with partial operations
* Restored to original state if any operation fails
## ACID
### Atomicity
* All changes successfully complete
### Consistency
* Changes will not violate integrity of DB or constraints
### Isolation
* No interference with other transactions
### Durability
* Interruption to availability does not impact consistency
## Keywords
* `START TRANSACTION`
* `ROLLBACK`
    * Undo anything since `START TRANSACTION`
* `COMMIT`
    * **Not tracked**
* `DROP TABLE`
### DELETE and UPDATE
* Apply to expressions
* Carefully verify output
## Database Anomalies
* May occur when DB changes
### Insertion anomaly
* Cannot insert data because other data is missing
* Can't add customer info for customer with no purchases
### Update anomaly
* Data stored redundantly in same table
* Hard to ensure all copies of a value are updated when changed
### Deletion anomaly
* Accidentally deleted needed info alongside unwanted
### Good Design
* Clear
* Essential
* Cooperative
* Efficient
* Precide
* Flexible
* Reusable


# Inserting Data
* `INSERT INTO`
* Insert records into a table
* Add new data to DB
* DML command — data manipulation language
* Order of columns is important when selecting
### Example
```sql
INSERT INTO tableName (col_1,col_2,col_3...col_n)
VALUES ("val_1","val_2","val_3","val_n");
```
* When inserting row, Must specify column where data will go
* Data added to all columns if none specified
    * Adds a row
* Single quote character and date values
### DESCRIBE
* Description of table or view
## NULL value
```sql
INSERT INTO tableName(col_1) values(NULL);
```
* Inserts NULL value into column
* Can insert into int column
### About NULL
* RDBMS is all about optional columns
* No value exists for the field
* null -ne null
* NULL in column with NOT NULL condition will throw error
## Import CSV
* Check CSV has data matching columns and data types in table
* Create table with same name as CSV
### Importing
* Ignore first row of CSV with `\n`
    * These are column headings, not identifiers
* Create new CSV without column headers. Replace empty strings with `\n` (NULL)
### Example
```sql
LOAD DATA INFILE '/tmp/loyalty.csv' INTO TABLE loyalty
FIELDS TERMINATED BY ' , ' ENCLOSED BY ' " '
LINES TERMINATED BY '\n' IGNORE 1 ROWS;
```
## Cleaning Data
* LEFT, RIGHT, TRIM, CONCAT
* LOWER, UPPER

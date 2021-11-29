# Selecting Data
## SELECT and FROM
* Access subset of rows, columns, both
* `FROM` specific table
### Example
```sql
SELECT family_name, given_name, dept_id FROM table_employees;
```
```sql
SELECT custname, address
FROM Customers;
```
### Clauses
* `WHERE`
    * Only certain rows
* `GROUP BY`
    * Groups result set using column ientifier
* `HAVING`
    * Use with GROUP BY. Which groups in results
* `ORDER BY`
    * Sort results by one or more columns. Asc or desc
### WHERE
```sql
SELECT custname, city, state
FROM Customers
WHERE state = 'NY'
```
## SQL syntax
* Brackets [] enclose optional parameters
* Specify at least 1 column or use * for all
```sql
SELECT col1[, col2, col3 ...] FROM table
```
* Queries are case sensitive
* Must match names in DB
* Delimiters are space or line break
* Limit table, column, index names to 30 characters
## Comments
```sql
-- Display the table structure
DESCRIBE Titles

SELECT custname, state -- not city
/* FROM Customers
WHERE city = 'Rochester' */
```
* Single line
* Inline
* Multi-line

# Built-in Functions
## Function Types
### Aggregate
* Use columns with multiple rows
* Return a number based on those
### Conversion
* Single row functions for typecasting
### Date
* Return the date
* Add/subtract date items
### String
* Manipulate string
* Query info about string
### Math
* To do math
### Control flow
* Provide logic to functions
### Window
* Perform calculations against partitions
## Date
```sql
SELECT bktitle , 
DATE_ADD(pubdate, INTERVAL 3 MONTH) AS new_date , 
TIMESTAMPDIFF(YEAR, pubdate, '2017-12-31') AS diff_date
FROM titles
```
### Nested functions
```sql
TIMESTAMPDIFF(YEAR, pubdate, NOW())
```
* NOW is an input argument
* How many years since book published, based on current year NOW
## Aggregate
* `COUNT`
* `AVG`
* `SUM`
    * Returns null in SELECT with no matching row
    * Ignores null values
    * `DISTINCT` for sum of non-duplicate values
* `MIN`
* `MAX`
* `DISTINCT`
    * No duplicate rows
#### Do not use keywords outside their context
## Strings
* Enclosed in single quotes
* Can't be used in math
* Case matched during compilation
### String functions
* `LEN`
* `UPPER`
* `LOWER`
* `TRIM`
    * `LTRIM`
    * `RTRIM`
* `SUBSTRING`
    * `(in, 1, 5)`
    * Input field
    * Starting character from 1
    * How many characters to print
* `CONCAT`
    * `(A, B)`
    * Includes white space
#### SUBSTRING
```sql
SUBSTRING('New York', 5, 4)
```
Returns `York`

# Conditional Search
## Search Condition
* Logical test applied to each row
* Two value expressions and operator
* Math operators work
### are Parameters used with:
* clauses
* expressions
* any DML statement
* some DDL statements
## Math Operators
* `+`, `-`,`*`,`/`,`%`
## Comparison Operators
* `=`, `!=`, `>`, `<`
* `<>` is same as `!=`
## Logical Operators
* `ALL`
    * True if all true
* `AND`
    * True if both bools true
* `OR`
    * True if either bool true
* `ANY`
    * True if one true
* `SOME`
    * True if multi true
* `BETWEEN`
    * True if in range
* `EXISTS`
    * True if contains any rows
* `IN`
    * True if equals one of a list
    * List syntax: `('CA' , 'NY , 'MA')`
* `LIKE`
    * True if pattern matched
* `NOT`
    * Inverts return of other logical operators
## Use in WHERE
### Multiple operators
### Parentheses
```sql
WHERE (state = 'NY' OR state = 'MA') AND repid = 'S01'
```
### Lists
```sql
WHERE state IN ('CA' , 'NY , 'MA')
```
## Aliases
* Provide query results with new column headers
* Different column names from original DB
```sql
SELECT col_name AS new_name
```
```sql
SELECT bktitle, slprice + slprice * .05 AS newprice
```
* Makes column easier to read
* Self-documenting
### Ways to alias
* AS
* omit AS
* Single quote multiple words
* Alias = expression
```sql
SELECT bktitle, newprice = slprice + slprice * .05
```
## NULL
* Missing value
* Two NULLs not equal
* NULL rows omitted from comparative search
    * Use `IS NULL` and `IS NOT NULL`
## Pattern Matching
* `LIKE '%string%'`
### SQL Wildcards
* Used with `WHERE` and `LIKE`
* Multiple allowed
* `%`
    * Substitute 1+ character in field
* `_`
    * Substitute one character in syntax expression
### REGEXP
* `WHERE column REGEXP 'expression'`
* BRE and ERE only
### lowerof() and upperof()
* `lowerof(column)`
* In `SELECT`
    * Print results in all lower or upper case
* In `WHERE`
    * Changes case sensitivity of pattern match

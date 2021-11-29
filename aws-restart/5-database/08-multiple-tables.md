# Getting Data from Multiple Tables
## Set operations
* Allow multiple rows from different tables compared or joined
### UNION
* Two+ SELECT statements into single result
* Excludes duplicates by default
* `UNION ALL` shows duplicates
#### SELECT requirements
* Number of columns must match
* Compatible data types
* No dupe column names
## Joins
* Combine 2+ rows or fields from 2+ tables
### Qualified column name
* Table.column
* Easily define JOIN output
* Remove ambiguity
### Inner join
* Selects only matching data in both tables
### Outer join
* Left
    * All Table 1 plus matching data in Table 2
* Right
    * All Table 2 plus matching data in Table 1
* Full
    * Merge tables regardless of condition
#### [Inner and Outer Joins][1]
### Self join
* Join a table to itself
* Compare a row in same table
* Alias same table twice
    * check1, check2
    * Repeating table name can cause error
* LEFT JOIN or INNER JOIN

[1]: https://www.educba.com/types-of-joins-in-sql/

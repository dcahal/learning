# Organizing Data
## ORDER
* `ORDER BY column ASC`
* `ORDER BY column DESC`
* Can take secondary column and sort
## PARTITION BY
* `PARTION BY column`
* Creates subset of rows based on argument
* Run calculation on partition
## Ranking
### RANK
* `RANK() OVER expression`
* Use on PARTITION
* Tie creates gap in ranking count
### DENSE RANK
* `DENSE_RANK` for no gaps
### ROW NUMBER
* `ROW_NUMBER() OVER expression`
* Use with ORDER BY
* Lists place in sequence
### NTILE
* `NTILE(i) OVER expression`
* Breaks results into approx equal groups
* Buckets
* Outputs lists bucket
## Truncating
* `SELECT TOP(i) PERCENT`
    * PERCENT optional
* `ORDER BY column DESC limit 10`
## Groups
* Combine rows into groups based on matching values
* Group results summarized in single row
* `GROUP BY column`
* After `WHERE`
* SELECT columns must be in GROUP BY
    * Only direct references
    * Not those subject to aggregating function
### HAVING
* Search within GROUP BY results
* Based on columns in SELECT
### WITH ROLLUP
* `GROUP BY columns WITH ROLLUP`
* Sorts output ranked by group name



# [Russ Olsen - Functional Programming in 40 Minutes](https://www.youtube.com/watch?v=0if71HOyVjY)


Functional programming is about "real" functions
    NOT procedures or subroutines

### Characteristics
* Look at input, return output
* Code outside the function doesn't matter

### 
**Problm:** Changes in input data structure
**Solutn:** Immutable, copy on modification

**Problm:** Copy efficiency
**Solutn:** Copy only modified node/element, retain the rest of the data

**Problm:** Side-effects from handling state changes
**Solutn:** Another function to handle changes in incoming data

**Problm:** Do actions to outside
**Solutn:** Send request to queue. Queue handles orderly execution of changes asked by all functions.

Good functional programming helps threading. Ensures one thread can't fetch garbbled data structure because another thread is updating it at the same time.

Codebase is majority functions with a sliver of interfaces.

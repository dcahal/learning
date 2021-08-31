## The file handle is NOT the file.
Treat this bridge as its own item.

## str.find is not grep
str.find returns the index of the first character where the matching pattern is found.
To get text after the match, you need to search after the character count of the pattern. Something like `line[found_line+6:]` for `pattern`.

## Global variables in functions
If any variable is assinged a value inside a function with `=`, `==`, or `is`, it will become local.
Any references to that name will use the currrent value of the global variable. The local variable will be shadowed outside of its function.

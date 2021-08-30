

## str.find is not grep
str.find returns the index of the first character where the matching pattern is found.
To get text after the match, you need to search after the character count of the pattern. Something like `line[found_line+6:]` for `pattern`.

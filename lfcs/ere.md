# ERE are not globs!

Extended regular expressions won't match if starting with `*`
Make sure to start a wildcard pattern with `.*`
To get the number of KDE Neon packages:
* `apt list | grep -e .*neon | wc` 

# File Access Control Lists

`+` at the end of `rwx` permissions line means extended ACL permissions.
* Not Posix
* Check with `getfacl`
* Set with `setfacl`

## Permissions issues? Check ACL

Use `ls -la` to check if your file or directory has a `+` and check it with `getfacl /path/`

## Reading ACL permissions

ACL permissions in the output of `getfacl` are:
* `mask`
* `default:user`
* `default:group`
* `default:mask`
* `default:other`

`effective` is the practical active permissions from mixing `setfacl` and `chmod` rules.

## Management

`chmod` can't alter the ACL even with root access. Likewise, `setfacl` does not override `chmod` settwings. They are two distinct rulesets and the `effective` permissions are the most restrictive combination of the two.

* **setfacl -bR**
* Delete all ACL rules under current location, recursively.

# Over the Wire: Bandit
## Numbered by logged in user
1. Didn't write it 
2. Didn't write it 
3. Didn't write it 
4. `grep -r [0-9]* .`
5. `find . -name "*" -size 1033c` OR `grep -r [0-9]* .`
6. `find / -user bandit7 -group bandit6 -size 33c`
7. `grep millionth data.txt`
8. `sort data.txt | uniq -u`
    * `sort -u file` is identical to `sort file | uniq`
9. `strings data.txt | grep ===`
10. `base64 -d data.txt`
11. `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
    * `tr 'A-Za-z' 'N-ZA-Mn-za-m'` is ROT13 encryption for alphabetic strings
    * The `tr` pattern signifies moving the beginning of the alphabet from `A` to `N`


### bandit12
```bash
xxd -r data.txt > data.tar.gz
gzip -d data.tar.gz
bunzip2 data.tar
mv data.tar.out data2.tar.gz
gzip -d data2.tar.gz
tar xvf data2.tar
tar xvf data5.bin
bunzip2 data6.bin
mv data6.bin.out data6.tar
tar xvf data6.tar
gzip -S .bin -d data8.bin
```
`gzip -d` and `gunzip` are interchangeable. Same for `bzip2 -d` and `bunzip2`. Streamline with `zcat`.

### bandit13
```bash
ssh -i sshkey.private bandit14@localhost
less /etc/bandit_pass/bandit14
```

### bandit14 
```bash
telnet localhost 30000
```

### bandit15 
```bash
openssl s_client -connect localhost:30001
```

### bandit16
```bash
nmap -A -T4 -p 31000-32000 localhost
openssl s_client -connect localhost:31790
```

### bandit17
`diff passwords.old passwords.new --color=always`

### bandit18
`ssh bandit18@bandit.labs.overthewire.org -p 2220 cat "~/readme"`

### bandit19
`./bandit20-do cat /etc/bandit_pass/bandit20`

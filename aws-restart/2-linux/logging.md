# Logging
* system
* events
* applications
* services

## Levels
0. EMERGENCY
    * when system becomes unstable
1. ALERT
    * when immediate action is needed
2. CRITICAL
    * system may become unstable
3. ERROR
4. WARN
    * typically default logging level
5. NOTICE
    * normal events of significant importance
6. INFO
7. DEBUG
    * debug messages + INFO

## /var/log
* `syslog`: system info
* `secure`: auth info on RHEL
* `auth.log`: auth info on Debian
* `kern`: kernel info on RHEL
* `auth.log`: auth info on Debian
* `boot.log`: startup messages
* `maillog`: mail messages
* `daemon.log`: running background services
* `cron.log`
* `httpd`: Apache messages on RHEL
* `dnf.log`
* `YUM`: old systems
* `apache2/access.log`: Apache auth info on Debian
* `lastlogin`: Binary holding info about successful logins to host
    * View with `lastlog` command
    * `lastlog -u user`
    * `lastlog -t 2`: logins within the past 2 days

## logrotate
Compress, rename, clean up log files
* Split logs based on size or time
* Automatic renaming
* Different policies for different logs

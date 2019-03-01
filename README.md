# IP Normalization

A quick script to bulk transform IP addresses into CIDR range. prints to `STDOUT`

usage:
   `./ipnorm.py IPFILE`

> notes : (1) prints to stdout. Redirect to file.  (2). makesure `netaddr` installed.

## Bulk insert

you can redirect IPFILE into file INST_ID.ips and use .bulkIps.sh to insert into mysql
please edit bulkIps before use and enter mysql user,pass, and host.

## TODO

 - [ ] move to virtualenv
 - [ ] clean up
 - [ ] update to python 3.x
 - [ ] create examples  
 - [ ] Update bulkIps.sh to use transaction

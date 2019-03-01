#!/bin/bash

#ADD IPS en masse
# uncomment and enter User, Pass, and Host below.
# TODO: use transaction
# Author: matthew g. roth <matthew.g.roth@yale.edu>
# usage: ./bulkIps.sh INST_ID.ips
# where INST_ID.ips are a list of cidr ranges per line
##

INFILE=$1.ips
instId=$1
#u=MYSQL_USER
#p=MYSQL_PASS
#h=MYSQL_HOST

addIP() {
  echo "ADD IPS: $INFILE"
  for cidr in $(cat $INFILE)
  do
    echo "ADDING $cidr"
    mysql -u$u -p$p -h$h ehraf -e "
      INSERT INTO tblnetworks 
      VALUES ($instId, aton_start($cidr), aton_end($cidr), $cidr, 'allow', is_current);" 
    
  done
}

addIP

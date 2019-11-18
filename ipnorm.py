#!/usr/bin/env python
import sys
import netaddr
import re

'''PIECES, CLEAN UP
######BUT, ITERATE NORMALIZE THROUGH FILES
####LOOK AT .addRussia.sh in ~/ @ hraf02
'''
def normalize(ip):
    if '/' in ip: 
        return [ip]
         
    ocets = [ocet.replace(' ','') for ocet in ip.split('.')]
    if len(ocets) == 4: ocets += ocets
    if len(ocets) == 7: 
        if (re.search('-',ocets[3])):
            for i,v in enumerate(ocets[3:]):
                if i == 0:
                    last = ocets[4]
                    ocets[3],ocets[4] = ocets[3].split('-')
                else:
                    if 4+i < len(ocets):
                        newVal = last
                        last = ocets[4+i]
                        ocets[4+i] = newVal
                    else: 
                        ocets.append(last)
             
    if len(ocets) != 8: 
        return 'ERROR WITH: %s not right size %d' % ('.'.join(ocets),len(ocets))
    for i,ocet in enumerate(ocets):
        #is *
        if (re.search('\*',ocet)): 
            ocets[i] = '0'
            ocets[i+4] = '255'        
        
        
        if (re.search('-',ocets[i])): 
            ocets[i],ocets[i+4] = ocets[i].split('-')[0:2]
    newIP = netaddr.iprange_to_cidrs('.'.join(ocets[0:4]) ,'.'.join(ocets[4:]))
    return newIP


def main():
    try:
        item = sys.argv[1]
    except:
        print('Usage: %s IPFILE' % (sys.argv[0]))
        sys.exit(1)
    f = open(sys.argv[1],'r+')
    print('\n\n\nIPS FROM %s' % (item))
    o = open(item + '.ips', 'w+')
    for line in f:
        x = normalize(line.strip())
        print("TRANSFORM %s to BECOME: " % (line.strip()))
        for i in x: 
            print(i)
            o.write(str(i) + '\n')
    o.close()
    f.close()


if __name__ == '__main__':
    main()

  
'''  
for item in os.listdir('.'):
    f = open(item,'r+')
    print('\n\n\nIPS FROM %s' % (item))
    o = open(item + '.ips', 'w+')
    for line in f:
        x = normalize(line.strip())
        print("TRANSFORM %s to BECOME: " % (line.strip()))
        for i in x: 
            print(i)
            o.write(str(i) + '\n')
    o.close()
    f.close()




for i,v in enumerate(x[3:]):
    if i == 0:
        last = x[4]
        x[3],x[4] = x[3].split('-')
    else:
        if 3+i < len(x):
            newVal = last
            last = x[4+i]
            x[4+i] = x
        else: 
            x.append(last)
'''
                      

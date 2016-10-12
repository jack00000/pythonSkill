#!/usr/bin/python #python导入python-nmap模块可以调用nmap的一些接口来实现一些nmap中的功能
# -*- coding: UTF-8 -*-

import optparse #
import nmap

def nmapScan(th,tp):
    #print 'see'
    nmScan=nmap.PortScanner()
    results=nmScan.scan(th,tp)
    state=results['scan'][th]['tcp'][int(tp)]['state']
    print ('[*]'+th+'tcp/'+tp+''+state)
def main():
    parser = optparse.OptionParser('usage %prog –H< targethost > -p < targetport > ')
    parser.add_option('-H', dest='th', type='string',
                      help='specify target host')
    parser.add_option('-p', dest='tp', type='int',
                      help='specify target port')
    (options, args) = parser.parse_args()
    th = options.th
    tp = options.tp
    print th
    print tp
    #args.append(tp)
    #print args
    if (th == None) or (tp == None):
        print('[-] You must specify a target host and port[s]!')
        exit(0)
    for a in args:
 	#print  'aa'
	nmapScan(th, a)
if __name__=='__main__':
    main()

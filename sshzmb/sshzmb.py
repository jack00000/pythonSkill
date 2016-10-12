# coding=UTF-8#利用pexpect模块的交互功能来实现自动化登录ssh然后可以利用自动化的过程猜解ssh密码也叫做ssh密码爆破ssh登录后可远程执行命令

import pexpect

PROMPT =['#','>>>','>','\$']#登陆成功后反馈期望即得到以上期望的反馈即认定登录成功


#发送命令并打印发送的命令
def send_cmd(child,cmd):
	child.sendline(cmd)
	child.expect(PROMPT)
	print child.before


#连接ssh匹配连接结果，判定是否连接成功
def conn(user,host,pwd):
	ssh_newkey = 'are you sure you want to continue connecting'
	connStr='ssh '+user+'@'+host
	child=pexpect.spawn(connStr)
	ret=child.expect([pexpect.TIMEOUT,ssh_newkey,'[P|p]assword:'])
	print ret
	if ret == 0:
		print('[-]Error Connecting')
		return
	if ret == 1:
		child.sendline('yes')
		ret=child.expect([pexpect.TIMEOUT,'[P|p]assword:'])
	if ret == 0:
		print('[-]Error Connecting')
		return child
	child.sendline(pwd)
	child.expect(PROMPT)
	return child
def main():
	host='127.0.0.1'
	user='root'
	pwd='123456'
	child=conn(user,host,pwd)
	send_cmd(child,'nmap -v')
if __name__ == '__main__':
	main()		

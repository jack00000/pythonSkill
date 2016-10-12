#-*- coding:utf-8 -*-#这个.py的目的是用字典破解zip文件的密码
import zipfile #导入zip压缩文件模块，这个包可以打开或者写入zip文件
import threading#线程模块
import optparse #参数模块
def crack(zfile,password):	#破解函数原理是从字典里穷举密码，如果密码出错
#会抛出异常如果正确直接返回密码
	try:
		zfile.extractall(pwd=password)
		print 'password is'+password#打印正确密码
		return password
	except:
		pass
def main():
	parser=optparse.OptionParser('usage%prog -f<zipfile>-d<dictionary>')
	parser.add_option('-f',dest='zname',type='string',help='zip文件相对路径或者绝对路径')
	parser.add_option('-d',dest='dname',type='string',help='字典文件路径')
	options,args=parser.parse_args()
	#print options.zname,options.dname
	if (options.zname==None)or(options.dname==None):
		print parser.usage
		exit(0)
	else:
		zname=options.zname
		dname=options.dname
	z=zipfile.ZipFile(zname)#打开要破解的压缩文件以供处理
	f=open(dname)#打开字典文件
	for pwd in f.readlines():#从字典里读取每一行密码
		pawd=pwd.strip('\n')#消除每行的换行符
		thd=threading.Thread(target=crack, args=(z, pawd))#新建进程对象
		thd.start()	#开启进程
#print crack(z,'123456')
if __name__=='__main__':
	main()

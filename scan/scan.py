# coding=UTF-8
import optparse
import socket


#设置socket 并扫描连接ip的端口
def connScan(th,tp):
	try:
		conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		conn.connect((th,tp))
		print '[+]%d/tcp open'%tp
		conn.close()
	except:
		print '[-]%d/tcp closed'%tp

#connScan(th,tp)
def portScan(th,tps):
	try:
		tgtIP=socket.gethostbyname(th)
	except:
		print '[-] %s unknown host'%th
		return
	try:
		tgtName=socket.gethostbyaddr(tgtIP)
		print '\n[+]Scan Results for :'+tgtName[0]
	except:
		print '\n[+]Scan Results for :'+tgtIP
	socket.setdefaulttimeout(1)
	for tp in tps:
		print 'Scaning port '+str(tp)
		connScan(th,int(tp))
#portScan('www.nchu.edu.cn',[80,443,3389,1433,23,445])
def main():
	#命令设置
	usage = 'usage:%prog -H <targethost> -P <targetport>'
	parser=optparse.OptionParser(usage=usage)
	parser.add_option('-H',dest='th',type='string',help='目标IP')
	parser.add_option('-P',dest='tp',type='int',help='目标端口')#这里的选项还没改
	options,args=parser.parse_args()
	if options.th==None or options.tp==None:
        	print parser.usage
	 	exit(0)
	else:
        	th=options.th
        	tp=options.tp
        	print th
        	print tp
	print args#这里会少掉一个参数例如：输入80、21、22只会扫描21、22会漏掉80
	portScan(th,args)#huiyouyixie qiguaidedongxi
if __name__=='__main__':
	main()

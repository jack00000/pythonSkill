#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import numpy as np
from matplotlib import pyplot as plt
tt=[]
pp=[]
rr=[]
hezhi2=[]
cishu1=[]
global  aa

def wri(data,aa):#写入数据data到aa文件里去
    f=open(aa,'wb')
    for i in data:
        f.write(i)
        f.write('\n')
    # f.write(data)
    f.close()
def rea(aa):#读取文件里的数据aa为文件名
    result = []
    f=open(aa,'r')
    for line in f.readlines():
        result.append(line.split(' '))
    f.close()
    return result

def getdata():#获取彩票往期数据
    url="http://trend.caipiao.163.com/gxkuai3/hezhi.html?selectDate=&beginPeriod=20170328001&endPeriod=20170405078"
    request=urllib2.urlopen(url)
    soup=BeautifulSoup(request,'html.parser')
    # print soup
    t=soup.find_all('tr',attrs={"data-period":True})#找到网页数据中的data-period数据
    p=soup.find_all('tr',attrs={"data-award":True})#找到网页数据中的data-award数据
    for j in t:
        pp.append(j.attrs['data-period'])
    for i in p:
        tt.append(i.attrs['data-award'])
    # aa = int(tt[1])
    # print tt

    wri(tt,'data-award.txt')
    wri(pp,'data-period.txt')
def hezhi(datafil):#计算和值，返回一个和值的list其中的值为整数
    hezhi = []
    hezhi1=[]#返回和值用
    hezhi=rea(datafil)
    for i in hezhi:
        hezhi1.append(int(i[0])+int(i[1])+int(i[2]))
    return hezhi1
    # print hezhi[1][1]

    #return soup.prettify()
def int2str(data):#整型转字符串
    dataret=[]
    for dataline in data:
        dataret.append(str(dataline))
    return dataret
def tongjicishu(data):#统计每个和值出现的次数
    cishu=[]
    for j in range(0,19,1):
        cishu.append(0)
        print
    for i in data:
        # print  i
        cishu[i]=cishu[i]+1
    return cishu
def yilouzhi(data):#计算最大遗漏值
    yilouzhi=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    flag=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    f=0
    for i in data:
        if f>flag[i]:
            if yilouzhi[i]<f-flag[i]:
                yilouzhi[i]=f-flag[i]
        f+=1
        flag[i]=f
    return yilouzhi

getdata()

hezhiint=hezhi('data-award.txt')
hezhistr=int2str(hezhiint)
# print yilouzhi(hezhiint)
wri(hezhistr,'hezhi.txt')
cishu1=tongjicishu(hezhiint)
# print cishu1
# print hezhiint[-1]
# # data = [5, 20, 15, 25, 10]
# print (cishu1[8]+cishu1[9]+cishu1[10]+cishu1[11]+cishu1[12]+cishu1[13])*100/821
#
plt.bar(range(len(cishu1)),cishu1)
plt.show()
# rr=rea('data-award.txt')
# print int(rr[1][1])
# print data
#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import io


# import re
# import requests
# url='https://image.baidu.com/'
# data=requests.get(url).text
# jpglist=re.findall('<img src="(.*?)" a',data,re.S)
# n=1
# for each in jpglist:
#     print(each)
#     try:
#         pic=requests.get(each,timeout=10)
#     except:
#         print("下载失败！")
#         continue
#     stri='pic\\'+str(n)+'.jpg'
#     fp=open(stri,'wb')
#     fp.write(pic.content)
#     fp.close()
#     n+=1



# import re
# from urllib import request
# url='https://www.google.com/search?biw=1920&bih=937&tbm=isch&sa=1&ei=61lSXdemHJO6_wSC1r7QAg&q=nose&oq=nose&gs_l=img.3..0l10.2360.2772..4404...0.0..0.461.1367.2-2j1j1......0....1..gws-wiz-img.2GcKAAZNLYU&ved=0ahUKEwiXyMSknf_jAhUT3Z8KHQKrDyoQ4dUDCAY&uact=5'
# url_request=request.Request(url)
# url_response=request.urlopen(url_request)
# data=url_response.read().decode('utf-8')
# jpglist=re.findall('http.+?.jpg',data)
# n=1
# for each in jpglist:
#     print(each)
#     try:
#         request.urlretrieve(each,'pic\\%s.jpg',n)
#     except Exception as e:
#         print(e)
#     finally:
#         print('success downloding %s',n)
#     n+=1

 

# from urllib import request
# import re   #使用正则表达式
# import sys
# def getResponse(url):
#     url_request = request.Request(url)
#     url_response = request.urlopen(url_request)
#     return url_response   
# def getJpg(data):
#     jpglist = re.findall(r'src="http.+?.jpg"',data)
#     return  jpglist
# def downLoad(jpgUrl,n):
#     try:
#         request.urlretrieve(jpgUrl,'pic\\%s.jpg'  %n)   
#     except Exception as e:
#         print(e)
#     finally:
#         print('图片%s下载操作完成' % n)
# http_response = getResponse("http://dzh.mop.com/") 
# data = http_response.read().decode('utf-8')
# global n 
# n = 1
# L = getJpg(data)
# for jpginfo in L:
#     print(jpginfo)
#     s = re.findall(r'http.+?.jpg',jpginfo)
#     downLoad(s[0],n)
#     n= n +1


#!-*- coding:utf-8 -*-
#FileName : img.py
#Author : CSDN_fzs
#Data : 2018/01/10
 
import re #导入正则表达式模块
import requests #python HTTP客户端 编写爬虫和测试服务器经常用到的模块
import random #随机生成一个数，范围[0,1]
 
#定义函数方法
def spiderPic(html,keyword):
    print('正在查找 ' + keyword +' 对应的图片,下载中，请稍后......')
    for addr in re.findall('"objURL":"(.*?)"',html,re.S):     #查找URL
        print('正在爬取URL地址：'+str(addr)[0:30]+'...')  #爬取的地址长度超过30时，用'...'代替后面的内容
 
        try:
            pics = requests.get(addr,timeout=10)  #请求URL时间（最大10秒）
        except requests.exceptions.ConnectionError:
            print('您当前请求的URL地址出现错误')
            continue
 
        fq = open('E:\\Visual_code\\tongue_trainer\\negdata2\\' + (keyword+'_'+str(random.randrange(0,10000,4))+'.jpg'),'wb')     #下载图片，并保存和命名
        fq.write(pics.content)
        fq.close()
 
#python的主方法
if __name__ == '__main__':
    word = input('请输入你要搜索的图片关键字：')
    result = requests.get('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=' + word)
 
#调用函数
spiderPic(result.text,word)
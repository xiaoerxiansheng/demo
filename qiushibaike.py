# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:16:49 2019

@author: Lenovo
"""
import urllib.request as r
url='https://www.qiushibaike.com/'
#headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
req = r.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'})
data = r.urlopen(req).read().decode('utf-8')

url='https://pic.qiushibaike.com/system/pictures/12168/121680077/medium/G942QSKPL1ENZ02V.jpg'
r.urlretrieve(url,'a.jpg')






import urllib.request as r
url='https://www.qiushibaike.com/text/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
req = r.Request(url,headers=headers)
data = r.urlopen(req).read().decode('utf-8')



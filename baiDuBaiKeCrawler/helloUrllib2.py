#coding:utf-8
import urllib2, cookielib
#网页下载器

url = r'https://baike.baidu.com/item/Python'

print '第一种方法'
#直接请求
response1 = urllib2.urlopen(url)
#获取状态码，如果是200表示获取成功
print response1.getcode()
#读取内容
cont = response1.read()
print len(cont)

print '第二种方法'
#创建Request对象
request = urllib2.Request(url)
#添加数据
# request.add_data('a', '2')
#添加http的header
request.add_header('User-Agent', 'Mozilla/5.0') #伪装成浏览器
#发送请求获取结果
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print '第三种方法'#需要用户登录；需要代理；HTTPS
#创建cookie容器
cj = cookielib.CookieJar()
#创建1个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#给urllib2安装opener
urllib2.install_opener(opener)
#使用带有cookie的urllib2访问网页
response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
print response3.read()
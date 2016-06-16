#使用Cookie登录网站
import json
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import urllib

'''
cookielib模块的主要作用是提供可存储cookie的对象，以便于与urllib2模块配合使用来访问Internet资源。
Cookielib模块非常强大，我们可以利用本模块的CookieJar类的对象来捕获cookie并在后续连接请求时重新发送，
比如可以实现模拟登录功能。该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。
它们的关系：CookieJar —-派生—->FileCookieJar —-派生—–>MozillaCookieJar和LWPCookieJar
'''


'''
#获取cookie保存到变量
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib.request.HTTPCookieProcessor(cookie)
#通过hander来构建opener
opener=urllib.request.build_opener(handler)

response = opener.open('http://www.baidu.com')
for item in cookie:
	print('Name='+item.name)
	print('Value='+item.value)
'''

'''
#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib.request.build_opener(handler)
#创建一个请求，原理同urllib2的urlopen
response = opener.open("http://www.baidu.com")
#保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)

#ignore_discard的意思是即使cookies将被丢弃也将它保存下来，
#ignore_expires的意思是如果cookies已经过期也将它保存并且文件已存在时将覆盖，在这里，
#我们将这两个全部设置为True。运行之后，cookies将被保存到cookie.txt文件中，
'''

'''
#从文件中获取Cookie并访问
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
req=urllib.request.Request("https://passport.baidu.com/center")
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
response = opener.open(req)
print(response.read().decode('utf-8'))
'''

#利用cookie模拟登录网站 百度
filename='cookie.txt'
cookie=cookielib.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
postdata=urllib.parse.urlencode({
			'userName':'F_L___y',
			'password':''
	})
postdata = postdata.encode('utf-8')  
loginUrl='https://passport.baidu.com'

result=opener.open(loginUrl,postdata)
#print(result.read())
cookie.save(ignore_discard=True,ignore_expires=True)
url='https://passport.baidu.com/center?_t=1465636330'
r = opener.open(url)
print(r.read().decode('utf-8'))
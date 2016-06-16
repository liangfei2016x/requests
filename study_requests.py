import requests
import json
#get请求
r1 =requests.get('https://api.github.com/events')
#post请求
r2 = requests.post('http://httpbin.org/post',data={'key':'value'})
#在URL中传递参数
payload = {'key1':'value1','key2':'value2'}
r3 = requests.get('http://httpbin.org/get',params=payload)
print(r3.url)#http://httpbin.org/get?key1=value1&key2=value2

#读取响应内容
r4 = requests.get('https://api.github.com/events')
#Requests会自动解码来自服务器的内容。大多数unicode字符集都能被无缝地解码。
#请求发出后，Requests会基于HTTP头部对响应的编码作出有根据的推测。当你访问r.text 之时，
#Requests会使用其推测的文本编码。你可以找出Requests使用了什么编码，并且能够使用 
#r.encoding 属性来改变它:
a = r4.text
#r4的编码类型
b=r4.encoding
print(b)

#读取二进制请求响应
c = r4.content
#Requests会自动为你解码 gzip 和 deflate 传输编码的响应数据。
#例如，以请求返回的二进制数据创建一张图片，你可以使用如下代码:
from PIL import Image
from io import StringIO
i=Image.open(StringIO(r4.content))
print(c)

#Requests中也有一个内置的JSON解码器，助你处理JSON数据:
d = r4.json()
print(d)
#在罕见的情况下你可能想获取来自服务器的原始套接字响应，那么你可以访问 r.raw 。 
#如果你确实想这么干，那请你确保在初始请求中设置了 stream=True 。具体的你可以这么做:
r5=requests.get('https://github.com/timeline.json',stream=True)
r5.raw
#<requests.packages.urllib3.response.HTTPResponse object at 0x101194810>
r.raw.read(10)
#'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'

#定制表头 这个非常有用!!!!!!!!
url = 'https://api.github.com/some/enpoint'
payload={'some:data'}
headers={'content-type':'application/json'}

r6 = requests.post(url,data=json.dumps(payload),headers=headers)

#复杂的POST请求

#通常，你想要发送一些编码为表单形式的数据—非常像一个HTML表单。 要实现这个，
#只需简单地传递一个字典给 data 参数。你的数据字典 在发出请求时会自动编码为表单形式:
paylod = {'key1':'value1','key2':'value2'}
r = requests.post("http://httpbin.org/post",data=payload)

print(r.text)
'''{
  ...
  "form": {
    "key2": "value2",
    "key1": "value1"
  },
  ...
}'''
#很多时候你想要发送的数据并非编码为表单形式的。如果你传递一个 string 而不是一个dict ，
#那么数据会被直接发布出去。例如，Github API v3接受编码为JSON的POST/PATCH数据:

url = 'https://github.com/some/endpoint'
payload = {'some':'data'}

r7 =requests.post(url,data=json.dumps(payload))

#POST一个多部分编码(Multipart-Encoded)的文件

#Requests使得上传多部分编码文件变得很简单:
url = 'http://httpbin.org/post'
files = {'file':open('report.xls'),'rb'}

#也可以显示的设置文件名
#files ={'file':('report.xls',open('report.xls,','rb'))}

#如果你想，你也可以发送作为文件来接收的字符串:
#files ={'file':('report.csv','some , data, to send\nother,row,to,send\n')}

r8 = requests.post(url,files=files)
r8.text
'''{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}'''

#响应状态码
r9 = requests.get('http:http://httpbin.org/get')
r9.status_code#200
#为方便引用，Requests还附带了一个内置的状态码查询对象:
r9.status_code == requests.code.ok
#如果发送了一个失败请求(非200响应)，我们可以通过 Response.raise_for_status() 来抛出异常:
r9.rasie_for_status()
#但是，由于我们的例子中 r 的 status_code 是 200 ，当我们调用 raise_for_status() 时，得到的是:
r.raise_for_status()#None

响应头

#查看以一个Python字典形式展示的服务器响应头
r10.headers
'''{
	'status': '200 OK',
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json; charset=utf-8'
}'''
#对大小写不敏感我们可以这样访问响应头
r10.headers['content-type']
#也可以这样
r10.headers['content-type']
#不存在的响应头返回NonSe
r10.headers['x-type']

Cookies
#如果某个响应中包含一些Cookie，你可以快速访问它们:
url='http:example.com/some/cokie/setting/url'
r11 = requests.get(url)

r11.cookies['example_cookie_name']
#要想发送你的cookies到服务器，可以使用cookies参数:
url = 'http:http://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r12 = requests.get(url,cookies=cookies)
r12.text

#重定向与请求历史
#使用GET或OPTIONS时，Requests会自动处理位置重定向。
#Github将所有的HTTP请求重定向到HTTPS。可以使用响应对象的 history 方法来追踪重定向。
r13 = requests.get('http://github.com')
#可以禁用重定向
#r13 = request2.get('http://github.com',allow_redirects=False)
#如果你使用的是POST，PUT，PATCH，DELETE或HEAD，你也可以启用重定向
#allow_redicts=Ture
r13.history

超时

#你可以告诉requests在经过以 timeout 参数设定的秒数时间之后停止等待响应:
r14 = requests.get('http://github.com',timeout=0.1)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)
'''
#错误与异常
#遇到网络问题（如：DNS查询失败、拒绝连接等）时，Requests会抛出一个ConnectionError 异常。
#遇到罕见的无效HTTP响应时，Requests则会抛出一个 HTTPError 异常。
#若请求超时，则抛出一个 Timeout 异常。
#若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。
#所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException 。

#参考资料:http://blog.csdn.net/iloveyin/article/details/21444613
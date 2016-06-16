#coding:utf-8
import requests
import json
aa="http://fanyi.youdao.com/openapi.do?keyfrom=zhilutianshi&key=293831118&type=data&doctype=json&version=1.1&q="
word = input("请输入要翻译的内容:")
payload = {'q':'value'}
payload['q'] = word.encode('utf-8')
url = aa + word
r = requests.get(url,params=payload).text
data = json.loads(r)
for x in data['translation']:
	print(x
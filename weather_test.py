import requests 
import json

url = r'http://wthrcdn.etouch.cn/weather_mini?citykey=101280601' 
#得到Json格式字符串
jsonStr = requests.get(url).text
#解码：把Json格式字符串解码转换成Python对象   json.loads()
print(type(jsonStr))
data = json.loads(jsonStr)
print(data)
weather = data["data"]
print("city:",weather["city"])
print("promot:",weather["ganmao"])
for x in weather["forecast"]:
	print(x["date"],x["type"],x["high"],x["low"],x["fengxiang"],x["fengli"])

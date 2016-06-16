import io
import sys    
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


import requests
from bs4 import BeautifulSoup
#分析
#MovieRankingHistory-rank-1 > div > div.txtbox > h3 > a
#MovieRankingHistory-rank-1 > div > div.picbox > a > img
#MovieRankingHistory-rank-1 > div > div.txtbox > b > p:nth-child(2) > a:nth-child(1)
#MovieRankingHistory-rank-1 > div > div.txtbox > b > p:nth-child(2)

url = 'http://movie.mtime.com/boxoffice/?area=global&type=MovieRankingHistory&category=all&page=0&display=list&timestamp=1465724537887&version=07bb781100018dd58eafc3b35d42686804c6df8d'
r = requests.get(url).text
soup = BeautifulSoup(r,'html.parser')
names = soup.select('dd > div > div.txtbox > h3 > a')
imgs = soup.select('dd > div > div.picbox > a > img')
actors = soup.select('dd > div > div.txtbox > b > p:nth-of-type(2)')

for name,actor,img in zip (names,actors,imgs):
	data={
	'name':name.get_text(),
	'img':img.get('src'),
	'arctor':actor.get_text()
	}
	print(data)

n=0
for img in imgs:
	imgUrl=img.get('src')
	with open("D://requests//picture/%s.jpg" % n,"wb") as jpg:	
		image=requests.get(imgUrl,stream=True).content
		jpg.write(image)
		n +=1
	jpg.close()

#参考：http://blog.itpub.net/29733787/viewspace-1460117/
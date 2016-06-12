import io
import sys    
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


import requests
from bs4 import BeautifulSoup

url = 'http://movie.mtime.com/boxoffice/?area=global&type=MovieRankingHistory&category=all&page=0&display=list&timestamp=1465724537887&version=07bb781100018dd58eafc3b35d42686804c6df8d'
r = requests.get(url).text
soup = BeautifulSoup(r,'lxml')
listUrl = ['#MovieRankingHistory-rank-{}'.format(str(i) for i in range(1,101))]
print(listUrl)
for url in listUrl:
	names = soup.select( url+'> div > div.txtbox > h3 > a')
	for name in names:
		print(name)
	print(names)

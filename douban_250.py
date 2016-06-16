import requests
from bs4 import BeautifulSoup
import io
import sys    
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


def get_index():
	#分析单个url
	#url="https://movie.douban.com/top250?start=0&filter="
	#写入文件
	with open('moive.txt', 'w') as f:
		urls=['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25)]
		headers={'User-Agent':'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'}
		for url in urls:
			r=requests.get(url,headers)
#分析单个名字的csspath
#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span:nth-child(1)
#content > div > div.article > ol > li:nth-child(1)
			soup=BeautifulSoup(r.text,'lxml')
			names=soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a > span:nth-of-type(1)')
			for name in names:
				name=name.get_text()
				print(name)	
				f.write(name+'\n')
		f.close()


#def get_allurl():
#	urls=['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25)]
#	for single_url in urls:
#		get_index(single_url)
get_index()

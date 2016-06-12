import requests
from bs4 import BeautifulSoup
import io
import sys    
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def get_index(url,data=None):
	url = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
	web_data =requests.get(url).text
	soup = BeautifulSoup(web_data,'lxml')
	titles = soup.select('div.property_title > a')
	imgs = soup.select('img[width="160"]')
	cates = soup.select('div.p13n_reasoning_v2')

	for title,img,cate in zip(titles,imgs,cates):
		data = {
			'title':title.get_text(),
			'img':img.get('src'),
			'cate':list(cate.stripped_strings),
		}
		print(data)

#用cookie登录。查询自己的信息
def get_mycate(): 
	myUrl='http://www.tripadvisor.cn/MemberProfile-a_uid.22BAC6BF933443C0E3BE5DA31CAB6B2D'
	headers={
		'User-Agent':'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
		'Cookie':'ServerPool=X; TAUnique=%1%enc%3AwOak2Km49Ibj0stptjnxerj65uGstEcgU%2Bn9L9uB4ubiJ6g91gwMNg%3D%3D; TASSK=enc%3AwZxJuk0O3k6xD1c84q6toaorUgnAz1gAzBMqgD9y73aH0eBg9U%2Bb%2FxYLYg89fjIC; _jzqy=1.1465698710.1465698710.1.jzqsr=baidu|jzqct=cn%2Etripadvisor%2Ecom.-; _jzqckmp=1; __gads=ID=6cc9e78694d41b3c:T=1465698800:S=ALNI_MbYW1pN1vHVPOt1ZoKq5vct9igVxQ; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.293917_163l2_163*RS.1; ki_u=f84af6ac-4a36-eb11-bbb8-39bb; ki_s=154790%3A3.0.0.0.2; TAAuth2=%1%3%3A7fb3576686df89d83176b319f3d7a912%3AADmnkaZBULHRJSQLRjKu5f98X8Ne30ytGLvafNX66C8e3pPwxrBWNYD6oYwVZa3JnlnYNjgm3cucyeg6p3qsrClHbZsLwGC44odoaLxoTV0LVntGTQcNxFXzzCbqU7cNd%2BD93CJyLEquPKk7jOR%2FTLfdsHxI0Pvo%2Fb9xnlYCK5EZFEn36LUK0%2FfFieg7%2B7iMpDFB0nQIalmabnhXmVkzvFg%3D; _jzqx=1.1465703373.1465713058.1.jzqsr=tripadvisor%2Ecn|jzqct=/attractions-g60763-activities-new_york_city_new_york%2Ehtml.-; TAReturnTo=%1%%2F; CM=%1%t4b-pc%2C%2C-1%7CRCPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CRCSess%2C%2C-1%7CHomeASess%2C4%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7C2016sticksess%2C%2C-1%7CCCPers%2C%2C-1%7CCpmPopunder_1%2C3%2C1465789872%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C3%2C-1%7Cb2bmcsess%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7C2016stickpers%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7Csess_rev%2C4%2C-1%7Csessamex%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CRBAPers%2C%2C-1%7C; _smt_uid=575cc996.518a008a; roybatty=ACmCI6AUEgLW4ZISbkI0iC5q8v17XCc%2F30uyf67KZKEltNv%2BCQc%2B3%2FzzEne0%2FzC%2B3CJ%2FkiWtsZHgwPe7J7H8rj%2BFvYJP82oboe%2Fc5Y5QyGYCeckiSTV95RqynqeaBrN9%2B0Am8eW49Ek7Okn5%2Bwl%2FWeWl2l7bhGeggOvXOgOvu6g0%2C1; NPID=; ki_t=1465698712118%3B1465698712118%3B1465714973958%3B1%3B19; ki_r=; _qzja=1.504538394.1465698710338.1465703372578.1465713057661.1465714918073.1465714973976..0.0.20.3; _qzjb=1.1465713057661.10.0.0.0; _qzjc=1; _qzjto=20.3.0; _jzqa=1.3606242541498277000.1465698710.1465703373.1465713058.3; _jzqc=1; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1465698710; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1465714974; _jzqb=1.10.10.1465713058.1; TASession=%1%V2ID.2B3DAC4CB31D9CF4AF3FBE79F4910074*SQ.75*MC.18061*PR.1434%7CUserReview*LS.MemberProfile*GR.55*TCPAR.62*TBR.53*EXEX.66*ABTR.79*PPRP.93*PHTB.2*FS.86*CPU.14*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.22BAC6BF933443C0E3BE5DA31CAB6B2D*FA.1*DF.0*LR.https%3A%2F%2Fwww%5C.baidu%5C.com%2Fbaidu%5C.php%3Fsc%5C.OstK000Q8hIwmpOq3a79-FNYJnwtU6sq49aWurPlyZAF_o9IB6Cz0tKiH2iKQfCABCzW9TMVPPX807e_5QLAYTrXcqoXJaeMu5DDahTyOJI62SdWx1Qs_ouHdEUIFXJGHHEiZaf%5C.7b_a9nOA1Iqj3LHTbZxikg__lpS_XjZaqWx8vu5ZkLe8_XjZZakgdWsmvg_I5uu8_txZG_vImtA5ZGmlk3nUr*LP.%2F-a_suppm%5C.-a_supkw%5C.20749484724-a_supbl%5C.%257BlocalInfo%257D-a_supbc%5C.0-a_supsc%5C.1-a_supap%5C.1clg1-a_supbt%5C.-m18061-a_supai%5C.6405077608-a_supci%5C.95827795*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.1*BG.60763*BT.hmnhxd; TAUD=LA-1465698794444-1*LG-16448456-2.1.F*LD-16448458-.....'
	}
	r=requests.get(myUrl,headers=headers)
	soup = BeautifulSoup(r.text,'lxml')
	mycates=soup.select('div.tagBlock')
	for mycate in mycates:
		print(mycate.get_text())
#自然爱好者 夜生活爱好者 安详与宁静的追寻者

#多页爬取
def get_allurl():
	urls=['http://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,960,33)]
	for single_url in urls:
		get_index(single_url)



if __name__ == '__main__':
 	#get_index()
 	#get_mycate()
 	get_allurl()
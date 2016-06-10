import requests
import os
try:
    import cookielib
except:
    import http.cookiejar as cookielib

url='https://www.zhihu.com'
headers={
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Connection':'keep-alive',
	'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
	'Accept-Encoding':'gzip, deflate, sdch',
	'User-Agent':'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
}
r=requests.get(url)
#使用cookie信息
#获得session对象
session = requests.session()
print(session)
c=session.cookies=cookielib.LWPCookieJar(filename='cookies')
try:
	session.cookies.load(ignore_discard=True)
except:
	print("cookie 未能加载")

def get_xsrf():
	a=r.cookies['_xsrf']
	return a
def get_captcha():
	t = str(int(time.time()*1000))
	captcha_url = 'https://www.zhihu.com/captcha.gif?r='+t+"&type=login"
	r=session.get(captcha_url,headers=headers)
	with open('captcha.jpg','web') as f:
		f.write(r.content)
		f.close()
	try:
		im=Image.open('captcha.jpg')
		im.show()
		im.close()
	except:
		print(u'请到 %s 目录找到captcha.jpg手动输入' % os.path.abspath('captcha.jpg'))
	captcha=input("请输入验证码:")
	return captcha

def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://www.zhihu.com/settings/profile"
    login_code = session.get(url,allow_redirects=False).status_code
    if int(x=login_code) == 200:
        return True
    else:
        return False

def login(account,secert):
	post_url ='https://www.zhihu.com/#signin'
	postdata={
		'_xsrs':get_xsrf(),
		'email':account,
		'password':secret,
	}
	try:
		login_page=session.post(post_url,data=postdata,headers=headers)
		login_code=login_page.text
		print(login_page)
	except:
		postdata["captcha"] = get_captcha()
		login_page = session.post(post_url,data=postdata, headers=headers)
		login_code = eval(login_page.text)
		print(login_code['msg'])
session.cookies.save()

if __name__ == '__main__':
	if isLogin():
		print('你已经登录')
	else:
		account = input('请输入你的用户名\n>')
		secret = input('请输入你的密码\n>')
		login(secret,account)
from urllib import request, parse
from bs4 import BeautifulSoup as BS
import json
import datetime
import xlsxwriter
 
starttime = datetime.datetime.now()
 
url = r'http://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC'
# 拉钩网的招聘信息都是动态获取的，所以需要通过post来递交json信息，默认城市为北京
 
tag = ['companyName', 'companyShortName', 'positionName', 'education', 'salary', 'financeStage', 'companySize',
    'industryField', 'companyLabelList'] # 这是需要抓取的标签信息，包括公司名称，学历要求，薪资等等
 
tag_name = ['公司名称', '公司简称', '职位名称', '所需学历', '工资', '公司资质', '公司规模', '所属类别', '公司介绍']
 
 
def read_page(url, page_num, keyword):
    page_headers = {
        'Host':'www.lagou.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
        'Connection':'keep-alive',
    }
    if page_num == 1:
        boo = 'true'
    else:
        boo = 'false'
    #通过页面分析，发现浏览器提交的FormDate包括以下参数  
    page_data = parse.urlencode({
        'first':boo,
        'pn':page_num,
        'kd':keyword,
        })
    req = request.Request(url,headers=page_headers)
    page = request.urlopen(req,data=page_data.encode('utf-8')).read()
    page = page.decode('utf-8')
    return page

def read_tag(page,tag):
    page_json = json.loads(page)#转化成json对象
    page_json = page_json['content']['positionResult']['result']#通过分析获取json信息可知，招聘信息包含在result中
    page_result=[num for num in range[15]]#构造一个容量为15的list占位符，用来构造接下来的二维数组
    for i in range(15):
        page_result[i]=[]#构造二维数组
        for page_tag in tag:
            page_result[i].append[page_json[i].get(page_tag)]#遍历参数,将他们放置在同一个list中
        page_result[i][8] = ','.join(page_result[i][8])
    return page_result

def read_max_page(page):
    page_json = json.loads(page)
    max_page_num = page_json['content']['pageNo']
    if max_page_num >30:
        max_page_num = 30
    return max_page_num

def save_excel(fin_result,tag_name,file_name):
    book = xlsxwriter.Workbook(r'C:\Users\Administrator\Desktop\%s.xls' % file_name)#默认保存在桌面
    tmp = book.add_worksheet()
    row_num = len(fin_result)
    for i in range(1,row_num):
        if i ==1:
            tag_pos = 'A%S' % i
            tmp.write_row(tag_pos,tag_name)
        else:
            con_pos = 'A%s' % i
            content =fin_result[i-1]
            tmp.write_row(con_pos,content)
    book.close()

if __name__ == '__main__':
    print('*****************即将进行抓取********************')
    keyword = input('请输入你要搜索的语言类型:')
    fin_result = []
    max_page_num = read_max_page(read_page(url,1,keyword))
    for page_num in range(1,max_page_num):
        print('*****************即将进行抓取********************')
        page = read_page(url,page_num,keyword)
        page_result = read_tag(page,tag)
        fin_result.extend(page_result)
    file_name = input('抓取完成，输入文件保存名:')
    save_excel(fin_result,tag_name,file_name)
    endtime = datetime.datetime.now()
    time = (endtime-starttime).senconds
    print('总用时：%s s' % time)














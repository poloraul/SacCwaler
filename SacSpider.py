import urllib
import json
from bs4 import BeautifulSoup
import csv
import os
import time
import random
import pandas as pd
import requests
proxyFlag = True
def get_proxy():
    return requests.get(" http://123.207.35.36:5010/get/").content
proxy_info = pd.read_csv(open("proxy.csv"))
proxy_info = proxy_info.iloc[:,1:6].dropna()
# + proxy_info.iloc[:,0]+":"+proxy_info.iloc[:,1]
httptypes = proxy_info.iloc[:,4]
proxyAddresses = proxy_info.iloc[:,4]+ "://"+ proxy_info.iloc[:,0]+":"+ (proxy_info.iloc[:,1].map(str))+ "/"
proxy_list = []
proxyAddresses = [
                    '106.57.6.84:4528',
                    '106.59.58.214:4573',
                    '123.190.135.135:4511',
                    '182.110.118.227:4556',
                    '1.30.189.97:4599',
                    '112.113.161.163:4556',
                    '39.81.146.150:4588',
                    '182.87.239.87:4548',
                    '122.246.160.122:4570',
                    '117.63.78.128:4552',
                    '112.83.40.37:4526',
                    '114.104.185.247:4548',
                    '115.226.229.160:4508',
                    '112.192.191.166:4515',
                    '117.42.230.175:4576',
                    '182.34.206.88:4546',
                    '116.55.2.50:4528',
                    '36.34.13.220:4536',
                    '119.5.181.181:4586',
                    '182.99.40.138:4596',
                    '222.241.69.28:4568',
                    '101.64.33.123:4528',
                    '122.243.12.187:4542',
                    '175.149.87.93:4568',
                    '36.34.12.230:4536',
                    '115.220.37.147:4508',
                    '182.240.52.218:4581',
                    '117.57.97.191:4552',
                    '115.219.73.159:4517',
                    '60.188.41.69:4541',
                    '180.127.220.249:4513',
                    '218.64.197.239:4576',
                    '59.62.182.112:4576',
                    '113.124.217.99:4566',
                    '60.185.150.239:4540',
                    '112.114.165.9:4528',
                    '220.186.149.132:4532',
                    '175.154.204.196:4516',
                    '27.220.123.204:4513',
                    '115.219.73.26:4507',
                    '125.112.158.183:4524',
                    '60.182.23.13:4530',
                    '61.174.152.253:4517',
                    '114.230.130.116:4557',
                    '223.242.92.168:4551',
                    '114.229.198.187:4507',
                    '202.110.62.229:4511',
                    '49.79.36.79:4506',
                    '180.115.169.233:4516',
                    '180.120.77.157:4524'
                    ]
for httptypedata,proxyAddress in zip(httptypes,proxyAddresses):
    proxy = {'http':str.lower(proxyAddress)}
    proxy_list.append(proxy)
print(proxy_list)
USER_AGENTS = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
    ]
def builder_proxy():
    if proxyFlag:  
        proxy = random.choice(proxy_list)  
        # proxy = {'http':'http://'+(get_proxy().decode('utf-8'))+ "/"}
        proxy_handler = urllib.request.ProxyHandler(proxy)
        print(proxy)
    else:
        proxy = None
        proxy_handler = urllib.request.ProxyHandler()

    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)
    if proxy != None:
        proxy_list.remove(proxy)
    return proxy

def getCompanyList():
    pass

def getMemberList():
    pass

def getRpiId(r2SS_IFjjk):
    #get rpi_id
    url = 'http://exam.sac.net.cn/pages/registration/train-line-register!gsUDDIsearch.action'
    user_agent = random.choice(USER_AGENTS)
    headers ={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Connection': 'keep-alive',
        # 'Content-Length': '100',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_trs_uv=jq1mp3t5_373_bzyh; BIGipServergrade=2907809984.20480.0000; JSESSIONID=u9Ldz0SlI9stZSnz945YmbPLVl3SZ0yyv2NR1E0sMoyUOONOEWFD!1954408222',
        'Host': 'exam.sac.net.cn',
        'Origin': 'http://exam.sac.net.cn',
        # 'Referer': 'http://exam.sac.net.cn/pages/registration/sac-finish-person.html?r2SS_IFjjk=7DB526B20175E457E053D551A8C029D9',
        'User-Agent': user_agent,
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'filter_EQS_PPP_ID': r2SS_IFjjk,
        'sqlkey': 'registration',
        'sqlval': 'SD_A02Leiirkmuexe_b9ID'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, headers=headers, data=data)
    flag = False
    while flag == False:
        try:
            # proxy = builder_proxy()
            # time.sleep(random.randint(0,7))
            page = urllib.request.urlopen(req,timeout=30).read()
            page = page.decode('utf-8')
            objjson = json.loads(page)
            print('获取索引编号时,',objjson)
            if (isinstance(objjson,list) == False):
                if 'message' in objjson:
                    if objjson.get('message') == '访问过于频繁，请稍候访问！':
                        builder_proxy()
                        continue
            rpi_id = objjson[0].get("RPI_ID")
            flag = True
            return rpi_id
        except (ConnectionRefusedError,urllib.request.URLError) as e:
            print('获取索引编号时,',e)
            builder_proxy()
       

def getMemberInfo(rpi_id):
    #get photo
    url = 'http://exam.sac.net.cn/pages/registration/train-line-register!gsUDDIsearch.action'
    user_agent = random.choice(USER_AGENTS)
    headers ={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Connection': 'keep-alive',
        # 'Content-Length': '70',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_trs_uv=jq1mp3t5_373_bzyh; BIGipServergrade=2907809984.20480.0000; JSESSIONID=u9Ldz0SlI9stZSnz945YmbPLVl3SZ0yyv2NR1E0sMoyUOONOEWFD!1954408222',
        'Host': 'exam.sac.net.cn',
        'Origin': 'http://exam.sac.net.cn',
        # 'Referer': 'http://exam.sac.net.cn/pages/registration/sac-finish-person.html?r2SS_IFjjk=7DB526AF067FE457E053D551A8C029D9',
        'User-Agent': user_agent,
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'filter_EQS_RPI_ID': rpi_id,
        'sqlkey': 'registration',
        'sqlval': 'SELECT_PERSON_INFO'
    } 
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, headers=headers, data=data)
    flag = False
    while flag == False:
        try:
            # proxy = builder_proxy()
            # time.sleep(random.randint(0,7))
            page = urllib.request.urlopen(req,timeout=30).read()
            page = page.decode('utf-8')
            objjson = json.loads(page)
            print('获取基本信息时,',objjson)
            if (isinstance(objjson,list) == False):
                if 'message' in objjson:
                    if objjson.get('message') == '访问过于频繁，请稍候访问！':
                        builder_proxy()
                        continue
            memberInfo = objjson[0]
            flag = True
            return memberInfo
        except (ConnectionRefusedError,urllib.request.URLError,ConnectionError) as e:
            print('获取基本信息时,',e)
            builder_proxy()
def savePhoto(photoUrl,photoName,savePath):
    flag = False
    while flag == False:
        try:
            urllib.request.urlretrieve(photoUrl,'{}{}.jpg'.format(savePath,photoName))
            flag = True
            return
        except (ConnectionRefusedError,urllib.request.URLError,ConnectionError) as e:
            print('保存照片时,',e)
            builder_proxy()

def saveInfo(memberInfo,writeCsv):
    RPI_NAME = memberInfo.get('RPI_NAME')
    RPI_PHOTO_PATH = memberInfo.get('RPI_PHOTO_PATH')
    SCO_NAME = memberInfo.get('SCO_NAME')
    ECO_NAME = memberInfo.get('ECO_NAME')
    AOI_NAME = memberInfo.get('AOI_NAME')
    AOI_ID = memberInfo.get('AOI_ID')
    ADI_ID = memberInfo.get('ADI_ID')
    ADI_NAME = memberInfo.get('ADI_NAME')
    PTI_NAME = memberInfo.get('PTI_NAME')
    CER_NUM = memberInfo.get('CER_NUM')
    OBTAIN_DATE = memberInfo.get('OBTAIN_DATE')
    ARRIVE_DATE = memberInfo.get('ARRIVE_DATE')
    CERTC_ID = memberInfo.get('CERTC_ID')
    CERTC_NAME = memberInfo.get('CERTC_NAME')
    writeCsv.writerow([RPI_NAME,RPI_PHOTO_PATH,SCO_NAME,ECO_NAME,AOI_NAME,AOI_ID,ADI_ID,ADI_NAME,PTI_NAME,CER_NUM,
                        OBTAIN_DATE,ARRIVE_DATE,CERTC_ID,CERTC_NAME])
    photoBaseUrl = 'http://exam.sac.net.cn/photo/images/'
    try:
        savePhoto(photoBaseUrl+RPI_PHOTO_PATH,RPI_NAME+ADI_ID,'./photo/')
        return
    except Exception as e:
        with open('errorfile.csv','a',encoding='utf-8') as errorcsv:
            errorwriteCsv =  csv.writer(csvfile)
            errorwriteCsv.writerow([RPI_NAME,RPI_PHOTO_PATH,SCO_NAME,ECO_NAME,AOI_NAME,AOI_ID,ADI_ID,ADI_NAME,PTI_NAME,CER_NUM,
                        OBTAIN_DATE,ARRIVE_DATE,CERTC_ID,CERTC_NAME])
        print(e)
        return

def getSingle(r2SS_IFjjk,writeCsv):
    try:
        rpi_id = getRpiId(r2SS_IFjjk)
        memberInfo = getMemberInfo(rpi_id)
        saveInfo(memberInfo,writeCsv)
    except Exception as e:
        print(e)
        return
    

def getmemberList(writeCsv):
    url = 'http://exam.sac.net.cn/pages/registration/train-line-register!list.action'
    user_agent = random.choice(USER_AGENTS)
    headers ={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Connection': 'keep-alive',
        # 'Content-Length': '237',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_trs_uv=jq1mp3t5_373_bzyh; BIGipServergrade=2907809984.20480.0000; JSESSIONID=u9Ldz0SlI9stZSnz945YmbPLVl3SZ0yyv2NR1E0sMoyUOONOEWFD!1954408222',
        'Host': 'exam.sac.net.cn',
        'Origin': 'http://exam.sac.net.cn',
        # 'Referer': 'http://exam.sac.net.cn/pages/registration/sac-finish-person.html?r2SS_IFjjk=7DB526B20175E457E053D551A8C029D9',
        'User-Agent': user_agent,
        'X-Requested-With': 'XMLHttpRequest'
    }
    formdata = {
        'filter_EQS_AOI_ID': '1999090',
        'filter_EQS_PTI_ID': '',
        'page.searchFileName': 'homepage',
        'page.sqlKey': 'PAGE_FINISH_PUBLICITY',
        'page.sqlCKey': 'SIZE_FINISH_PUBLICITY',
        '_search': 'false',
        'nd': '1545623413025',
        'page.pageSize': '100',
        'page.pageNo': '1',
        'page.orderBy': 'id',
        'page.order': 'desc'
    } 
    nextFlag = True
    i = 46
    proxy = builder_proxy()
    while nextFlag == True:
        i = i+1
        print('正在处理第'+str(i)+'页')
        formdata['page.pageNo'] = str(i)
        data = urllib.parse.urlencode(formdata).encode('utf-8')
        req = urllib.request.Request(url, headers=headers, data=data)
        flag = False
        while flag == False:
            try:
                page = urllib.request.urlopen(req,timeout=30).read()
                flag = True
            except (ConnectionRefusedError,urllib.error.URLError,ConnectionError) as e:
                print('获取列表时，',e)
                builder_proxy()
            except Exception as e:
                print('获取列表时，',e)
                return
        page = page.decode('utf-8')
        objjson = json.loads(page)
        result = objjson.get('result')
        for single in result:
            ppp_id = single.get('PPP_ID')
            getSingle(ppp_id,writeCsv)
        csvfile.flush()
        print(objjson.get('hasNext'))
        nextFlag = objjson.get('hasNext')
        

csvfilename = 'member_info.csv'
with open(csvfilename,'a',encoding='utf-8') as csvfile:
    writeCsv =  csv.writer(csvfile)
    getmemberList(writeCsv)

# a = get_proxy().decode('utf-8')
# print(a)

# getPhoto('http://exam.sac.net.cn/photo/images/2018-11-05/registrationRpInfo/154138124799215413812479920.jpg','张伟欣','./photo/')

# csvfilename = 'member_info.csv'
# if os.path.exists(os.path.join(csvfilename)):
# 	os.remove(os.path.join(csvfilename))
# with open(csvfilename,'a',encoding='utf-8') as csvfile:
#     writeCsv =  csv.writer(csvfile)
#     getSingle('7DB526B30594E457E053D551A8C029D9',writeCsv)
# getMemberInfo(39956115)
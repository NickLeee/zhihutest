# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 19:34:03 2016

@author: lenovo
"""

import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.zhihu.com'
login_url = url+'/login/email'
login_data = {
    'email': 'email', 
    'password': 'pw',
    'rememberme': 'true',
}
headers_base = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
    'Connection': 'keep-alive',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36', 
    'Referer': 'http://www.zhihu.com/',
}

s = requests.session()
def get_xsrf(url=None):
        r = s.get(url, headers=headers_base)        
        xsrf = re.search(r'(?<=name="_xsrf" value=")[^"]*(?="/>)', r.text)
        if xsrf == None:
            return ''
        else:
            return xsrf.group(0)

xsrf = get_xsrf(url)
login_data['_xsrf'] = xsrf.encode('utf-8')

captcha_url = 'http://www.zhihu.com/captcha.gif'
captcha = s.get(captcha_url, stream=True)
print captcha
f = open('captcha.gif', 'wb')
for line in captcha.iter_content(10):
    f.write(line)
f.close()
   
print u'输入验证码:' 
captcha_str = raw_input() 
login_data['captcha'] = captcha_str

res = s.post(login_url, headers=headers_base, data=login_data)
print res.status_code
m_cookies = res.cookies


dataid = soup.find('button',class_="zg-btn zg-btn-follow zm-rich-follow-btn")
ids = dataid.attrs['data-id']





#coding:utf-8
'''
Created on 2015年5月21日

@author: mark_pc
'''
import urllib2
import urllib
import cookielib

filename = 'cookie.txt'
# 声明对象示例
cookie = cookielib.MozillaCookieJar(filename)
# 利用Urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 构建opener
opener = urllib2.build_opener(handler)

'''
enable_proxy = False
proxy_handler = urllib2.ProxyHandler({"http":"http://some-proxy.com:8080"})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
#urllib2.install_opener(opener)


values = {"username":"mark_meego","password":"csdn123.com"}
data = urllib.urlencode(values)
'''
postdata = urllib.urlencode({'username':'maiyt3','password':'zhishanyuan8534'})
url = "https://sso.sysu.edu.cn/cas/login"
'''
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
headers = {'User-Agent': user_agent}
request = urllib2.Request(url)
'''
try:
    response = opener.open(url, postdata)
    #print response.read()
except urllib2.URLError,e:
    if hasattr(e , "code"):
        print e.code
        print
    if hasattr(e, "reason"):
        print e.reason

else:
    print "OK"
    for item in cookie:
        print 'Name =' + item.name
        print 'Value = ' + item.value
    cookie.save(ignore_discard=True, ignore_expires=True)
    gradeUrl= 'https://sso.sysu.edu.cn/cas/login?service=http://ecampus.sysu.edu.cn/zsuyy/login.jsp'
    result = opener.open(gradeUrl)
    #print result.read()

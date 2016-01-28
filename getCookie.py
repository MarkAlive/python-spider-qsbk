import cookielib
import urllib2

cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
req = urllib2.Request("http://ecampus.sysu.edu.cn/zsuyy/application/main.jsp")

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
try:
    response = opener.open(req)
    #print response.read()
except urllib2.URLError,e:
    if hasattr(e , "code"):
        print e.code
        print
    if hasattr(e, "reason"):
        print e.reason

else:
    print "OK"
    print response.read()

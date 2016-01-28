#-*- coding:utf-8 -*-
__author__ = 'MYT'

import re
import urllib2
import time
from collections import defaultdict

#糗事百科热门段子爬虫类
class QSBK:
    def __init__(self):
        self.pageIndex = 1 # 当前要访问的页面
        self.MAX_PAGE_INDEX = 35 # 设置最大的访问页面数

        # 设置headers, 模拟浏览器访问，以防服务器不响应
        self.user_agent = ('Mozilla/5.0 (Macintosh; Intel ' +
        'Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like'+
        ' Gecko) Chrome/45.0.2454.85 Safari/537.36')
        self.headers = {'User-Agent': self.user_agent}

        self.pageItems = defaultdict(list) #收集已爬取的段子

        # 设置过滤段子内容的正则表达式,引入'?'表示以非贪婪模式匹配，‘re.S’标志表示'.'可以进行任意匹配，包括换行符
        self.pattern = re.compile('qiushi_tag_(.*?)".*?class="author.*?'+
                '<a.*?h2>(.*?)</h2>.*?<div.*?class='+
                '"content">(.*?)<!--(.*?)-->(.*?)class='+
                '"number">(.*?)</i>',re.S)

    def getPageItems(self):
        '''
        获取第self.pageIndex页的所有段子，并保持到self.pageItems中

        成功返回True, 否则返回False
        '''
        url = 'http://www.qiushibaike.com/hot/page/' + str(self.pageIndex)
        try:
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            pageContent = response.read().decode('utf-8')
            items = self.pattern.findall(pageContent) # 找出当前页面所有段子
            for item in items:
                haveImg = re.search('<img', item[3])
                # 过滤含照片的段子
                if not haveImg:
                    tagId = item[0]
                    x = time.localtime(int(item[3])) # 获取时间戳并转成北京时间
                    pubTime = time.strftime('%Y-%m-%d %H:%M:%S',x)
                    author = item[1]; nVote = item[5]; content = item[2]
                    self.pageItems[tagId] = [author, pubTime, nVote, content]
            return True

        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print e.code
            if hasattr(e, 'reason'):
                print e.reason
            return False

    def printPageItem(self, item):
        '''
        按格式打印段子
        '''
        # 将<br> 换成换行符
        content = item[3].strip().replace('<br/>','\n\t')
        print u"作者: %s\n发表时间: %s\n被赞数: %s\n内容:\n\t%s\n" % (item[0],item[1],item[2],content)
   

    def start(self):
        '''
        主程序，接受用户输入显示当前热门段子
        '''
        print u"正在读取糗事百科热门段子，按回车查看最新段子，按\"Q\"退出。"

        while True:
            input = raw_input()
            if input == "Q" or input == "q":
                return
            if len(self.pageItems) == 0:
                while len(self.pageItems) == 0:
                    if self.MAX_PAGE_INDEX < self.pageIndex:
                        print u"没有更多的段子，已退出。"
                        return
                    else:
                        if not self.getPageItems():
                            print u"获取页面失败，已退出。"
                            return
                        self.pageIndex += 1
            item_tag = self.pageItems.keys()[0]
            item = self.pageItems.pop(item_tag)
            self.printPageItem(item)
            print u"按回车查看下一条段子，按\"Q\"退出。"


if __name__ == '__main__':
    spider = QSBK()
    spider.start()

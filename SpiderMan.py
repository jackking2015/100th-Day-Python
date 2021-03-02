#coding:utf-8
#import os,sys
#sys.path.append("D:\Repository\PythonCode\1024Crawer")

from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from URLManager import URLManager

class SpiderMan(object):
    def __init__(self):
        self.manager = URLManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self,root_url):
        #添加入欧URL
        self.manager.add_new_url(root_url)
        #判断URL管理器中是否有新的URL，同时判断抓取了多少个URL
        while(self.manager.has_new_url() and self.manager.old_url_size()<10):
            try:
                #从URL管理器获取新的URL
                new_url = self.manager.get_new_url()
                #HTML下载器下载网页
                html = self.downloader.download(new_url)
                #HTML解析器抽取网页数据
                new_urls,data = self.parser.parser(new_url,html)
                #将抽取的URL添加到URL管理器中
                self.manager.add_new_urls(new_urls)
                #数据存储器存储文件
                self.output.store_data(data)
                print("已经抓取%s个链接"%self.manager.old_url_size())
            except Exception as e:
                print (e.args)
            #数据存储器将文件输出指定格式
        self.output.output_html()

if __name__ =="__main__":
    spider_man = SpiderMan()
    #暂时只选择一个folder
    #http://xh2.1024xp3.com/pw/html_data/14/1907/4170772.html
    #https://xh2.1024xp2.rocks/pw/index.php
    #https://xh2.1024xp2.rocks/pw/html_data/49/1909/4338064.html
    #https://xh2.1024xp2.rocks/pw/html_data/49/1909/4338055.html
    #http://k6.csnmdcjnx.xyz/pw/thread.php?fid=15
    #https://p3.csgfnmdb.xyz/pw/
    spider_man.crawl("https://p3.csgfnmdb.xyz/pw/thread.php?fid=15")

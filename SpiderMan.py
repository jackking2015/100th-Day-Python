from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from URLManager import URLManager
import jieba
import imageio
import wordcloud

class SpiderMan(object):
    def __init__(self):
        self.manager = URLManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()
        self.pageUrl = []
        for num in range(1,29):
            self.pageUrl.append(f'https://cl.887x.xyz/thread0806.php?fid=20&search=&page={num}')

    def crawl(self,root_url):
        self._crawlPages()
        #判断URL管理器中是否有新的URL，同时判断抓取了多少个URL
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                #从URL管理器获取新的URL
                new_url = self.manager.get_new_url()
                #HTML下载器下载网页
                html = self.downloader.download(new_url)
                #HTML解析器抽取网页数据
                self.parser.parser_article_page(new_url,html)
                #数据存储器存储文件
                #self.output.store_data(data)
                print("已经抓取%s个链接"%self.manager.old_url_size())
            except Exception as e:
                print (e.args)
            #数据存储器将文件输出指定格式
        #self.output.output_html()
        file_path = './doc/1111.txt'

        f = open(file_path, "r", encoding='utf-8').read()
        words = jieba.lcut(f)     # 使用精确模式对文本进行分词
        counts = {}     # 通过键值对的形式存储词语及其出现的次数

        for word in words:
            if  len(word) == 1:    # 单个词语不计算在内
                continue
            else:
                counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1
                
        items = list(counts.items())#将键值对转换成列表
        items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序

        for i in range(15):
            word, count = items[i]
            print("{0:<5}{1:>5}".format(word, count))

        with open(file_path,mode='r',encoding='utf-8')as f:
            #print(content)
            content = f.read()
            txt_list = jieba.lcut(content)
            string1 = ' '.join(txt_list)
            wc=wordcloud.WordCloud(
                width=2000,
                height=1200,
                background_color = "black",
                font_path = 'msyh.ttc',
                scale=15,
                stopwords=set([line.strip()for line in open('./doc/stopword.txt',mode='r',encoding='utf-8').readlines()])
            )
            wc.generate(string1)
            #plt.imshow(wc)
            #plt.axis("off")#不显示坐标轴
            #plt.show()#显示图片
            wc.to_file('./doc/1111.png')

    def _crawlPages(self):
        print("----------------------start crawl pages----------------------")
        #准备基础页面URL
        for page in self.pageUrl:
            #HTML下载器下载网页
            html = self.downloader.download(page)
            #HTML解析器抽取网页数据
            new_urls = self.parser.parserCatalog(page,html)
            #将抽取的URL添加到URL管理器中
            self.manager.add_new_urls(new_urls)
        print("----------------------stop crawl pages----------------------")
        return


if __name__ =="__main__":
    spider_man = SpiderMan()
    #暂时只选择一个folder
    #https://cl.887x.xyz/thread0806.php?fid=20&search=&page=1
    #http://xh2.1024xp3.com/pw/html_data/14/1907/4170772.html
    #https://xh2.1024xp2.rocks/pw/index.php
    #https://xh2.1024xp2.rocks/pw/html_data/49/1909/4338064.html
    #https://xh2.1024xp2.rocks/pw/html_data/49/1909/4338055.html
    #http://k6.csnmdcjnx.xyz/pw/thread.php?fid=15
    #https://p3.csgfnmdb.xyz/pw/
    spider_man.crawl("https://cl.887x.xyz/thread0806.php?fid=20&search=&page=1")

#coding:utf-8
import re
import urlparse3
import jieba
import imageio
import wordcloud
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup

class HtmlParser(object):

    def parserCatalog(self,page_url,html_cont):
        '''
        用于解析网页内容，抽取URL和数据
        :param page_url:下载页面的URL
        :param html_cont:下载的网页内容
        :return:返回URL和数据
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='GBK')
        new_urls = self._get_new_article_urls(page_url,soup)
        return new_urls

    def parser_article_page(self,page_url,html_cont):
        '''
        用于解析网页内容，抽取URL和数据
        :param page_url:下载页面的URL
        :param html_cont:下载的网页内容
        :return:返回URL和数据
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='GBK')
        self._get_new_article_data(page_url,soup)
        return

    def parser(self,page_url,html_cont):
        '''
        用于解析网页内容，抽取URL和数据
        :param page_url:下载页面的URL
        :param html_cont:下载的网页内容
        :return:返回URL和数据
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='GBK')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data


    def _get_new_article_urls(self,page_url,soup):
        '''
        抽取新的URL集合
        :param page_url:下载页面的URL
        :param soup:soup
        :return:返回新的URL集合
        '''
        new_urls = set()
        #抽取符合要求的a标记
        links = soup.find_all('a',href=re.compile(r'htm_data\/[0-9]+\/[0-9]+\/[0-9]+.html'))
        #links = soup.find_all('a',attrs={'href',re.compile(r'htm_data\/[0-9]+\/[0-9]+\/[0-9]+.html')})
        for link in links:
            if link.b == None:
                #and link.font['color']!='green'
                if link.font != None and link.font['color'] =='red':
                    if link['href'] == 'htm_data/0805/20/131469.html' or link['href'] == 'htm_data/0810/20/183193.html' or link['href'] == 'htm_data/2010/20/932276.html' :
                        print("delete---->"+link.string+" : "+link['href']+": "+link.font['color'])
                    else:
                        new_urls.add('https://cl.887x.xyz/' +link['href'])
                        #print("add---->"+link.string+" : "+link['href']+": "+link.font['color'])
                else:
                    #if link.font != None :
                        #print("color---->"+link.string+" : "+link['href']+": "+link.font['color'])
                    #提取href属性
                    new_urls.add('https://cl.887x.xyz/' +link['href'])
                    #new_url = link['href']
                    #拼接成完整网址 https://cl.887x.xyz/
                    #new_full_url = 'https://cl.887x.xyz/' +new_url
                    #new_urls.add(new_full_url)
        return new_urls

    def _get_new_urls(self,page_url,soup):
        '''
        抽取新的URL集合
        :param page_url:下载页面的URL
        :param soup:soup
        :return:返回新的URL集合
        '''
        new_urls = set()
        #抽取符合要求的a标记
        links = soup.find_all('a',href=re.compile(r'html_data\/[0-9]+\/[0-9]+\/[0-9]+.html'))
        #links = soup.find_all('a')
        for link in links:
            #提取href属性
            new_url = link['href']
            #拼接成完整网址 http://k5.99e5be8a.club/pw/thread.php?fid=15
            new_full_url = 'https://p3.csgfnmdb.xyz/pw/' +new_url
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        '''
        抽取有效数据
        :param page_url:下载页面的URL
        :param soup:
        :return:返回有效数据
        '''
        data={}
        images = soup.find_all('img',src=re.compile(".*\/upload\/image\/.*.jpg"))
        for image in images:
            new_url = image['src']
            data['url'] = new_url
            #data.append(new_url)
        return data

    def _get_new_article_data(self,page_url,soup):
        '''
        抽取有效数据
        :param page_url:下载页面的URL
        :param soup:
        :return:返回有效数据
        '''
        print(page_url)
        #page_id = re.compile(r"(\/)(\d+)(\.)").findall(page_url)

        #page_id = re.sub(r"(\/)(\d+)(\.)","\2",page_url)
        page_url = page_url[0:page_url.rfind(".html")]
        page_id = page_url[page_url.rfind("/")+1:]
        #print(page_id)

        article = soup.find('div',attrs={"class" :"tpc_content do_not_catch"})
        content = article.text
        pattern1 = r"赞\(\d+\)"
        #datepat1=re.compile(pattern1)
        pattern2 = r"\[...\]"
        #datepat2=re.compile(pattern2)
        #print(datepat1.findall(content))
        #print(datepat2.findall(content))
        content = re.sub(pattern1, "", content)
        content = re.sub(pattern2, "", content)
        content = content.replace('\t','')
        #file_path = './doc/'+page_id+'.txt'
        file_path = './doc/1111.txt'
        with open(file_path,mode='a',encoding='utf-8')as f:
            #print(content)
            f.write(content)
            # txt_list = jieba.lcut(content)
            # string1 = ' '.join(txt_list)
            # wc=wordcloud.WordCloud(
            #     width=2000,
            #     height=1200,
            #     background_color = "black",
            #     font_path = 'msyh.ttc',
            #     scale=15,
            #     stopwords=set([line.strip()for line in open('./doc/stopword.txt',mode='r',encoding='utf-8').readlines()])
            # )
            # wc.generate(string1)
            #plt.imshow(wc)
            #plt.axis("off")#不显示坐标轴
            #plt.show()#显示图片
            #wc.to_file(page_id+'.png')
        return

    
        

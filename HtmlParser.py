#coding:utf-8
import re
import urlparse3
from bs4 import BeautifulSoup

class HtmlParser(object):

    def parser(self,page_url,html_cont):
        '''
        用于解析网页内容，抽取URL和数据
        :param page_url:下载页面的URL
        :param html_cont:下载的网页内容
        :return:返回URL和数据
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

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

    
        

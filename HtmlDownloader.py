#coding:utf-8
import requests
class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None
        #user_agent = 'Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)'
        #user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

        #headers = {'User-Agent':user_agent}
        r = requests.get(url,headers = headers)
        if r.status_code == 200:
            r.encoding = 'GBK'
            return r.text
        return None

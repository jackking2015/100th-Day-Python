from bs4 import BeautifulSoup
soup = BeautifulSoup('<b class="boldest" href="sss"></b>','lxml')
tt = soup.find('b')
if tt.font == None :
    print("ok")
tag = soup.b
type(tag)
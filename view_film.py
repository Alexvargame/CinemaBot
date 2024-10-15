from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import ssl
import re
import requests
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

params={'story':'Тор','value':'Тор'}
bs0bj=BeautifulSoup(requests.get('https://kinotochka.co/index.php?do=search',params).text)
#html=urlopen('https://kinozal.tv/browse.php',context=ctx)
v=bs0bj.find('div',{'class':'big-wrapper'}).find('table').findAll('input')[0]#find('div',{'class':'berrors'})#.find('div',{'id':'dle-content'})#.findAll('a')#,href=re.compile('^(/details)'))
print(v)
vv=bs0bj.find('div',{'class':'big-wrapper'}).find('div',{'class':'center-box'}).findAll('a',{'class':'sres-wrap'})
print(vv)

view_films=bs0bj.find('div',{'class':'big-wrapper'}).find('div',{'class':'middle-content-wr'})
print(view_films)
##for link in search_films:
##    if 'href' in link.attrs:
##        li='https://kinozal.tv/'+link['href']
##        film=link.get_text()
##        print(li, film)
##        print()


##for link in top_films:
##    if 'href' in link.attrs:
##        temp=BeautifulSoup(urlopen('https://kinozal.tv/'+link['href'],context=ctx).read())
##        title=temp.find('div',{'class':'content'}).find('div',{'class':'mn_wrap'}).find('a').get_text()
##        print(title)
##        actors=temp.find('div',{'class':'content'}).find('div',{'class':'mn_wrap'}).find('div',{'class':'mn1_content'}).findAll('b')
##        for act in actors:
##            if act.get_text()=='В ролях:':
##                print(act.get_text())
##                print(temp.find('div',{'class':'content'}).find('div',{'class':'mn_wrap'}).find('div',{'class':'mn1_content'}).findAll('span')[3].get_text())
##        
##          
## 

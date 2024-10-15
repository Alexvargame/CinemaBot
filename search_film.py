from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import ssl
import re
import requests





def search_film(params):
    result={}
    name_film=[]
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    #params={'s':'','d':'','c':'','g':'','v':'','w':'','t':'','f':''}
    ##params['s']=input('Введите название: ')
    ##params['d']=input('Год выпуска: ')

    bs0bj=BeautifulSoup(requests.get('https://kinozal.tv/browse.php', params).text)
    search_films=bs0bj.findAll('div',{'class':'bx2_0'})[3].find('table').findAll('a',href=re.compile('^(/details)'))
    for link in search_films:
        if 'href' in link.attrs:
            li='https://kinozal.tv/'+link['href']
            film=link.get_text()
            if film.split('/')[0] not in name_film:
                name_film.append(film.split('/')[0])
                result[li]=film
    return result
def main():
    for key,value in search_film(params).items():
        print(key,value)
  
  
 
if __name__ == "__main__":
    params={'s':'Тор','d':'','c':'','g':'','v':'','w':'','t':'','f':''}
##    params['s']=input('Введите название: ')
##    params['d']=input('Год выпуска: ')

    main()

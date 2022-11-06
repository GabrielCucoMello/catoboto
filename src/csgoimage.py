from urllib import request as req
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def pegaImagem(url):
    uClient = uReq(url)
    pageHtml = uClient.read()
    uClient.close()
    pageSoup = soup(pageHtml, "html.parser")
    if pageSoup.find('div', {"class":"playerAvatarAutoSizeInner"}):
        avatarUrl = pageSoup.find('div', {"class":"playerAvatarAutoSizeInner"}).find('img', recursive = False)['src']
    return avatarUrl
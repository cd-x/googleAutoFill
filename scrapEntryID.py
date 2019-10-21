from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

import os

link=input()
urlClient = uReq(link)

html_find = urlClient.read()

urlClient.close()

parsed_page = soup(html_find,"html.parser")

body= parsed_page.find('body')

csr= body.find('script',{'type':'text/javascript'})

#now using regex we can obtain all entries

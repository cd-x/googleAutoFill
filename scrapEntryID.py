from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os


#link = "https://docs.google.com/forms/d/e/1FAIpQLSeSPjE6xjtEIK636ZKW-EUMKPrhJ9hgPy3DSj06HgHgS2OGfA/viewform?usp=sf_link"
#link="https://forms.gle/9uMFD6NTeQBSBPwp8"

class Scrap:
    def __init__(self,link):
        self.link =link
        self.result ={}
        self.set ={'\"Name\"','\"Email\"','\"Phonenumber\"','\"Address\"','\"Comments\"','\"Collegename\"',
                   '\"UGMarks\"','\"PGMarks\"','\"Class10thmarks\"','\"Class12thmarks\"','\"DateofBirth\"'}
        
    def entryID(self):
        #self.link =link
        urlClient = uReq(self.link)
        html_find = urlClient.read()
        urlClient.close()
        parsed_page = soup(html_find,"html.parser")
        body= parsed_page.find('body')
        
        public_data= body.find('script',{'type':'text/javascript'})

        #now creating parser we can obtain all entries
        text = public_data.contents
        text=text[0]
        txt = text[27:-2]
        txt=txt.replace(" ","")
        txt = txt.replace("\n",",")
        txt = txt.replace("[",",")
        txt = txt.replace("]",",")
        list2 =txt.split(sep=',')
        list3=[]
        for x in list2:
            if len(x)>0 and x is not 'null':
                list3.append(x)
        #make the entries update here        


         #if an entry present in set  found then look for its entry id in parsed 'txt' above .
                
        for i in range(len(list3)):
            if list3[i] in self.set:
                val=list3[i]
                while True:
                    i=i+1
                    if i>=len(list3) or len(list3[i])>=9 and list3[i].isnumeric():
                        break
                #print(val,'==>',list3[i],'\n')
                self.result[val]=list3[i]

        '''print('======DETAILS====')
        for e in res:
            str = "entry."+res[e]
            print(str)'''
        return self.result

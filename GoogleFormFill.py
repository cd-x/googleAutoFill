from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
import time
import json
from scrapEntryID import Scrap

class Formfiller:
    def __init__(self):
        self.name = ''
        self.address = ''
        self.clg_nm = ''
        self.gender = ''
        self.ten_mar = ''
        self.twel_mar = ''
        self.grad_mar = ''
        self.pg_mar = ''
        self.dob = ''
        self.email = ''
        self.contact = ''
        
        self.nameb = ''
        self.addressb = ''
        self.clg_nmb = ''
        self.genderb = ''
        self.ten_marb = ''
        self.twel_marb = ''
        self.grad_marb = ''
        self.pg_marb = ''
        self.dobb = ''
        self.emailb = ''
        self.contactb = ''
        
    def read(self):
        self.name = input("Enter your name")
        self.address = input("write your Address")
        self.clg_nm = input("Enter your institution name")
        self.gender = input(" gender ")
        self.ten_mar = input("class 10th marks ")
        self.twel_mar = input("Class 12th marks" )
        self.grad_mar = input("UG marks")
        self.pg_mar = input("PG Marks")
        self.dob = input("Date of birth")
        self.email = input("Enter your email id")
        self.contact = input("Enter your contact number")
        
    def storeuserdat(self):
        userdat = {}
        userdat = {'name':self.name,
                   'address' : self.address,
                   'clg' : self.clg_nm,
                   'gender' : self.gender,
                   'ten_mar':self.ten_mar,
                   'twel_mar':self.twel_mar,
                   'grad_mar':self.grad_mar,
                   'pg_mar':self.pg_mar,
                   'dob':self.dob,
                   'email':self.email,
                   'contact':self.contact
                   }
        
        with open('user_details.json','w+') as user:
            json.dump(userdat, user)
            
            
    def dataloader(self):
        with open('user_details.json') as json_data:
            user_di = json.load(json_data)
            json_data.close()
            dat = {}
            dat = dict(user_di)
            
            self.nameb = dat['name']
            self.addressb = dat['address']
            self.clg_nmb = dat['clg']
            self.genderb = dat['gender']
            self.ten_marb = dat['ten_mar']
            self.twel_marb = dat['twel_mar']
            self.grad_marb = dat['grad_mar']
            self.pg_marb = dat['pg_mar']
            self.dobb = dat['dob']
            self.emailb = dat['email']
            self.contactb = dat['contact']
        
    def formfill(self):

        link = input('Enter form link here  ==>>')
        s=Scrap(link)
        entries = s.entryID()
        driver = webdriver.Firefox(r"C:\\Users\\rishi kumar\\Desktop\\sem3\\py & r\\1")
        driver.get(link)
        time.sleep(1)
        username = driver.find_element_by_name("entry."+entries['"Name"'])
        username.send_keys(self.nameb)
        time.sleep(1)
        details = driver.find_element_by_name("entry."+entries['"Address"'])
        details.send_keys(self.addressb)
        
        details = driver.find_element_by_name("entry."+entries['"Collegename"'])
        details.send_keys(self.clg_nmb)
        time.sleep(1)

        details = driver.find_element_by_name("entry."+entries['"Class10thmarks"'])
        details.send_keys(self.ten_marb)
        time.sleep(1)
        
        details = driver.find_element_by_name("entry."+entries['"Class12thmarks"'])
        details.send_keys(self.twel_marb)
        time.sleep(1)
        
        details = driver.find_element_by_name("entry."+entries['"UGMarks"'])
        details.send_keys(self.grad_marb)
        time.sleep(2)
        
        details = driver.find_element_by_name("entry."+entries['"PGMarks"'])
        details.send_keys(self.pg_marb)
        time.sleep(1)
        
        details = driver.find_element_by_name("entry."+entries['"DateofBirth"'])
        details.send_keys(self.dobb)
        time.sleep(2)
        
        details = driver.find_element_by_name("entry."+entries['"Email"'])
        details.send_keys(self.emailb)
        time.sleep(1)
        
        details = driver.find_element_by_name("entry."+entries['"Phonenumber"'])
        details.send_keys(self.contactb)
        time.sleep(1)
        
        submit = driver.find_element_by_tag_name('span')
        submit.click()
        
        
u1 = Formfiller()
u1.dataloader()
u1.formfill()
        

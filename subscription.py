#!/usr/bin/python

__author__ = "J_Hack92"

import os
from lxml import html
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from twilio.rest import TwilioRestClient
import re
import requests


class HtmlRat:

    def __init__(self):
        pass

    def req_page(self, url):
        page = requests.get(url)
        tree = html.fromstring(page.content)
        return tree

    def tag_data(self, txpath):
        tag_val = tree1.xpath(txpath + "/text()")
        val = ''.join(tag_val).strip(' ')
        val = val.split(' ')
        return val


class WebBrowser:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def open_site(self, url):
        self.driver.get(url)
        time.sleep(3)

    def typer(self, id, data):
        input = self.driver.find_element_by_id(id)
        input.send_keys(data)
        time.sleep(2)

    def newTab(self):
        # for any os other than OSX it should be control else command0
        self.driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')

    def clicker(self, id):
        self.driver.find_element_by_id(id).click()
        time.sleep(5)

    def clickerX(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()
        time.sleep(5)

    def wait(self, sec):
        print "start of wait"
        time.sleep(sec)
        print "end of wait"

    def close(self):
        self.driver.close()


class Subscription:
    def __init__(self):
        pass

    def siriusxm(self):
        browser = WebBrowser()
        browser.open_site("http://fakemailgenerator.com/#/"+domainre+"/"+first+"/")
        browser.newTab()
        browser.open_site('https://streaming.siriusxm.com/?/flepz=true#_frmAccountLookup')
        time.sleep(2)
        browser.typer("frmAccountLookup_txtFName", first)
        browser.typer("frmAccountLookup_txtLName", last)
        browser.typer("frmAccountLookup_txtEmail", email)
        browser.typer("frmAccountLookup_txtPhone", fphone)
        browser.typer("frmAccountLookup_txtzipcode", zip)
        browser.clicker("frmAccountLookup_btnnext")
        browser.clicker("frmSelfIdentity_imageDonotRadio")
        browser.clicker("frmSetupLogin_btnDone")
        #browser.close()
    # Will be adding more sites soon!

class Eaccount:
    def __init__(self):
        self.browser = WebBrowser()

    def zoho(self):
        self.browser.open_site("https://mail.zoho.com/biz/createAcc.do")
        self.browser.typer("sfirstname", first)
        self.browser.typer("lastname", last)
        self.browser.typer("username", user)
        self.browser.typer("password", password)
        self.browser.typer("email", email)

class Messenger:
    def __init__(self):
        pass
    
    def send_txt(message):

        #SID/Token are retrievable from your accounts page
        ACCOUNT_SID = "ACcce1c4143b4642d547ffda9ddde4bf9c"
        AUTH_TOKEN = "6cf7df628257162286b6bcb5efbdc4cc"

        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

        message = client.messages.create(
            body="'"+message+"'",  # Message body, if any
            to="+ADDPHONEHERE", # Add your phone number here
            from_="+ADDTIWLIOHERE", #Add the number given by twilio
        )
        print message.sid

# Defining the classes
markup = HtmlRat()
sub = Subscription()
txtmsg = Messenger()
egen = Eaccount()
# execute functions to get data via xpath
tree1 = markup.req_page("http://fakenamegenerator.com")
aname = markup.tag_data('//*[@id="details"]/div[2]/div[2]/div/div[1]/h3')
phone = markup.tag_data('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[4]/dd')
address = markup.tag_data('//*[@id="details"]/div[2]/div[2]/div/div[1]/div')

#variables with the values
first = aname[0]
last = aname[2]

fphone = re.sub("[^0-9]", "", phone[0])
zip = address[-1] # last one in the array is the zip

tree1 = markup.req_page("http://fakemailgenerator.com")
user = markup.tag_data('//*[@id="home-email"]')
domain = markup.tag_data('//*[@id="domain"]')
# could have done a function (for the email spit)but whatever
d = domain[0].split("@")
domainre = d[1]
#user = re.search("[\w.]+", email).group()
# end of all the stripping of email addresses
email = first+"@"+domainre
print (first, last, email, fphone, zip)


#sub.siriusxm()
egen.zoho()
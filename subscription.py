#!/usr/bin/python

__author__ = "J_Hack92"

import os
from lxml import html
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from twilio.rest import TwilioRestClient
import requests
import re



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

#Basic selenium setup
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

    def wait(self, sec):
        time.sleep(sec)

    def close(self):
        self.driver.close()

def zip_chk():
    try:
        float(zip)
        print "Zip code is good yo"
        return True
    except:
        print "Zip is no bueno try parsing again"
        os.system("python html_handlerv2.py")

Class Subscription:
	def siriusxm():
		browser = WebBrowser()
		browser.open_site("http://fakemailgenerator.com/#/"+domain+"/"+user)
		browser.newTab()
		browser.open_site('https://streaming.siriusxm.com/?/flepz=true#_frmAccountLookup')
		browser.typer("frmAccountLookup_txtFName", first)
		browser.typer("frmAccountLookup_txtLName", last)
		browser.typer("frmAccountLookup_txtEmail", email)
		browser.typer("frmAccountLookup_txtPhone", fphone)
		browser.typer("frmAccountLookup_txtzipcode", zip)
		browser.clicker("frmAccountLookup_btnnext")
		browser.clicker("frmSelfIdentity_imageDonotRadio")
		browser.clicker("frmSetupLogin_btnDone")
		browser.close()
	# Will be adding more sites soon!

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

# Defining the class
markup = HtmlRat()
# execute functions to get data via xpath
tree1 = markup.req_page("http://fakenamegenerator.com")
aname = markup.tag_data('//*[@id="details"]/div[2]/div[2]/div/div[1]/h3')
mail = markup.tag_data('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[9]/dd')
phone = markup.tag_data('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[4]/dd')
address = markup.tag_data('//*[@id="details"]/div[2]/div[2]/div/div[1]/div')

#variables with the values
first = aname[0]
last = aname[2]
email = mail[0]
# could have done a function (for the email spit)but whatever
d = re.search("@[\w.]+", email).group().split("@")
domain = d[1]
user = re.search("[\w.]+", email).group()
# end of all the stripping of email addresses
fphone = re.sub("[^0-9]", "", phone[0])
#faddress = address[40], address[41], address[43], address[44]
zip = address[-1]
print (first, last, email, fphone, zip)

zip_chk()
siriusxm()

# If you want to send a text message use function send_txt("type message here" below it will send me the email address
send_txt(email)

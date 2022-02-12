#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import telepot
import os
import smtplib
import time 
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# virtualenv -p python3 kopf-env
#http://chromedriver.chromium.org/downloads
#https://tirinox.ru/selenium-screenshot-python/
# pip install telepot

def save_screen(url):
  DRIVER = 'chromedriver'
  options = webdriver.ChromeOptions()
  options.add_argument('--start-maximized')
  options.add_argument('--headless')
  options.add_argument('--no-sandbox')
  options.add_argument('--single-process')
  options.add_argument('--disable-dev-shm-usage')
  options.add_argument('--window-size=1280,1024')
  driver = webdriver.Chrome(DRIVER, options=options)
  driver.get("http://10.31.110.153/mrtg/mrtg-cnt.fcgi/lptz-bpe2.cnt.ip.rostelecom.ru/lptz-bpe2.cnt.ip.rostelecom.ru_xe-1_0_0.61"+url+".html")
  screenpath='/tmp/screenshot61'+url+'.png'
  driver.save_screenshot(screenpath)
  driver.quit()
  return screenpath

#1123336121:AAG__r3tJuahFAL7ca5-b18w9IvmVH9ttZE
#1001356529963
#https://stackoverflow.com/questions/35314526/telegram-bot-telepot-api-is-it-possible-to-send-an-image-directly-from-url-wi
#https://telepot.readthedocs.io/en/latest/#send-a-message
def send2telegram(screenshot):
  telepot.api.set_proxy('http://192.168.101.192:8080') 
#  bot = telepot.Bot("1123336121:AAG__r3tJuahFAL7ca5-b18w9IvmVH9ttZE") #Old group MON-NLMK
  bot = telepot.Bot("1508333012:AAFF5MYJCx63TUuFE_btXIq4L2PEx5iCcow")  #New group RCYSS-SCREEN
#bot.sendMessage(-1001356529963, "ТЕСТ")
#  bot.sendPhoto(-1001356529963, photo=open(screenshot, 'rb'))
  bot.sendPhoto(-449892266, photo=open(screenshot, 'rb'))

#https://stackoverflow.com/questions/13070038/attachment-image-to-send-by-mail-using-python
#https://stackoverflow.com/questions/13070038/attachment-image-to-send-by-mail-using-python
def send2mail(ImgFileName):
  img_data = open(ImgFileName, 'rb').read()
  msg = MIMEMultipart()
  msg['Subject'] = 'Screenshot camera graphs '+time.strftime("%Y%m%d-%H%M%S")+' '+ImgFileName
  msg['From'] = 'video-nlmk@les.loc'
  msg['To'] = 'igor.dzyuin@rt.ru'

  text = MIMEText("Screenshot camera graphs")
  msg.attach(text)
  image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
  msg.attach(image)

  s = smtplib.SMTP("10.35.198.100", "25")
  s.ehlo()
 #   s.starttls()
  s.ehlo()
 #   s.login(UserName, UserPassword)
  s.sendmail(msg['From'], msg['To'], msg.as_string())
  s.quit()


if __name__ == '__main__':
  list_urls = ["17", "18", "19", "20", "21", "22"]

  for url_id in list_urls:
    screenpath=save_screen(url_id)
    send2telegram(screenpath)
#    send2mail(screenpath)

import configparser
import requests
import csv
import chardet
# import gevenv
import logging
# import chrome
import datetime
from bs4 import BeautifulSoup
import time
from datetime import datetime, date, timedelta
from googletrans import Translator
import slackweb
import settings


SLACK_ID = settings.SLACK_ID
translator = Translator()

url = "https://techcrunch.com/startups/"
u = requests.get(url)
soup = BeautifulSoup(u.content, 'lxml')
for i in range(1,15):
       urlx=str(soup).split('"post-block__title"')[i].split('href="')[1].split('"')[0]
       title=str(soup).split('"post-block__title"')[i].split('href="')[1].split('">')[1].split('</a>')[0].replace('	','')
       print(urlx)
       print(title)

       # trans_ja = translator.translate(title,src='en', dest='ja')
       # print(trans_ja.text)
       

       # text=trans_ja.text +" "+ urlx
       text=title + " \n" + urlx 
       
       slack = slackweb.Slack(url=SLACK_ID)
#XXXはslackの「Incoming Webhook」にて取得
       dt_now = datetime.now()- timedelta(days=1)
       print(dt_now.strftime('%Y/%m/%d/') in urlx)
       if dt_now.strftime('%Y/%m/%d/') in urlx:
           slack.notify(text=text)
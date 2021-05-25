from bs4 import BeautifulSoup
import requests
import re
import json

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

data_url = ['https://blog.alfamart.co.id/category/promo/',
      'https://blog.alfamart.co.id/category/promo/page/2/']

summary = []
aimlFile = open("alfamartdetail.aiml", "w+")
aimlFile.write('<?xml version="1.0" encoding="UTF-8"?><aiml><category><pattern>PROMO ALFAMART</pattern><template><set name="namapromo">PROMO ALFAMART</set>:<random>')

for web in data_url:
  html = requests.get(web,headers=headers).text
  soup = BeautifulSoup(html, 'html.parser')
  for container in soup.findAll('div', class_='archive-post'):
    heading = container.find('h2', class_='entry-title').text
    article_summary = container.find('div', class_='entry-content').text
    url = container.find('a', class_='vmagazine-archive-more')['href']
    postedOn = container.find('span', class_='posted-on').text
    duration = ''
      #' '.join(article_summary.strip().split())
    article_summary = re.sub('\s+',' ',article_summary.strip())
    heading = heading.strip()
    check = article_summary.lower().find('read more')
    href = f'<br/><a target="_blank" href="{url}">info lengkapnya</a>'

    if(check > 0):
      article_summary = article_summary.replace('Read More',href)
    else:
      article_summary = article_summary + href 

    text = f'<li><![CDATA[<html><br/><b>{heading}</b><br/>{article_summary} </html>]]></li>'+"\n"
    aimlFile.write(text)

#print(json.dumps(summary, indent=2, ensure_ascii=False))
aimlFile.write('</random></template></category></aiml>')
aimlFile.close()

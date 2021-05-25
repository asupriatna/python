from bs4 import BeautifulSoup
import requests
import re
import json

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

data_url = ['https://www.traveloka.com/id-id/promotion']
summary = []
aimlFile = open("travelokadetail.aiml", "w+")
aimlFile.write('<?xml version="1.0" encoding="UTF-8"?><aiml><category><pattern>PROMO TRAVELOKA</pattern><template><set name="namapromo">PROMO TRAVELOKA</set>:<random>')

for web in data_url:
  html = requests.get(web,headers=headers).text
  soup = BeautifulSoup(html, 'html.parser')
  for container in soup.findAll('div', class_='promo-thumb'):
    category = container["data-product"].strip()
    heading = container.find('div', class_='promo-thumb-desc').text
    article_summary = container.find('div', class_='promo-thumb-desc').text
    url = container.find('a', class_='buttonLinkPromotion')['href']
    duration = container.find('div', class_='promo-thumb-duration').text
      #' '.join(article_summary.strip().split())
    heading = re.sub('\s+',' ',heading.strip())  
    article_summary = re.sub('\s+',' ',article_summary.strip())
    duration = re.sub('\s+',' ',duration.strip())
    check = article_summary.lower().find('read more')
    href = f'<br/><a target="_blank" href="https://www.traveloka.com/{url}">info lengkapnya</a>'

    if(check > 0):
      article_summary = article_summary.replace('Read More',href)
    else:
      article_summary = article_summary + href 

    text = f'<li><![CDATA[<html><br/><b>{heading}</b><br/>{article_summary} </html>]]></li>'+"\n"
    try:
      aimlFile.write(text)
    except:
      pass
#print(json.dumps(summary, indent=2, ensure_ascii=False))
aimlFile.write('</random></template></category></aiml>')
aimlFile.close()
    # summary.append({
    #     'Judul': heading.strip(),
    #     'Keterangan': article_summary,
    #     'url':'https://www.traveloka.com/'+url,
    #     'duration':duration,
    #     'category':category,
    #     'postedon': '',
    #     'sumber': 'Traveloka'
    # })


print(json.dumps(summary, indent=2, ensure_ascii=False))
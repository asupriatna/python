import json
import requests
import re
from datetime import datetime


headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}


category = {'TO-1000064': 'Tour and Travel','54650':'Elektronik','53704':'Otomotif','53270':'Komputer','54593':'Handphone'}
summary = []
aimlFile = open("bliblidetail.aiml", "w+")
aimlFile.write('<?xml version="1.0" encoding="UTF-8"?><aiml><category><pattern>PROMO BLIBLI</pattern><template><set name="namapromo">PROMO BLIBLI</set>:<random>')

for k, v in category.items():
    for x in range(2):
        page = x+1
        weburl = 'https://www.blibli.com/backend/content/promotions?category='+k+'&page='+ str(page)
        data = requests.get(weburl,headers=headers).text
        jsonObject = json.loads(data)
        for rowData in jsonObject.get("data"):
            name = rowData.get("name")
            title = rowData.get("title")
            url = rowData.get("url")
            starttime = int(rowData.get("startTime"))/1000 #Smallest accepted Unix timestamp by Windows 
            endtime = int(rowData.get("endTime"))/1000 #Smallest accepted Unix timestamp by Windows 
         
            title = re.sub('\s+',' ',title.strip())
            name = name.strip()
            check = title.lower().find('read more')
            href = f'<br/><a target="_blank" href="https://www.blibli.com/{url}">info lengkapnya</a>'
            duration = datetime.fromtimestamp(starttime).strftime('%d-%b-%Y') + ' s/d '+datetime.fromtimestamp(endtime).strftime('%d-%b-%Y')
            if(check > 0):
                title = title.replace('Read More',href)
            else:
                title = title + href

            text = f'<li><![CDATA[<html><br/><b>{name}</b><br/>{duration}<br/>{title}</html>]]></li>'+"\n"
            aimlFile.write(text)

  #          summary.append({
   #             'judul': rowData.get("name"),
    #            'keterangan': rowData.get("title"),
    #            'url': 'https://www.blibli.com/'+rowData.get("url"),
    #            'duration': datetime.fromtimestamp(starttime).strftime('%d-%b-%Y') + ' s/d '+datetime.fromtimestamp(endtime).strftime('%d-%b-%Y'),
    #            'category': v,
    #            'postedon': '',
    #            'sumber': 'blibli.com'
    #        })

# print(json.dumps(summary, indent=2, ensure_ascii=False))
aimlFile.write('</random></template></category></aiml>')
aimlFile.close()        

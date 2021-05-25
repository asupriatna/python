from bs4 import BeautifulSoup
import requests
import re
import json

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

url = 'https://www.tiket.com/promo'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup)
txScript = soup.find_all('script')[1].string
#save the result to file 
f = open("scripttag.txt", "w")
f.write(txScript)
f.close

print('done')

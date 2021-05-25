import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.accommodationforstudents.com/search-results?location=London&area=Baker%20Street&beds=0&searchType=any&lettingPeriod=academicYear&price=undefined&limit=12'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

#get the fourth script tag, test the json format on https://jsonformatter.org/ 
#extract json data starting from 58 exclude ending ; (-1) 
#remove all return carriage string

txScript = soup.find_all('script')[4].string.strip()[58:-1].rstrip('\r\n')

#save the result to file 
f = open("scripttag.txt", "w")
f.write(txScript)
f.close

#the result extracted json data able to proceed
data = json.loads(txScript)
print(data['properties']['listings']['groups'][0]['results'][0])
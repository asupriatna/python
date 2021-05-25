# Import the beautifulsoup 
# and request libraries of python.
import requests
import bs4
  
# Make two strings with default google search URL
# 'https://google.com/search?q=' and
# our customized search keyword.
# Concatenate them
text= "&q=allintitle:promo+tiket+pesawat+april+2021"
url = 'https://www.google.co.id/search?cr=countryID' + text
url = 'https://personalfinance.kontan.co.id/rubrik/219/Promo-dan-Diskon'
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36" ,
    'referer':'https://www.google.co.id/'
}

# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
request_result=requests.get(url,header)
  
# Creating soup from the fetched request
soup = bs4.BeautifulSoup(request_result.text,"html.parser")
print(soup)
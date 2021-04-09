import requests

data = requests.get('http://www.gutenberg.org/cache/epub/8001/pg8001.html')
content = data.content
print(content[1163:2200])

#content = 'content="Ebookmaker 0.4.0a5 by Marcello Perathoner <webmaster@gutenberg.org>" name="generator"/>\r\n</head>\r\n <body><p id="id00000">Project Gutenberg EBook The Bible, King James, Book 1: Genesis</p>\r\n\r\n<p id="id00001">Copyright laws are changing all over the world. Be sure to check the\r\ncopyright laws for your country before downloading or redistributing\r\nthis or any other Project Gutenberg eBook.</p>\r\n\r\n<p id="id00002">This header should be the first thing seen when viewing this Project\r\nGutenberg file. Please do not remove it. Do not change or edit the\r\nheader without written permission.</p>\r\n\r\n<p id="id00003">Please read the "legal small print," and other information about the\r\neBook and Project Gutenberg at the bottom of this file. Included is\r\nimportant information about your specific rights and restrictions in\r\nhow the file may be used. You can also find out about how to make a\r\ndonation to Project Gutenberg, and how to get involved.</p>\r\n\r\n<p id="id00004" style="margin-top: 2em">**Welcome To The World of F'

import re
from bs4 import BeautifulSoup

def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    [s.extract() for s in soup(['iframe', 'script'])]
    stripped_text = soup.get_text()
    stripped_text = re.sub(r'[\r|\n|\r\n]+', '\n', stripped_text)
    return stripped_text

clean_content = strip_html_tags(content)
print(clean_content[1163:2045])

import requests
import time

url = "https://zenquotes.io/api/today"
res = requests.get(url)
data = res.json()

# Variables
quote = data[0]['q']
author = data[0]['a']
now = time.strftime("%c")
quote_area = '\n<div align="center"><b><span>'+quote + \
    '</span></b><br><br><i> - '+author+'</i></div>\n'
updated_area = "<br><br><kbd>Last updated:"+now+"</kbd>"
# Readme File
readme = open("./README.md", "w")
readme.write(quote_area+updated_area)
readme.close()

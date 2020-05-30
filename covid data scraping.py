import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/country/india/"

req = requests.get(url)
bsobj = BeautifulSoup(req.text,"html.parser")
data = bsobj.find_all("div",class_ ="maincounter-number")

print("total Case :",data[0].text.strip())
print("total Deaths :",data[1].text.strip())
print("total Recovered :",data[2].text.strip())


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
url = "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=9f68fe31-ced4-48b7-b589-6a4c0e97db47&as-backfill=on"
uClient = uReq(url)
html= uClient.read()
uClient.close()
page_soup = soup(html,"html.parser")
container = page_soup.find_all("div",{"class","_3wU53n"})
# Here we are calculating the number of items present in the a website example Filpkart.com etc
print(container)
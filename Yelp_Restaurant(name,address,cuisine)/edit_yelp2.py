import requests
from bs4 import BeautifulSoup



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get("https://www.yelp.com/search?cflt=restaurants&find_loc=Tempe%2C%20AZ",headers=headers)
content = response.content
soup = BeautifulSoup(content,"html.parser")

top_rest = soup.find_all("div",attrs={"class": "lemon--div__373c0__6Tkil mainContentContainer__373c0__32Mqa arrange__373c0__UHqhV gutter-30__373c0__2PiuS border-color--default__373c0__2oFDT"})
list_tr = top_rest[0].find_all("div",attrs={"class": "lemon--div__373c0__6Tkil u-padding-t3 u-padding-b3 border--top__373c0__19Owr border-color--default__373c0__2oFDT"})

list_rest =[]
for tr in list_tr:
    dataframe ={}
    dataframe["rest_name"] = (tr.find("a",attrs={"class": "lemon--a__373c0__1_OnJ link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5"})).text;    
    dataframe["rest_address"] = (tr.find("span",attrs = {"class":"domtags--span__373c0__1VGzF"})).text;
    #print(dataframe["rest_address"].text)
    dataframe["cuisine_type"] = (tr.find("div",attrs={"class":"lemon--div__373c0__6Tkil priceCategory__373c0__3zW0R border-color--default__373c0__2oFDT"})).text
    list_rest.append(dataframe)
list_rest

import pandas
df = pandas.DataFrame(list_rest)
df.to_csv("yelp_txtfile.txt",index=False)
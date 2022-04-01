import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import webbrowser as wb
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}


def flipkart(product):
    uri = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off".format(
        product)
    req = requests.get(uri, headers=headers)
    html = req.text
    soup = bs(html, 'html.parser')
    baseurl = "https://www.flipkart.com"
    names1 = []
    prices1 = []
    urls = []
    offers = []

    h = soup.find_all("div", {"class": "_2kHMtA"})

    if not h:
        h = soup.find_all("div", {"class": "_4ddWXP"})
        for i in h:
            for j in i.find_all("a", {"class": "s1Q9rs"}):
                names1.append(j.text.replace("(", "").replace(")", "").replace(",", "").replace("-", ""))
            for k in i.find_all("div", {"class": "_30jeq3"}):
                prices1.append(k.text.replace("₹", "").replace(",", ""))
            for link in i.find_all("a", href=True):
                urls.append(baseurl + link['href'])
    else:
        for i in h:
            for j in i.find_all("div", {"class": "_4rR01T"}):
                names1.append(j.text.replace("(", "").replace(")", "").replace(",", "").replace("-", ""))
            for k in i.find_all("div", {"class": "_30jeq3 _1_WHN1"}):
                prices1.append(k.text.replace("₹", "").replace(",", ""))
            for link in i.find_all("a", href=True):
                urls.append(baseurl + link['href'])
    # urls=urls[:10]
    for i in urls:
        req = requests.get(i, headers=headers)
        html = req.content
        soup = bs(html, 'html.parser')
        offer = soup.find("li", {"_16eBzU col"})
        offers.append(offer)

    df1 = pd.DataFrame({'model': pd.Series(names1), 'price': pd.Series(prices1), 'offers': pd.Series(offers)})
    df1 = df1.dropna()
    return df1


start_time = time.time()
product = input("product name:")
df1 = flipkart(product)
result = pd.concat([df1], keys=["Flipkart"], axis=1)
stop_time = time.time()
print("Time taken {}".format(stop_time - start_time))
print(df1.to_string())
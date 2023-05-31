import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

from tabulate import tabulate

pd.set_option('display.max_colwidth', None)

soup = BeautifulSoup(requests.get("https://www.smartprix.com/ui/api/page-info?k=1SYMJDYwYlHJG5M4LKl_IzKE2JLH9GF6YiY52L2YwSUiYLYwnsttovtrnrrmmiYKLYwnsttovtqosvvpU").content)
res = json.loads(soup.text)
res = (res["item"]["searchResults"]["nodes"])
print("\n\n ****\n")

# data = {"Name":[],"Store":[],"Best Price":[]}
data = {"Name":[],"Store":[],"Best Price":[],"Link":[]}

for product in res:
    if product["stock"] != "UPCOMING":
        data["Name"].append(product["name"])
        data["Store"].append(product["bestStore"]["store"]["slug"])
        data["Best Price"].append(product["price"])
        data["Link"].append(product["bestStore"]["trackingLink"])

        data["Name"].append(" ")
        data["Store"].append(" ")
        data["Best Price"].append(" ")
        data["Link"].append(" ")

df = pd.DataFrame(data)
print(tabulate(df, showindex=False, headers=df.columns))

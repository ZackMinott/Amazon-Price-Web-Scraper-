# Amazon Web Scraper

import requests # requests allows us to access a url and pull data from there
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Samsung-UN65RU7100FXZA-Flat-UHD-Smart/dp/B07NC96MBL/ref=sxin_2_ac_d_pm?ac_md=6-1-QmV0d2VlbiAkNjAwIGFuZCAkMSwwMDA%3D-ac_d_pm&keywords=tv&pd_rd_i=B07NC96MBL&pd_rd_r=fc350547-69ee-4bea-baca-72e7fee45ece&pd_rd_w=UPFwB&pd_rd_wg=SLhpJ&pf_rd_p=eeff02d5-070a-45ea-a79e-d591974b877e&pf_rd_r=ANVQYB83VADNNXH2XSY4&psc=1&qid=1568233581&s=gateway'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

# Grabs all the data from the specified URL
page = requests.get(URL, headers = headers) 

# Parse all the data
soup = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(soup.prettify(), 'html.parser')

# get price and title of product
title = soup2.find(id = "productTitle").get_text()
price = soup2.find(id = "priceblock_ourprice").get_text()
converted_price = float(price[1:]) # gets the price of the item without the dollar sign

print(converted_price)
print(title.strip())
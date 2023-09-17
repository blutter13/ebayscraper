# bluter13 Ebay scraper
import requests
import re
from bs4 import BeautifulSoup
#Ebay search terms
ebay_1 = 'https://www.ebay.com/sch/search1'
ebay_2 = 'https://www.ebay.com/sch/search2'
ebay_3 = 'https://www.ebay.com/sch/search3'
ebay_4 = 'https://www.ebay.com/sch/search4'
#Scrape searches
res_1 = requests.get(ebay_1)
res_2 = requests.get(ebay_2)
res_3 = requests.get(ebay_3)
res_4 = requests.get(ebay_4)
#Slack integration
webhook = 'https://hooks.slack.com/workflows/<SLACK WEBHOOK URL>'
#Parse requests
bs_output_1 = BeautifulSoup(res_1.text, "html.parser")
bs_output_2 = BeautifulSoup(res_2.text, "html.parser")
bs_output_3 = BeautifulSoup(res_3.text, "html.parser")
bs_output_4 = BeautifulSoup(res_4.text, "html.parser")
#Extract items and sellers
tag_1 = bs_output_1.findAll(class_ = 's-item__title')
tag_2 = bs_output_2.findAll(class_ = 's-item__title')
tag_3 = bs_output_3.findAll(class_ = 's-item__title')
tag_4 = bs_output_4.findAll(class_ = 's-item__title')

links_1 = bs_output_1.findAll(class_ = 's-item__seller-info-text')
links_2 = bs_output_2.findAll(class_ = 's-item__seller-info-text')
links_3 = bs_output_3.findAll(class_ = 's-item__seller-info-text')
links_4 = bs_output_4.findAll(class_ = 's-item__seller-info-text')
#Regex Search Temrms
regex_search = re.compile(r'term1|term2|term3|term4')
#list and report
for i in range(1, len(tag_1)):
    result = regex_search.search(tag_1[i].text)
    if result != None:
        print('Hardware found: ', tag_1[i].text, "sold by storefront", links_1[i].text)
        items_1 = {"item_title": tag_1[i].text, "item_seller": links_1[i].text}
        send_1 = requests.post(webhook, json = items_1)
        print(send_1.text)
for i in range(1, len(tag_2)):
    result = regex_search.search(tag_2[i].text)
    if result != None:
        print('Hardware found: ', tag_2[i].text, "sold by storefront", links_2[i].text)
        items_2 = {"item_title": tag_2[i].text, "item_seller": links_2[i].text}
        send_2 = requests.post(webhook, json = items_2)
        print(send_2.text)
for i in range(1, len(tag_3)):
    result = regex_search.search(tag_3[i].text)
    if result != None:
        print('Hardware found: ', tag_3[i].text, "sold by storefront", links_3[i].text)
        items_3 = {"item_title": tag_3[i].text, "item_seller": links_3[i].text}
        send_3 = requests.post(webhook, json = items_3)
        print(send_3.text)
for i in range(1, len(tag_4)):
    result = regex_search.search(tag_4[i].text)
    if result != None:
        print('Hardware found: ', tag_4[i].text, "sold by storefront", links_4[i].text)
        items_4 = {"item_title": tag_4[i].text, "item_seller": links_4[i].text}
        send_4 = requests.post(webhook, json = items_4)
        print(send_4.text)
def lambda_handler(event, context):
        return event

from turtle import mode
import requests
from bs4 import BeautifulSoup
from json import loads
import csv
from datetime import datetime
import pandas as pd


def get_urls(url):
    res = requests.get(url)
    date_today = datetime.today().strftime('%m-%d-%y')

    json_list = loads(res.text)
    data_list = []
    # data_str = ''

    for item in json_list:
        urls_str = item['link'] + ','
        urls_str += date_today
        data = urls_str.split(',')

        data_list.append(data)

    # print(data_list)
    return data_list


url = 'https://www.highonstudy.com/wp-json/wp/v2/posts?author=43&per_page=10'
result = get_urls(url)

print(result[0][0])
df = pd.read_csv('./results.csv')
data = df['url'].eq(result[0][0])
print(data)
# urls = pd.DataFrame(result, columns=None, index=None)

# urls.to_csv('results.csv', mode='a', encoding='utf-8')

# result = pd.read_csv('./results.csv')

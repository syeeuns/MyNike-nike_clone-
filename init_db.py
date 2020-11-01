import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbnike


def create_db(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    mom_url = 'https://www.nike.com'
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    targets = soup.select('.ncss-container > ul > li > .a-product')
    my_list = []

    for one in targets:
        img_url = one.select_one('.a-product-image-primary > img')['src']
        name = one.select_one('.item-title').text
        price = one.select_one('.product-display-price').text
        url_detail = one.select_one('.a-product-image > a')['href']
        url_result = mom_url + url_detail

        product = {
            'img':img_url,
            'name':name,
            'price':price,
            'url':url_result
        }
        my_list.append(product)
    return my_list


db.shoes.insert_many(create_db('https://www.nike.com/kr/ko_kr/w/women/fw'))
db.clothes_jacket.insert_many(create_db('https://www.nike.com/kr/ko_kr/w/women/ap/jackets-vests'))
db.clothes_hood.insert_many(create_db('https://www.nike.com/kr/ko_kr/w/women/ap/hoodies-crews'))
db.clothes_pants.insert_many(create_db('https://www.nike.com/kr/ko_kr/w/women/ap/pants-shorts'))
db.clothes_top.insert_many(create_db('https://www.nike.com/kr/ko_kr/w/women/ap/tops-tshirts'))
db.equip.insert_many(create_db('https://www.nike.com/kr/ko_kr/w/w/eq/accessories-equipment'))

db.all.insert_many(create_db('https://www.nike.com/kr/ko_kr/w/women/fw'))
db.all.insert_many(create_db('https://www.nike.com/kr/ko_kr/w/women/ap/jackets-vests'))
db.all.insert_many(create_db('https://www.nike.com/kr/ko_kr/w/women/ap/hoodies-crews'))
db.all.insert_many(create_db('https://www.nike.com/kr/ko_kr/w/women/ap/pants-shorts'))
db.all.insert_many(create_db('https://www.nike.com/kr/ko_kr/w/women/ap/tops-tshirts'))
db.all.insert_many(create_db('https://www.nike.com/kr/ko_kr/w/w/eq/accessories-equipment'))
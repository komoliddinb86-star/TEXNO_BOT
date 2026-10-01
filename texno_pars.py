import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


def pars_texno(category):
    load_dotenv()
    list_products = []
    URL = os.getenv('URL')
    HOST = os.getenv('HOST')
    HEADERS = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
    }

    html = requests.get(URL + category, headers=HEADERS)
    soup = BeautifulSoup(html.text, 'html.parser')

    blocks = soup.find_all('div', class_={'product-item-wrapper'})

    for block in blocks:
        link_image = block.find('a', class_='product-link')
        images = link_image.find('img').get('data-src')
        title = block.find('h2').get_text()
        cred_price = block.find('div', class_='installment-price').get_text(strip=True)
        price = block.find('div', class_='product-price__current').get_text(strip=True)
        link=HOST+block.find('a').get('href')
        print(link)

        list_products.append({
            'title': title,
            'images': images,
            'price': price,
            'cred_price': cred_price,
            'link': link
        })

    return list_products


pars_texno('katalog/nozhi-i-nabory-nozhei/')

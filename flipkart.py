import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.flipkart.com/search?q=laptop'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []

    for product in soup.find_all('div', class_='_1YokD2 _3Mn1Gg'):
        title = product.find('div', class_='_4rR01T').text
        price = product.find('div', class_='_30jeq3').text
        image = product.find('img', class_='_396cs4')['src']
        products.append({'Title': title, 'Price': price, 'Image URL': image})
        
        df = pd.DataFrame(products)
        excel_file = 'flipkart_product.xlsx'
        df.to_excel(excel_file, index=False)

        print(f"Scraped {len(products)} products and saved to {excel_file}")

    else:
        print("Failed to fetched product form the url", response.status_code)

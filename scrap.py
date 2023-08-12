
import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithharry.com/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    #extract the data

    data_elements = soup.find_all('div', class_='flex')

    for elem in data_elements:
        print(elem.text)

    else:
        print("Failed to fetch the website", response.status_code)
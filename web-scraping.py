import requests
from bs4 import BeautifulSoup

url = "https://www.txori.com/dbdevolution"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    elementos = soup.find_all('archive')
    print(len(elementos))
else:
    print("Error al cargar la web, codigo:", response.status_code)
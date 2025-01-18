import requests
from bs4 import BeautifulSoup

url = 'https://mail.google.com/'


response = requests.get(url)


if response.status_code == 200:
 
    soup = BeautifulSoup(response.text, 'html.parser')


    headlines = soup.find_all(['h2', 'h3'])

    for headline in headlines:
        text = headline.get_text(strip=True)
        if text: 
            print(text)
else:
    print(f"Не вдалося завантажити сторінку. Статус код: {response.status_code}")
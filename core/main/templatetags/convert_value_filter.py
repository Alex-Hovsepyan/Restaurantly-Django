from django import template
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36'
}

req = requests.get('https://www.google.com/search?q=usd+into+rubles&rlz=1C1KNTJ_ruAM1063AM1063&oq=usd+into+rubles&aqs=chrome.0.0i512j0i22i30l9.7494j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

soup = BeautifulSoup(req.text, 'lxml')
register = template.Library()

@register.filter
def convert_currency(price, currency_code):
    if currency_code == 'ru':
        return round(price * float(soup.find('span', class_='DFlfde SwHCTb').text.replace(',', '.')), 1)
    else:
         return price
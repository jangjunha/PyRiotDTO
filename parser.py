import requests
from bs4 import BeautifulSoup
from marshmallow import pprint
import json
from datetime import datetime


API_DOCUMENT_URL = 'https://developer.riotgames.com/api/methods'


print "Retrieving Riot API Documents..."
r = requests.get(API_DOCUMENT_URL)
soup = BeautifulSoup(r.text, 'html.parser')

soup_divs = soup.find_all('div', class_='response_body')
soup_dtos = {}
for soup_div in soup_divs:
    key = soup_div.find('b').text
    if key.endswith('Dto') and key not in soup_dtos:
        soup_dtos.update({key: soup_div})
        # print(div.find('b').text)

dtos = {}
for dto_key in soup_dtos:
    soup_trs = soup_dtos[dto_key].find('table').find_all('tr')

    attrs = {}
    for soup_tr in soup_trs:
        soup_tds = soup_tr.find_all('td')
        if len(soup_tds) > 0:
            name = soup_tds[0].text
            data_type = soup_tds[1].text
            description = soup_tds[2].text

            attr = {
                name: {
                    'data_type': data_type,
                    'description': description
                }
            }
            attrs.update(attr)
    dtos.update({dto_key[:-3]: attrs})

time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
filename = 'result_%s.json' % time
with open(filename, 'w') as f:
    json.dump(dtos, f)

print("END. result at %s" % filename)

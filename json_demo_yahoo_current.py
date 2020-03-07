import json
from urllib.request import urlopen

# "https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json" does not work anymore.
with urlopen("https://finance.yahoo.com/currencies") as response:
    source = response.read()

# print(source)

data = json.loads(source)
print(json.dumps(data, indent=2))

print(len(data['list']['resources']))

for item in data['list']['resources']:
    print(item)

usd_rates = dict()
for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(usd_rates['USD/EUR'])
print(50 * usd_rates['USD/EUR'])


for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    print(name, price)


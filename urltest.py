import requests


data = requests.GET('https://api.currencyapi.com/v2/latest?apikey=021ad610-71cb-11ec-9624-3d72d01cd316')

print(data)

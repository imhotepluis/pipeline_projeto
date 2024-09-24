import requests

link_api = "https://restcountries.com/v3.1/all"

requisicao = requests.get(link_api)

print(requisicao.status_code)
print(requisicao.json())
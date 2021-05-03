import requests

url = 'http://bred.com.br/estagiosApp'
sessao = requests.session()
resp = sessao.get(url)
print(resp.text)
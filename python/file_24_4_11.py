import requests
url = 'https://www.sqlsec.com/macsoft.html'
response =requests.get(url)
print(response.text)
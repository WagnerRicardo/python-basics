import urllib.request
url = 'https://www.pudim.com.br'

try:
    ok = urllib.request.urlopen(url)
except Exception as error:
    print(f'\033[0;31mNão foi possível acessar o site {url}')
else:
    print(f'{url} está ok')

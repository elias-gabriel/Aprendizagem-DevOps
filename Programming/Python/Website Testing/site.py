from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def verificasite():
        site = str(input('Digite o site: https://'))
        site = 'https://' + site
        
        req = Request(site)
        try:
            response = urlopen(req)
        except HTTPError as e:
            print('\nO site não respondeu a requisição, site OFF.')
            print('Error code:' ,e.code)
        except URLError as e:
            print('\nNão foi possivel encontrar o servidor, digite uma URL válida.')
            print('Reason:', e.reason)
        else:
            print ('\nO site {} está funcionando.'.format(site))       

if __name__ == "__main__":
    verificasite()

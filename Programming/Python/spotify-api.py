# Spotify API

import requests
import json
import base64 as b64

client_id = ''
client_secret = ''
token = ''

def get_token():
    client_creds = f'{client_id}:{client_secret}'
    client_creds_b64 = b64.b64encode(client_creds.encode())
    url = 'https://accounts.spotify.com/api/token'
    headers = {'Authorization': f'Basic {client_creds_b64.decode()}'}
    data = {'grant_type': 'client_credentials'}
    response = requests.post(url, headers=headers, data=data)
    print(response.json())
    token = response.json()['access_token']

def get_artists(artist_name, token):
    url = 'https://api.spotify.com/v1/search?q=' + artist_name + '&type=artist'
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    json_response = json.loads(response.text)
    with open('artists.json', 'w', encoding='utf-8') as f:
        json.dump(json_response, f, ensure_ascii=False, indent=4)


#get_token()
get_artists('Metallica', token)
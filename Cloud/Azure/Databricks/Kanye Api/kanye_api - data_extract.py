import requests
import json

results = []

def quotes_ye(reads):
    for quotes in range(1, reads + 1):
        url = "https://api.kanye.rest/" + str(quotes)
        print("reading", url)
        response = requests.get(url)
        data = response.json()
        results.append(data)
    with open('ye_quotes.json', 'w', encoding='utf-8') as d:
            json.dump(results, d, ensure_ascii=False, indent=4)
            print('\nFile Saved!!')

quotes_ye(2)
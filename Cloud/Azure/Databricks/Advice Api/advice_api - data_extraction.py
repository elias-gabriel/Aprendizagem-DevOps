import requests
import json

results = []

def advice_data(reads):
    for page_num in range(1, reads + 1):
        url = "https://api.adviceslip.com/advice/" + str(page_num)
        print("\nReading", url)
        response = requests.get(url)
        data = response.json()
        results.append(data)
    print("Total of", len(results), "results")

    with open('advice_data.json', 'w', encoding='utf-8') as d:
        json.dump(results, d, ensure_ascii=False, indent=4)
        print('File Saved!')

advice_data(224)
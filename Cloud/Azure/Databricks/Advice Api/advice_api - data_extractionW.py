import requests
import json
import time

start_time = time.time()
results = set()
url = "https://api.adviceslip.com/advice"

while time.time() - start_time < 30:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        advice = data["slip"]["advice"]
        if advice not in results:
            results.add(advice)
    else:
        break
    print("Elapsed time:", int(time.time() - start_time), "seconds || status code:", response.status_code, "|| Total of:", len(results), "results")

print("Total of", len(results), "results")

with open('advice_data.json', 'w', encoding='utf-8') as d:
    json.dump(list(results), d, ensure_ascii=False, indent=4)
    print('File Saved!')

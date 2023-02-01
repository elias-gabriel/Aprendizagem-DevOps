import requests
import json
import time
import logging

logging.basicConfig(filename="advice_data_logs.log", level=logging.INFO)

url = "https://api.adviceslip.com/advice"
max_results = int(input("Enter the maximum number of results to collect: "))
sleep_time = int(input("Enter the sleep time in seconds between API requests: "))
start_time = time.time()
results = set()

while len(results) < max_results and time.time() - start_time < 30:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            advice = data["slip"]["advice"]
            if advice not in results:
                results.add(advice)
        else:
            logging.error(f"Status code: {response.status_code}")
            break
        elapsed_time = int(time.time() - start_time)
        logging.info(f"Elapsed time: {elapsed_time} seconds || status code: {response.status_code} || Total of: {len(results)} results")
        print(f"Elapsed time: {elapsed_time} seconds || status code: {response.status_code} || Total of: {len(results)} results")
        time.sleep(sleep_time)
    except Exception as e:
        logging.error(f"Error: {e}")
        break

print("Total of", len(results), "results")

with open('advice_data.json.json', 'w', encoding='utf-8') as d:
    json.dump(list(results), d, ensure_ascii=False, indent=4)
    print('File Saved!')

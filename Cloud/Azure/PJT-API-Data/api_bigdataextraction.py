import requests
import json
import time
from datetime import datetime

resultados_totais = []
paginas_totais_para_ler = 11000

# Funcao para buscar os dados de uma pagina especifica
def get_api_data(page_num): 
    url = "https://balldontlie.io/api/v1/stats?per_page=100&page=" + str(page_num)

    current_time = datetime.now().strftime("%H:%M:%S")
    print("{} - Lendo {}".format(current_time, url))
    
    # Guarda o inicio do request
    start_request = datetime.now()
    response = requests.get(url)

    # Calcula o tempo total do request
    end_request = datetime.now()
    delta = end_request - start_request

    # Se o request durou menos de 1 seg, aguardar para nao dar erro
    if delta.seconds <= 0:
        time.sleep(1)

    if response.status_code == 200:
        data = response.json()
        response.raise_for_status()
        return data['data']
    else:
        # Se mesmo assim tivermos erro de request, aguarda 15 segundos e tenta novamente
        current_time = datetime.now().strftime("%H:%M:%S")
        print("{} - ({}) Limite de request ... aguardando 15 seg para tentar novamente".format(current_time, response.status_code))
        time.sleep(15)
        return get_api_data(page_num)

# Loop para todas as paginas..
for page_num in range(1, paginas_totais_para_ler + 1):
    resultados_totais.extend(get_api_data(page_num))
    if page_num == paginas_totais_para_ler:
        print('\nSalvando Arquivo json..')
        with open('test.json', 'w', encoding='utf-8') as d:
            json.dump(resultados_totais, d, ensure_ascii=False, indent=4)
        print('\nArquivo Salvo!!')

print("Temos um total de", len(resultados_totais), "resultados")
import requests
import json
from kakfa_producer_gasolina import send_to_kafka

URL = "https://api.datos.gob.mx/v1/precio.gasolina.publico"

def get_gasolina():
    response = requests.get(URL)
    data = response.json()

    results = data['results']
    for result in results:
        result.pop('_id', None)
        result_json = json.dumps(result)
        #print(type(result_json))
        print(result_json)
        send_to_kafka('gasolinatopic', result_json)

    #print(data)
    #send_to_kafka('gasolinatopic', data)

get_gasolina()
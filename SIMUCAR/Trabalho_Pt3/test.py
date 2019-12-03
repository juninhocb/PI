import requests
from playhouse.shortcuts import dict_to_model
from Dados import *


dados = requests.get('http://thinger.io.bucket.s3-eu-west-1.amazonaws.com/20191130T233255.juninhocb.DadosRPM.K0gud7yC.json')
json_dados = dados.json()
print(json_dados[-1]['val'])



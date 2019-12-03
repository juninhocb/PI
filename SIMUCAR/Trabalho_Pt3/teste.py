from flask import Flask, render_template
import requests
from playhouse.shortcuts import dict_to_model

# simples implementação para teste JSON 

app = Flask(__name__)



@app.route("/")
def teste():
    
    dados_temperatura = requests.get('http://thinger.io.bucket.s3-eu-west-1.amazonaws.com/20191111T231757.juninhocb.temp.XTA2Q6cU.json')
    
    json_temp = dados_temperatura.json()
    
    temperatura = []
    
    for i in json_temp:
        
        temperatura.append(i)
        
    return render_template("teste.html", lista = temperatura)

app.run(debug=True)
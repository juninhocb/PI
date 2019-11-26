from peewee import *
import os

arq = './Dados.DB'
DB = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = DB

class Dados(BaseModel):
    rpm = FloatField()
    vel = FloatField()
    temp = FloatField()
    acel = FloatField()
    dist = FloatField()
    


if __name__ == "__main__":  # se estiver rodando esse programa, executa!  (evita rodar no import)


    if os.path.exists(arq):
        os.remove(arq)
   
    try:
        DB.connect()
        DB.create_tables([Dados])
    except OperationalError as e:
        print('erro ao criar tabela:' +str(e))


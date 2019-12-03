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


D1 = Dados.create(rpm= 2200, vel= 108, temp= 60, acel = 32, dist= 15 )


print('RPM (RPM):')
print(D1.rpm)
print('VELOCIDADE (KM/H):')
print(D1.vel)
print('TEMPERATURA DA AGUA (C°):')
print(D1.temp)
print('POSIÇÃO DO ACELERADOR (%):')
print(D1.acel)
print('DISTÂNCIA PERCORRIDA (KM):')
print(D1.dist)
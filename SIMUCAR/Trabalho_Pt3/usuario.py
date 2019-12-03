
from peewee import *
import os

arq = './Usario.DB'
DB = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = DB

class Usuario(BaseModel):
    nome = CharField()
    sobrenome = CharField()
    sexo = CharField()
    email = CharField()
    telefone = IntegerField()
    cidade = CharField()
    estado = CharField()


if __name__ == "__main__":  # se estiver rodando esse programa, executa!  (evita rodar no import)


    if os.path.exists(arq):
        os.remove(arq)
   
    try:
        DB.connect()
        DB.create_tables([Usuario])
    except OperationalError as e:
        print('erro ao criar tabela:' +str(e))


    marco = Usuario.create(nome = 'Marco', sobrenome = 'Prioto', sexo = 'masculino',
        email = 'm@gmail.com', telefone = '2439', cidade = 'Pirai', estado = 'PR')
    '''joao = Usuario.create(nome = 'Joao', sobrenome = 'Prioto',
        email = 'joao@gmail.com', telefone = '2329', cidade = 'Buri', estado = 'SP')
    caio = Usuario.create(nome = 'Caio', sobrenome = 'Prioto',
        email = 'c@gmail.com', telefone = '2139', cidade = 'Bahia', estado = 'PR')
    marcia = Usuario.create(nome = 'Marcia', sobrenome = 'Prioto',
        email = 'm@gmail.com', telefone = '2111', cidade = 'Pirai', estado = 'PR')
    renato = Usuario.create(nome = 'Renato', sobrenome = 'Prioto',
        email = 'r@gmail.com', telefone = '2454', cidade = 'Buri', estado = 'SP')
    jose = Usuario.create(nome = 'Jose', sobrenome = 'Prioto',
        email = 'j@gmail.com', telefone = '2239', cidade = 'Pirai', estado = 'PR')'''
    


    for u in Usuario.select():
        print('NOME DO USUÁRIO: ')
        print(u.nome)
        print('SOBRENOME DO USUÁRIO ')
        print(u.sobrenome)
        print('SEXO DO USUÁRIO ')
        print(u.sexo)
        print('EMAIL DO USUÁRIO ')
        print(u.email)
        print('TELEFONE DO USUÁRIO ')
        print(u.telefone)
        print('CIDADE DO USUÁRIO ')
        print(u.cidade)
        print('ESTADO DO USUÁRIO ')
        print(u.estado)

       


        
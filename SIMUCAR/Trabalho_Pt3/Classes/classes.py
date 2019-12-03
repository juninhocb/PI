from peewee import *
import os

arq = './classes.DB'
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

class Veiculo(BaseModel):
    marca = CharField()
    modelo = CharField()
    chassi = IntegerField()
    nmrPlaca = CharField()
    ano = IntegerField()

class Fornecedores(BaseModel):
    nome = CharField()

class Informacao(BaseModel):
    tipo = CharField()
    nome = CharField()
    conteudo = CharField()

class Diagnostico(BaseModel):
    infos = ManyToManyField(Informacao)
    estado = CharField()

class Problema(BaseModel):
    nome = CharField()
    possuiManutencao = BooleanField()

class Marca(BaseModel):
    nome = CharField()

class Mecanico(BaseModel):
    usuarios = ForeignKeyField(Usuario)
    preco = FloatField()

class Peca(BaseModel):
    nome = CharField()
    preco = FloatField()

class Engenheiro(BaseModel):
    nome = CharField()
    atribuicao = CharField()
 




if __name__ == "__main__":  # se estiver rodando esse programa, executa!  (evita rodar no import)


    if os.path.exists(arq):
        os.remove(arq)
   
    try:
        DB.connect()
        DB.create_tables([Usuario, Veiculo, Fornecedores,
        Informacao, Diagnostico, Problema, Marca, Mecanico, Peca, Engenheiro, Diagnostico.infos.get_through_model()])
    except OperationalError as e:
        print('erro ao criar tabela:' +str(e))


    fornecedor = Fornecedores.create(nome = 'Marco Peças')
    informacao = Informacao.create(tipo = 'Perigosa', nome = 'Situacao Carburador', conteudo = 'Biela')
    diagnostico = Diagnostico.create(estado = 'Com Falhas')
    informacao2 = Informacao.create(tipo = 'Perigosa', nome = 'Motor', conteudo = 'Problemas de Ignição')
    problemas = Problema.create(nome = 'Suspensão', possuiManutencao = 'FALSE')
    audi = Marca.create(nome = 'Audi')
    peca1 = Peca.create(nome = 'Pistão', preco = '12.2' )
    marco1 = Engenheiro.create (nome = 'Marco Priotto', atribuicao = 'Mecanica')
    marco = Usuario.create(nome = 'Marco', sobrenome = 'Prioto', sexo = 'masculino',
        email = 'm@gmail.com', telefone = '2439', cidade = 'Pirai', estado = 'PR')
    pedrao = Usuario.create(nome = 'Pedrao', sobrenome = 'Prioto', sexo = 'masculino',
        email = 'p@gmail.com', telefone = '423453', cidade = 'Boa Vista', estado = 'RR')
    mecanico = Mecanico.create (usuarios = pedrao , preco = 3)
    informacao2.diagnosticos.add(diagnostico)
    
    veiculo = Veiculo.create(marca = 'Audi', modelo = 'A3', chassi = '3244', nmrPlaca = '2984ZZ', ano = '2014')

    
    #1
    print('Usuarios:')
    for u in Usuario.select():
        print('Nome:', u.nome)
        print('Sobrenome:',u.sobrenome)
        print('Sexo:',u.sexo)
        print('Email',u.email)
        print('Telefone:', u.telefone)
        print('Cidade:', u.cidade)    
        print('Estado:', u.estado)

    #2
    print('\n\n')
    print('Veículos: ')
    for v in Veiculo.select():
        print('Marca:' ,v.marca)
        print('Modelo:' ,v.modelo)
        print('Chassi', v.chassi)
        print('Número da Placa:' ,v.nmrPlaca)
        print('Ano', v.ano)
    #3
    print('\n\n')
    print('Fornecedores:')
    for f in Fornecedores.select():
        print('Nome do Fornecedor:',f.nome)
        
    #4
    print('\n\n')
    print('Informações:')
    for i in Informacao.select():
        print('Tipo de Informacao:',i.tipo)
        print('Nome da Informacao',i.nome)
        print('Conteudo da Informacao',i.conteudo)
    #5
    print('\n\n')
    print('Diagnósticos:')
    for d in Diagnostico.select():
        print('Estado do Diagnostico:' ,d.estado)
        for i in d.infos:
            print('Tipo',i.tipo)
            print('Nome', i.nome)
            print('Conteudo', i.conteudo)
   #6
    print('\n\n')
    print('Problemas:')
    for p in Problema.select():
        print('Nome do Problema:',p.nome)
        if (p.possuiManutencao == 1): 
            print('Possuí Manutenção?:', 'Sim')
        else:
            print('Possuí Manutenção?:', 'Não')
    #7
    print('\n\n')
    print('Marcas:')
    for m in Marca.select():
        print('Nome da Marca:', m.nome)
   #8
    print('\n\n')
    print('Pecas:')
    for pe in Peca.select():
        print('Nome da Peça: ',pe.nome)
    
    #9
    print('\n\n')    
    print('Engenheiros:')
    for e in Engenheiro.select():
        print('Nome:', e.nome)
    
    #10
    print('\n\n')
    print('Mecanicos:')
    for m in Mecanico.select():
        print('Nome:',m.usuarios.nome)
        print('Sobrenome:',m.usuarios.sobrenome)
        print('Sexo:', m.usuarios.sexo)
        print('Email:',m.usuarios.email)
        print('Telefone: ', m.usuarios.telefone)
        print('Cidade:', m.usuarios.cidade)
        print('Estado: ', m.usuarios.estado)
        print('Preço: ', 'R$' + str(m.preco))
        
        

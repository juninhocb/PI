import socket
import sys
import random
from ctypes import *
import time
import obd
import time


def main():
    #incia debug
    obd.logger.setLevel(obd.logging.DEBUG)
    #incia a conexão setando o baudrate correto
    connection = obd.OBD(baudrate=10400, fast=False)
    if connection:
        print('conexão realizada com sucesso, o veículo possui 43 comandos disponíveis')
    else:
        print('conexão com falha')
        
    #instância de variáveis para o socket    
    server_addr = ('localhost', 2300)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if not (s):
        print("Erro ao se conectar")

    try:
        s.connect(server_addr)
        print ("Conectado a %s" % repr(server_addr))
    except:
        print ("ERROR: Conexao para %s recusada" % repr(server_addr))
        sys.exit(1)
    while(1):
        try:      
            rpm = obd.commands.RPM
            vel = obd.commands.SPEED
            temp = obd.commands.COOLANT_TEMP
            acel = obd.commands.THROTTLE_POS
            dist = obd.commands.DISTANCE_W_MIL
            #dtc = obd.commands.GET_DTC

            rrpm = connection.query(rpm)
            rvel = connection.query(vel)
            rtemp = connection.query(temp)
            racel = connection.query(acel)
            rdist = connection.query(dist)
            #rdtc = connection.query(dtc)
           
            
            print ("")
            dados_out = Dados(rrpm, rvel, rtemp, racel, rdist)
            

            print ("Sending rpm=%d, vel=%d, temp=%f, acel=%d, dist=%d, comb=%d, tens=%d, tempamb=%d" % (dados_out.rrpm,
                                                        dados_out.rvel,
                                                        dados_out.rtemp,
                                                        dados_out.racel,
                                                        dados_out.rdist))
            nsent = s.send(dados_out)
            print ("Sent %d bytes" % nsent)

            buff = s.recv(sizeof(dados_out))
            print(buff)
          
        finally:
            print ("Mensagem enviada com sucesso!")
            time.sleep(5)

if __name__ == "__main__":
    main()



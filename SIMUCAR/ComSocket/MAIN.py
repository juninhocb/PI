import socket
import sys
import random
from ctypes import *
import time
import obd
import time

class Dados(Structure):
    _fields_ = [("rrpm", c_float),
                ("rvel", c_float),
                ("rtemp", c_float),
                ("racel", c_float),
                ("rdist", c_float)]

   


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
           
        try: 
            
            x = rrpm.value.magnitude 
            y = rvel.value.magnitude
            w = rtemp.value.magnitude
            z = racel.value.magnitude
            u = rdist.value.magnitude
            print ("")
            #dados_out = Dados(rrpm.value.magnitude,rvel.value.magnitude,rtemp.value.magnitude
             #                 ,racel.value.magnitude,rdist.value.magnitude)
            dados_out = Dados(x, y, w, z, u)
            
            nsent = s.send(dados_out)
            #print ("Sent %d bytes" % nsent)

            buff = s.recv(sizeof(dados_out))
            print(buff)
            print ("Mensagem enviada com sucesso!")
        
        except:
            
            pass
          
        finally:
            
            time.sleep(5)

if __name__ == "__main__":
    main()



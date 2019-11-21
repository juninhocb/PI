import socket
import sys
import random
from ctypes import *
from SENSOR import *
import time

def main():
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
            rpm = OBD_COMMAND_RPM()
            vel = OBD_COMMAND_SPEED()
            temp = OBD_COMMAND_COOLANT_TEMP()
            acel = OBD_COMMAND_THROTTLE_POS()
            dist = OBD_COMMAND_DISTANCE_W_MIL()
            comb = OBD_COMMAND_FUEL_LEVEL()
            tens = OBD_CONTROL_MODULE_VOLTAGE()
            tempamb = OBD_CONTROL_AMBIANT_AIR_TEMP()
           
            print ("")
            dados_out = Dados(rpm.rpm, vel.vel, temp.temp, acel.acel,
            dist.dist, comb.comb, tens.tens, tempamb.tempamb)
            

            print ("Sending rpm=%d, vel=%d, temp=%f, acel=%d, dist=%d, comb=%d, tens=%d, tempamb=%d" % (dados_out.rpm,
                                                        dados_out.vel,
                                                        dados_out.temp,
                                                        dados_out.acel,
                                                        dados_out.dist,
                                                        dados_out.comb,
                                                        dados_out.tens,
                                                        dados_out.tempamb))
            nsent = s.send(dados_out)
            print ("Sent %d bytes" % nsent)

            buff = s.recv(sizeof(dados_out))
            print(buff)
          
        finally:
            print ("Mensagem enviada com sucesso!")
            time.sleep(5)

if __name__ == "__main__":
    main()



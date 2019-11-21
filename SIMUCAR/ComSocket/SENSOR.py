import sys
import random
from ctypes import *
from random import randint


   
class OBD_COMMAND_RPM:
    
    def __init__(self):
        self.rpm = int(randint(1000, 3000))
        
class OBD_COMMAND_SPEED:
    
    def __init__(self):
        self.vel = int(randint(40 , 70))
        
class OBD_COMMAND_COOLANT_TEMP:
    
    def __init__(self):
        self.temp = float(random.uniform(0 , 20))
        
class OBD_COMMAND_THROTTLE_POS:
    
    def __init__(self):
        self.acel = int(randint(0 , 15))

class OBD_COMMAND_DISTANCE_W_MIL:
    
    def __init__(self):
        self.dist = int(randint(5, 60))
        
class OBD_COMMAND_FUEL_LEVEL:
    
    def __init__(self):
        self.comb = int(randint(0 , 100))

class OBD_CONTROL_MODULE_VOLTAGE:
    
    def __init__(self):     
        self.tens = int(randint(11,12))

class OBD_CONTROL_AMBIANT_AIR_TEMP:
    
    def __init__(self):  
        self.tempamb = int(randint(24,25))

class OBD_CONTROL_FUEL_TYPE:
    
    def __init__(self): 
        self.tipocomb = 'Gasolina' 
                           

class Dados(Structure):
    _fields_ = [("rpm", c_int),
                ("vel", c_int),
                ("temp", c_float),
                ("acel", c_int),
                ("dist", c_int),
                ("comb", c_int),
                ("tens", c_int),
                ("tempamb", c_int)]



#rpm = obd.commands.RPM              #UNIDADE RPM
#vel = odb.commands.SPEED            #UNIDADE KM/H
#temp = obd.commands.COOLANT_TEMP    #UNIDADE GRAUS CELSIUS
#acel = obd.commands.THROTTLE_POS    #UNIDADE PORCENTAGEM
#dist = obd.commands.DISTANCE_W_MIL  #UNIDADE KILOMETROS
#comb = obd.commands.FUEL_LEVEL      #UNIDADE PORCENTAGEM
#volt = obd.commands.CONTROL_MODULE_VOLTAGE #UNIDADE VOLT
#ambtemp = obd.commands.AMBIANT_AIR_TEMP #UNIDADE GRAUS CELSIUS
#tipocomb = odd.commands.FUEL_TYPE   #UNIDADE STRING
#obd.commands.GET_DTC  #retorna uma tupla
    
rpm = OBD_COMMAND_RPM()
print(rpm.rpm)

vel = OBD_COMMAND_SPEED()
print(vel.vel)

temp = OBD_COMMAND_COOLANT_TEMP()
print(temp.temp)

acel = OBD_COMMAND_THROTTLE_POS()
print(acel.acel)

dist = OBD_COMMAND_DISTANCE_W_MIL()
print(dist.dist)

comb = OBD_COMMAND_FUEL_LEVEL()
print(comb.comb)

tens = OBD_CONTROL_MODULE_VOLTAGE()
print(tens.tens)

tempamb = OBD_CONTROL_AMBIANT_AIR_TEMP()
print(tempamb.tempamb)
    
    
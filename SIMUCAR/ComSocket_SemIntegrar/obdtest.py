import obd

connection = obd.OBD()
c = obd.commands.CONTROL_MODULE_VOLTAGE
response = connection.query(c)
print(response.value)

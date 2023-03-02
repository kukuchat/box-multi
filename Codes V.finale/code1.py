import pymodbus
from pymodbus.client.serial import ModbusSerialClient as ModbusClient

# Configuration de la connexion
client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600, timeout=1)

# Connexion au périphérique
client.connect()

# Lecture de la température (registre 1 pour la température et 2 pour l'humidité)
result_temp = client.read_input_registers(address=1, count=1, slave=1)
result_hum = client.read_input_registers(address=2, count=1, slave=1)

# Vérification de la réponse
if not result_temp.isError():	
    # Conversion de la valeur de température
    temperature = float(result_temp.registers[0]) / 100.0
    humidity = float(result_hum.registers[0]) / 100.0

    # Affichage de la température
    #print("Temperature : {:.1f} °C".format(temperature))
    #print("Humidity : {:.1f} %".format(humidity))
else:
    print("Erreur : {}".format(result_temp))
    print("Erreur : {}".format(result_hum))

# Conversion des données du capteur en string
str_data_temp = str(temperature)
str_data_hum = str(humidity)

# Création d'un fichier 
fichier = open('data_modbus.txt', 'a')

fichier.write("Temperature= "+str_data_temp+"°C"+'\n')
fichier.write("Humidity= "+str_data_hum+" %"+'\n')
fichier.close()	

# Fermeture de la connexion sur le port serial
client.close()

import bme680
import time
import datetime
import csv
import mysql.connector as mariadb

hostname = "localhost"      #Probably localhost
username = "user"           #User assigned to database
password = "ChangeMe"       #Password assigned to above user
database_name = "db_name"   #Name of database
table_name = "table_name"   #Name of table
print2screen = True         #Display readings in Terminal
write2CSV = True            #Record readings in commer seperated value local file
write2db = True             #Record readings to SQL database
sensor_interval = 60        #How often a reading is taken


try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY) #I2C_ADDR_PRIMARY is (0x76) 
except IOError:
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY) #I2C_ADDR_SECONDARY is (0x77)

#Sensitivity settings
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS) 

sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)
 
if write2CSV == True:
    with open(r'BME680CSV','w+') as f: #w means write to file, + means create file if it doesn't exist
        writer = csv.writer(f)
        writer.writerow(['Date Time (YYYY-MM-DD HH:MM:SS)','Temperature (deg C)','Pressure (hPa)','Humidity (%)','Gas Resistance (Ohms)']) #CSV file headers

if write2db == True:
    db = mariadb.connect(host=hostname,user=username, password=password,db=database_name) #Connects to MariaDB
    cur = db.cursor() #Creates cursor to pass on demands to MySQL/MariaDB
 
while True: #Collects data indefinitely
 
    degrees = sensor.data.temperature #Celsius
    pascals = sensor.data.pressure
    hectopascals = pascals / 100
    humidity = sensor.data.humidity
    gas = sensor.data.gas_resistance
    timenow = datetime.datetime.utcnow()
    
    if write2db == True:
        #Executes the SQL command in MySQL/MariaDB to insert data.
        cur.execute('''INSERT INTO '''+table_name+'''(date_time, temperature, pressure, humidity, gas) VALUES(%s,%s,%s,%s,%s);''',(timenow,degrees,hectopascals,humidity,gas))      
        db.commit() #commits the data entered above to the table
 
    if write2CSV == True:
        with open(r'BME680CSV', 'a') as f: #a means append to file
            writer = csv.writer(f)
            writer.writerow([timenow,degrees,pascals,humidity,gas]) 

    if print2screen == True:
        print ('Time      = ' + str(timenow))
        print ('Temp      = {0:0.3f} \N{DEGREE SIGN}C'.format(degrees)) #°C
        print ('Pressure  = {0:0.2f} hPa'.format(hectopascals))
        print ('Humidity  = {0:0.2f} %'.format(humidity))
        print ('Gas       = {0:0.2f} %'.format(gas))
 
    time.sleep(sensor_interval) #Waits for X seconds to collect data again

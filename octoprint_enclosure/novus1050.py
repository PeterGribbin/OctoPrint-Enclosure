#!/usr/bin/env python3
import minimalmodbus

## setup ##
 # port name, slave address (in decimal)
novus = minimalmodbus.Instrument('/dev/ttyUSB0', 1) 
# for Novus 1050 comms documentation see:
# https://cdn.novusautomation.com/downloads/registers_table_n1050_v11x_a_en.pdf
# rs485 to USB adaptor: USB to RS485 TTL Serial Converter Adapter FTDI interface FT232RL 75176 Module
novus.serial.baudrate = 115200
REG_ADDR = {
    'Active SP': 0,
    'PV': 1,
    'dppo': 73
}
## Read decimal point precision setting ##
DP = 3 - novus.read_register(REG_ADDR['dppo'], 0)
#print(f'decimal places: {DP}')
## set up complete ##

class Novus1050Temp:
    def getTemp(self):
        temperature = novus.read_register(REG_ADDR['PV'], DP)
        return '{0:0.1f}'.format(temperature)

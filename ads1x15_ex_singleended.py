#!/usr/bin/python
import csv
import time, signal, sys
from Adafruit_ADS1x15 import ADS1x15
import threading

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
	w.close()
        sys.exit(0)

with open(sys.argv[1], 'wt') as f:
	w = csv.writer(f)
w.writerow(["CO2", "TEMP"])

adc = ADS1x15(ic=0x00)
def read():
	t = threading.Timer(30, read)
	global i
	i += 1
	adc = ADS1x15(ic=0x00)
	CO2 = adc.readADCSingleEnded(0, 4096, 250)
	Temperature = adc.readADCSingleEnded(1, 4096, 250)
	print(str(Temperature) + " " + u"\u00B0" + "C")
	print(str(CO2) + " mV")
	w.writerow([str(CO2), str(Temperature)])
	if(i == 120):
		t.cancel()
		w.close()
		print("Data got!")
	t.start()
i = 0
read()


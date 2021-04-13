import minimalmodbus
import time
import sys, os, io

sleepTime = 10

try:
    inv = minimalmodbus.Instrument('/dev/ttyUSB0', 10) # port name, slave address (in decimal)
    inv.serial.baudrate = 9600
    inv.serial.timeout  = 0.2
except:
    print("Inverter not found.")

def readINV(fileObj):
    try:
        batVolts = inv.read_register(30014, 1)
        time.sleep(0.2)
        valName  = "mode=\"batVolts\""
        valName  = "{" + valName + "}"
        dataStr  = f"MUST_INV{valName} {batVolts}"
        print(dataStr, file=fileObj)

        batAmps = inv.read_register(30015, 1)
        time.sleep(0.2)
        valName  = "mode=\"batAmps\""
        valName  = "{" + valName + "}"
        dataStr  = f"MUST_INV{valName} {batAmps}"
        print(dataStr, file=fileObj)

        loadPercent = inv.read_register(30012, 0)
        time.sleep(0.2)
        valName  = "mode=\"loadPercent\""
        valName  = "{" + valName + "}"
        dataStr  = f"MUST_INV{valName} {loadPercent}"
        print(dataStr, file=fileObj)

        outputVA = inv.read_register(30011, 0)
        time.sleep(0.2)
        valName  = "mode=\"outputVA\""
        valName  = "{" + valName + "}"
        dataStr  = f"MUST_INV{valName} {outputVA}"
        print(dataStr, file=fileObj)

        outputW = inv.read_register(30010, 0)
        time.sleep(0.2)
        valName  = "mode=\"outputW\""
        valName  = "{" + valName + "}"
        dataStr  = f"MUST_INV{valName} {outputW}"
        print(dataStr, file=fileObj)

        tempInt = inv.read_register(30018, 0)
        time.sleep(0.2)
        valName  = "mode=\"tempInt\""
        valName  = "{" + valName + "}"
        dataStr  = f"MUST_INV{valName} {tempInt}"
        print(dataStr, file=fileObj)

    except:
        print("MUST INV: off.")


while True:
    file_object = open('/ramdisk/MUST_INV.prom.tmp', mode='w')
    readINV(file_object)
    file_object.flush()
    file_object.close()
    outLine = os.system('/bin/mv /ramdisk/MUST_INV.prom.tmp /ramdisk/MUST_INV.prom')
    
    time.sleep(sleepTime)


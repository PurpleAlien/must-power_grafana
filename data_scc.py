import minimalmodbus
import time
import sys, os, io

sleepTime = 10

try:
    scc = minimalmodbus.Instrument('/dev/ttyUSB0', 1) # port name, slave address (in decimal)
    scc.serial.baudrate = 9600
    scc.serial.timeout  = 0.2
except:
    print("SCC  not found.")


def readSCC(fileObj):
    # first SCC
    try:
        soc = scc.read_register(15223,0)
        time.sleep(0.2)
        valName  = "mode=\"SOC\""
        valName  = "{" + valName + "}"
        dataStr  = f"MUST_SCC{valName} {soc}"
        print(dataStr, file=fileObj)

        batVolts = scc.read_register(15206,1)
        time.sleep(0.2)
        valName  = "mode=\"batVolts\""
        valName  = "{" + valName + "}"
        dataStr  = f"MUST_SCC{valName} {batVolts}"
        print(dataStr, file=fileObj)

        pvVolts = scc.read_register(15205,1)
        time.sleep(0.2)
        valName  = "mode=\"pvVolts\""
        valName  = "{" + valName + "}"
        dataStr  = f"MUST_SCC{valName} {pvVolts}"
        print(dataStr, file=fileObj)

        pvAmps = scc.read_register(15207,1)
        time.sleep(0.2)
        valName  = "mode=\"pvAmps\""
        valName  = "{" + valName + "}"
        dataStr  = f"MUST_SCC{valName} {pvAmps}"
        print(dataStr, file=fileObj)

        loadWatts = scc.read_register(15208,0)
        time.sleep(0.2)
        valName  = "mode=\"loadWatts\""
        valName  = "{" + valName + "}"
        dataStr  = f"MUST_SCC{valName} {loadWatts}"
        print(dataStr, file=fileObj)

        sccTemp = scc.read_register(15209,0)
        time.sleep(0.2)
        valName  = "mode=\"sccTemp\""
        valName  = "{" + valName + "}"
        dataStr  = f"MUST_SCC{valName} {sccTemp}"
        print(dataStr, file=fileObj)

        batTemp = scc.read_register(15210,0)
        time.sleep(0.2)
        valName  = "mode=\"batTemp\""
        valName  = "{" + valName + "}"
        dataStr  = f"MUST_SCC{valName} {batTemp}"
        print(dataStr, file=fileObj)

        upDays = scc.read_register(15219,0)
        time.sleep(0.2)
        valName  = "mode=\"upDays\""
        valName  = "{" + valName + "}"
        dataStr  = f"MUST_SCC{valName} {upDays}"
        print(dataStr, file=fileObj)


    except:
        print("MUST SCC: off.")

while True:
    file_object = open('/ramdisk/MUST_SCC.prom.tmp', mode='w')
    readSCC(file_object)
    file_object.flush()
    file_object.close()
    outLine = os.system('/bin/mv /ramdisk/MUST_SCC.prom.tmp /ramdisk/MUST_SCC.prom')
    
    time.sleep(sleepTime)


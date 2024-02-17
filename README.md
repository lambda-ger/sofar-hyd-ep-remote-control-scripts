# sofar-hyd-ep-remote-control-scripts
Ready to go scripts for implementation in e.g. NodeRed

#howto
first you need to install minimalmodbus and pyserial

The port must be set up in each file
port = "/dev/ttyUSB0"

# set inverter to standby
python3 ./standby.py
you can also activate "full standby" in the file.

A full standby saves energy, but the inverter takes much longer until it can run at full power again. (up to 15 minutes)

# set inverter to automatic
python3 ./auto.py

# set inverter to charge
python3 ./charge.py

or

python3 ./charge.py 1000

if no value is specified, 5000 watts is assumed
(can be changed in the file)

# set inverter to discharge
python3 ./discharge.py

or

python3 ./discharge.py 1000

if no value is specified, 5000 watts is assumed
(can be changed in the file)

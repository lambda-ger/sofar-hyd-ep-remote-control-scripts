import minimalmodbus
import serial
import struct
import time
import sys


# adjust here
port = "/dev/ttyUSB1"
power = 5000  # when no command is send, use 5000 watt

# if a power is set, override the config

if len(sys.argv) > 1:
    power = int(sys.argv[1])

power = 0 - power
instrument = minimalmodbus.Instrument(port, 1, debug=False)  # port name, slave address
instrument.serial.baudrate = 9600  # Baud
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 0.5  # seconds
instrument.mode = minimalmodbus.MODE_RTU
instrument.clear_buffers_before_each_transaction = True

def manual(power=0):
    try:
        current = 9  # override the "current" state
        # we need an active passiv mode first
        # read the current state
        current = instrument.read_register(4368)
        time.sleep(0.2)
        # if not 3 (passiv mode) set it to 3
        if current != 3:
            instrument.write_register(4368, 3)
            time.sleep(0.2)

        # prepare the power value
        values = struct.pack(">l", power)
        # split low and high byte
        low = struct.unpack(">H", bytearray([values[0], values[1]]))[0]
        high = struct.unpack(">H", bytearray([values[2], values[3]]))[0]

        # send the registers
        instrument.write_registers(4487, [0, 0, low, high, low, high])
        time.sleep(0.1)
    except:
        print("Fault send command...")

manual(power)
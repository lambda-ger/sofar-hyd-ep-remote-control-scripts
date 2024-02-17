import minimalmodbus
import serial
import time


# adjust here
port = "/dev/ttyUSB1"


instrument = minimalmodbus.Instrument(port, 1, debug=False)  # port name, slave address
instrument.serial.baudrate = 9600  # Baud
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 0.5  # seconds
instrument.mode = minimalmodbus.MODE_RTU
instrument.clear_buffers_before_each_transaction = True


def auto():
    try:
        current = instrument.read_register(4368)
        time.sleep(0.1)
        if current != 0:
            # if controlstatus is not 0 (auto) set it to 0
            instrument.write_register(4368, 0)
            time.sleep(0.1)
    except:
        print("fault send command...")

auto()
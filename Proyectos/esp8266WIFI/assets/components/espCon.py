from pyModbusTCP.client import ModbusClient # type: ignore #pip install pyModbusTCP
import time


class espWifi():
    def __init__(self):
        self.serverHost = "192.168.1.78"
        self.serverPort = 502

        #   Registros que se usaran
        # ledCoil = 0
        # dataReg = 0
    def open_esp(self):

        self.client = ModbusClient(
            host=self.serverHost,
            port=self.serverPort,
            auto_open=True
        )

    def close_esp(self):
        self.client.close()
    
    # def read_esp(self):
    #     #a = client.read_coils(ledCoil,1)    
    #     b = self.client.read_discrete_inputs(0,1)

    #     #c = client.read_holding_registers(dataReg,1)
    #     d = self.client.read_input_registers(dataReg,1)

    # def write_esp(self):
    #     self.client.write_single_coil(ledCoil,a)

    #     self.client.write_single_register(dataReg,d)

    
    
    
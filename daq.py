from abc import ABC, abstractmethod

from nidaqmx.system import System
from nidaqmx.task import Task

class Controller(ABC):

    def __init__(self):
        self.open = False
        self.channels = {}

    @abstractmethod
    def start(self) -> bool:
        """
        Starts the measuring process
        """
        pass

    @abstractmethod
    def read(self) -> list[float]:
        """
        Takes a sample from the channel
        """
        pass
    
    @staticmethod
    def scan_for_devices() -> list[str]:
        """
        Scans for any connected NI DAQ Devices
        """
        return System.local().devices.device_names
    
class RTDController(Controller):

    def __init__(self):
        """
        A controller for the DAQ
        """
        self.channels = {
            "amb": "",
            "heater": "",
        }

    def set_amb_channel(self, channel : str):
        """
        Set the analog input channel for RTD ambient
        """
        self.open = False
        self.channels["amb"] = channel

    def set_heater_channel(self, channel : str):
        """
        Set the analog input channel for RTD heater
        """
        self.open = False
        self.channels["heater"] = channel

    def start(self):
        # Validate start up
        if "" in self.channels.values():
            return False
        
        # Task Creation
        self._rtd_task = Task()

        # Channels
        self._rtd_task.ai_channels.add_ai_rtd_chan(self.channels["amb"], min_val=-30, max_val=300)
        self._rtd_task.ai_channels.add_ai_rtd_chan(self.channels["heater"], min_val=-30, max_val=300)

        # Success
        self.open = True
        return True
    
    def read(self):
        # Validate
        if not self.open:
            return []
        
        # Read
        rtd_data : list[float] = self._rtd_task.read()

        # Return
        return list(rtd_data)
    
class VoltageController(Controller):

    def __init__(self):
        """
        A controller for the DAQ
        """
        self.channels = {
            "humidity": "",
            "pressure": "",
            "resistance": "",
            "power": ""
        }
        self.ref_resistor = 100.0 # Ohms

    def set_humidity_channel(self, channel : str):
        """
        Set the analog input channel for humidity
        """
        self.open = False
        self.channels["humidity"] = channel

    def set_pressure_channel(self, channel : str):
        """
        Set the analog input channel for pressure
        """
        self.open = False
        self.channels["pressure"] = channel

    def set_resistance_channel(self, channel : str):
        """
        Set the analog input channel for resistance
        """
        self.open = False
        self.channels["resistance"] = channel

    def set_power_channel(self, channel : str):
        """
        Set the analog input channel for power
        """
        self.open = False
        self.channels["power"] = channel

    def set_ref_resistor(self, resistor : float):
        """
        Sets the reference resistor
        """
        self.ref_resistor = resistor

    def start(self) -> bool:
        # Validate start up
        if "" in self.channels.values():
            return False
        
        # Making DAQ task
        self._v_task = Task()

        # Setup
        self._v_task.ai_channels.add_ai_voltage_chan(self.channels["humidity"])
        self._v_task.ai_channels.add_ai_voltage_chan(self.channels["pressure"], max_val=6)
        self._v_task.ai_channels.add_ai_voltage_chan(self.channels["resistance"])
        self._v_task.ai_channels.add_ai_voltage_chan(self.channels["power"])

        # Success
        self.open = True
        return True
    
    def read(self) -> list[float]:
        # Validate
        if not self.open:
            return []
        
        # Read
        v_data : list[float] = self._v_task.read()

        # Process Resistance
        resistance = v_data[2]*self.ref_resistor/(v_data[3] - v_data[2])

        # Return
        return [*v_data[:2], resistance]
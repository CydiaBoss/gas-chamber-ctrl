from nidaqmx.system import System
        
def scan_for_devices() -> list[str]:
    """
    Scans for any connected NI DAQ Devices
    """
    return System.local().devices.device_names

class RTDController():

    def __init__(self, device : str):
        """
        A controller for the DAQ's RTD
        """
        self.device = device

    def set_channel(self, channel : str):
        """
        Set the main analog input channel
        """
        self.channel = channel

    def start(self):
        """
        Start the data reading process
        """
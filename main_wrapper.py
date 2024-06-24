from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QCoreApplication

from pglive.kwargs import Axis
from pglive.sources.live_axis import LiveAxis
from pglive.sources.live_plot import LiveLinePlot
from pglive.sources.data_connector import DataConnector

import numpy as np

from main_gui import Ui_MainWindow

from constants import *

# Translating Function
_t = lambda x="" : QCoreApplication.translate("MainWindow", x)

class Window(Ui_MainWindow, QMainWindow):

    def __init__(self):
        """
        MainWindow wrapper
        """
        super().__init__(None)

        self.setupUi(self)

        self.setup_plots()

    def setup_plots(self):
        """
        Setup the plots
        """
        # Setup Background
        self.temp_plot.setBackground("w")
        self.humidity_plot.setBackground("w")
        self.pressure_plot.setBackground("w")
        self.resistance_plot.setBackground("w")

        # Setup Labels
        self.temp_plot.getPlotItem().setLabels(title=_t("Temperature"))
        self.humidity_plot.getPlotItem().setLabels(title=_t("Humidity"))
        self.pressure_plot.getPlotItem().setLabels(title=_t("Pressure"))
        self.resistance_plot.getPlotItem().setLabels(title=_t("Resistance")) 
        
        # Setup Axis Items
        self.temp_time_axis = LiveAxis(orientation="bottom", tick_angle=-45, Tick_Format=Axis.DURATION)
        self.temp_time_axis.setLabel(text=_t("Time"), units="s")

        self.temp_axis = LiveAxis(orientation="left")
        self.temp_axis.setLabel(text=_t("Temperature"), units="°C")
        
        self.humidity_time_axis = LiveAxis(orientation="bottom", tick_angle=-45, Tick_Format=Axis.DURATION)
        self.humidity_time_axis.setLabel(text=_t("Time"), units="s")

        self.humidity_axis = LiveAxis(orientation="left")
        self.humidity_axis.setLabel(text=_t("Humidity"), units="%RH")
        
        self.pressure_time_axis = LiveAxis(orientation="bottom", tick_angle=-45, Tick_Format=Axis.DURATION)
        self.pressure_time_axis.setLabel(text=_t("Time"), units="s")

        self.pressure_axis = LiveAxis(orientation="left")
        self.pressure_axis.setLabel(text=_t("Pressure"), units="psi")
        
        self.resistance_time_axis = LiveAxis(orientation="bottom", tick_angle=-45, Tick_Format=Axis.DURATION)
        self.resistance_time_axis.setLabel(text=_t("Time"), units="s")

        self.resistance_axis = LiveAxis(orientation="left")
        self.resistance_axis.setLabel(text=_t("Resistance"), units="Ω", unitPrefix="k")

        self.temp_plot.getPlotItem().setAxisItems({
            "left": self.temp_axis,
            "bottom": self.temp_time_axis
        })

        self.humidity_plot.getPlotItem().setAxisItems({
            "left": self.humidity_axis,
            "bottom": self.humidity_time_axis
        })

        self.pressure_plot.getPlotItem().setAxisItems({
            "left": self.pressure_axis,
            "bottom": self.pressure_time_axis
        })

        self.resistance_plot.getPlotItem().setAxisItems({
            "left": self.resistance_axis,
            "bottom": self.resistance_time_axis
        })
        
        # Setup Legend for Temperature
        self.temp_legend = self.temp_plot.getPlotItem().addLegend()

        # Setup Line Plot
        self.temp_amp_line = LiveLinePlot(pen="b", name=_t("Ambient"))
        self.temp_heater_line = LiveLinePlot(pen="r", name=_t("Heater"))
        self.temp_plot.addItem(self.temp_amp_line)
        self.temp_plot.addItem(self.temp_heater_line)
        self.humidity_line = LiveLinePlot(pen="g", name=_t("Humidity"))
        self.humidity_plot.addItem(self.humidity_line)
        self.pressure_line = LiveLinePlot(pen="c", name=_t("Pressure"))
        self.pressure_plot.addItem(self.pressure_line)
        self.resistance_line = LiveLinePlot(pen="m", name=_t("Resistance"))
        self.resistance_plot.addItem(self.resistance_line)

        # Setup Data Connectors
        self.temp_amb_data = DataConnector(self.temp_amp_line)
        self.temp_heater_data = DataConnector(self.temp_heater_line)
        self.humidity_data = DataConnector(self.humidity_line)
        self.pressure_data = DataConnector(self.pressure_line)
        self.resistance_data = DataConnector(self.resistance_line)

    def setup_variables(self):
        """
        Setups all the variables for the software
        """
        # Connection Related
        self.device = ""
        self.channels = {
            "temp_amb": "",
            "temp_heater": "",
            "humidity": "",
            "pressure": "",
            "resistance": ""
        }

        # Calculation Related
        self.reference_resistor = 100.0 # Ohms

        # Data Storage
        self.temp_amb_data_store = np.array([])
        self.temp_heater_data_store = np.array([])
        self.humidity_data_store = np.array([])
        self.pressure_data_store = np.array([])
        self.resistance_data_store = np.array([])
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QCoreApplication

from pglive.sources.live_axis import LiveAxis
from pglive.sources.live_plot import LiveLinePlot

from main_gui import Ui_MainWindow

from constants import *

# Translating Function
_t = lambda x="" : QCoreApplication.translate("MainWindow", x)

class Window(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super().__init__(None)

        self.setupUi(self)

        self.setup_plots()

    def setup_plots(self):
        """
        Setup the plots
        """
        # Setup Legend (Temp)
        self.temp_legend = self.temp_plot.getPlotItem().addLegend()

        # Setup Background
        self.temp_plot.setBackground("w")
        self.humidity_plot.setBackground("w")
        self.pressure_plot.setBackground("w")
        self.resistance_plot.setBackground("w")

        # Setup Axis Items
        self.temp_plot.getPlotItem().setAxisItems({
            "left": LiveAxis(orientation="left", text=_t("Temperature"), units="degC"),
            "bottom": LiveAxis(text=_t("Time"), **TIME_AXIS_CONFIG)
        })

        self.humidity_plot.getPlotItem().setAxisItems({
            "left": LiveAxis(orientation="left", text=_t("Humidity"), units="%RH"),
            "bottom": LiveAxis(text=_t("Time"), **TIME_AXIS_CONFIG)
        })

        self.pressure_plot.getPlotItem().setAxisItems({
            "left": LiveAxis(orientation="left", text=_t("Pressure"), units="psi"),
            "bottom": LiveAxis(text=_t("Time"), **TIME_AXIS_CONFIG)
        })

        self.resistance_plot.getPlotItem().setAxisItems({
            "left": LiveAxis(orientation="left", text=_t("Resistance"), units="Ohm"),
            "bottom": LiveAxis(text=_t("Time"), **TIME_AXIS_CONFIG)
        })

        # Setup Labels
        self.temp_plot.getPlotItem().setLabels(title=_t("Temperature"), left=_t("Temperature"), bottom=_t("Time"))
        self.humidity_plot.getPlotItem().setLabels(title=_t("Humidity"), left=_t("Humidity"), bottom=_t("Time"))
        self.pressure_plot.getPlotItem().setLabels(title=_t("Pressure"), left=_t("Pressure"), bottom=_t("Time"))
        self.resistance_plot.getPlotItem().setLabels(title=_t("Resistance"), left=_t("Resistance"), bottom=_t("Time")) 

        # Setup Line Plot
        self.temp_amp_line = LiveLinePlot(pen="b", label=_t("Ambient"))
        self.temp_heater_line = LiveLinePlot(pen="r", label=_t("Heater"))
        self.temp_plot.addItem(self.temp_amp_line)
        self.temp_plot.addItem(self.temp_heater_line)
        self.humidity_line = LiveLinePlot(pen="g", label=_t("Humidity"))
        self.humidity_plot.addItem(self.humidity_line)
        self.pressure_line = LiveLinePlot(pen="r", label=_t("Pressure"))
        self.pressure_plot.addItem(self.pressure_line)
        self.resistance_line = LiveLinePlot(pen="r", label=_t("Resistance"))
        self.resistance_plot.addItem(self.resistance_line)
from PyQt5.QtGui import QCloseEvent, QRegExpValidator, QPixmap
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import QCoreApplication, QRegExp, pyqtSlot

from pglive.kwargs import Axis
from pglive.sources.live_axis import LiveAxis
from pglive.sources.live_plot import LiveLinePlot
from pglive.sources.data_connector import DataConnector

import numpy as np

import os

from daq import RTDController, VoltageController
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

        self.setup_variables()

        self.setup_validations()

        self.setup_signals()

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
        self.temp_legend.setPen("k")

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
        self.time_data_store = np.array([], dtype=np.floating)
        self.temp_amb_data_store = np.array([], dtype=np.floating)
        self.temp_heater_data_store = np.array([], dtype=np.floating)
        self.humidity_data_store = np.array([], dtype=np.floating)
        self.pressure_data_store = np.array([], dtype=np.floating)
        self.resistance_data_store = np.array([], dtype=np.floating)

        # Controllers
        self.rtd_ctrl : RTDController = None
        self.v_ctrl : VoltageController = None

        # Heater
        self.heater_status = False
        self.measure_status = False
        self.record_status = False

    def setup_validations(self):
        """
        Add validation masks to inputs
        """
        # Temperature Validator
        temp_input_validator = QRegExpValidator(QRegExp("\d+(\.\d+)?"), self.heater_value)
        self.heater_value.setValidator(temp_input_validator)

        # Frequency Validator
        freq_temp_validator = QRegExpValidator(QRegExp("\d+(\.\d+)?"), self.freq_value)
        self.freq_value.setValidator(freq_temp_validator)

    def setup_signals(self):
        """
        Setup signal connections
        """
        # Heater Button Activity
        self.heater_value.textChanged.connect(self.heater_btn_status)

        # Record Button Activity
        self.freq_value.textChanged.connect(self.record_btn_status)
        self.file_dest.textChanged.connect(self.record_btn_status)

    # Events
    def closeEvent(self, a0: QCloseEvent | None) -> None:
        """
        Add confirmation to closing
        """
        confirm = QMessageBox.question(self, _t("Confirmation"), _t("Are you sure you want to close this application?"), QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        # Cancel closing if so
        if confirm == QMessageBox.StandardButton.No:
            a0.ignore()
            return

        return super().closeEvent(a0)

    # Slots
    @pyqtSlot()
    def on_action_Quit_triggered(self):
        self.close()

    @pyqtSlot()
    def heater_btn_status(self):
        """
        Should heater btn be unlocked
        """
        self.heater_toggle.setEnabled(self.heater_value.text() != "")

    @pyqtSlot()
    def on_heater_toggle_clicked(self):
        """
        Enable to disable heater
        """
        if self.heater_status:
            self.heater_toggle.setText(_t("Start Heater"))
            self.heat_status_icon.setPixmap(QPixmap(":/status/cross.png"))
            self.heater_value.setEnabled(True)
            self.heater_status = False
        else:
            self.heater_toggle.setText(_t("Stop Heater"))
            self.heat_status_icon.setPixmap(QPixmap(":/status/check.png"))
            self.heater_value.setEnabled(False)
            self.heater_status = True

    @pyqtSlot()
    def on_start_meas_btn_clicked(self):
        """
        Start button logic
        """
        self.start_meas_btn.setEnabled(False)

        # Process

        self.measure_status = True
        self.stop_meas_btn.setEnabled(True)
        self.meas_status_icon.setPixmap(QPixmap(":/status/check.png"))

        # Trigger Update
        self.record_btn_status()

    @pyqtSlot()
    def on_stop_meas_btn_clicked(self):
        """
        Stop button logic
        """
        # Check for recording
        if self.record_status:
            self.statusBar().showMessage(_t("Cannot stop measuring while recording"))
            return

        # Confirm 
        if QMessageBox.question(self, _t("Confirmation"), _t("Are you sure you want to stop measuring data?"), QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No) == QMessageBox.StandardButton.No:
            return
        
        self.stop_meas_btn.setEnabled(False)

        # Process

        self.measure_status = False
        self.start_meas_btn.setEnabled(True)
        self.meas_status_icon.setPixmap(QPixmap(":/status/cross.png"))

        # Trigger Update
        self.record_btn_status()

    @pyqtSlot()
    def record_btn_status(self):
        """
        Should record btn be unlocked
        """
        self.record_btn.setEnabled(self.freq_value.text() != "" and self.file_dest.text().endswith(".csv") and self.measure_status)

    @pyqtSlot()
    def on_record_btn_clicked(self):
        """
        Record button logic
        """
        # If On
        if self.record_status:
            # Confirm 
            if QMessageBox.question(self, _t("Confirmation"), _t("Are you sure you want to stop recording data?"), QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No) == QMessageBox.StandardButton.No:
                return
            
            self.record_btn.setText(_t("Start Recording"))
            self.record_status = False
            self.record_status_icon.setPixmap(QPixmap(":/status/cross.png"))
            self.freq_value.setEnabled(True)
            self.freq_unit.setEnabled(True)
            self.file_dest.setEnabled(True)

            self.statusBar().showMessage(_t("Recording stopped"), 5000)

        # If Off
        else:
            self.record_btn.setText(_t("Stop Recording"))
            self.record_status = True
            self.record_status_icon.setPixmap(QPixmap(":/status/check.png"))
            self.freq_value.setEnabled(False)
            self.freq_unit.setEnabled(False)
            self.file_dest.setEnabled(False)

            self.statusBar().showMessage(_t("Recording started"), 5000)

    @pyqtSlot()
    def on_file_btn_clicked(self):
        """
        Open File Explorer for file saving location
        """
        # Get current file directory
        dir_name = os.path.dirname(self.file_dest.text())

        # Ask for file destination
        save_dest = QFileDialog.getSaveFileName(self, _t("Choose a destination to save the file"), dir_name, "CSV (*.csv)")

        # If no file selected
        if save_dest[0].strip() == "":
            self.statusBar().showMessage(_t("No file destination selected"), 5000)
            return
        
        # Save file path
        self.file_dest.setText(save_dest[0].strip())
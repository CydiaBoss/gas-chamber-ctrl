# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/gas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.record_panel = QtWidgets.QFrame(self.centralwidget)
        self.record_panel.setMaximumSize(QtCore.QSize(16777215, 175))
        self.record_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.record_panel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.record_panel.setObjectName("record_panel")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.record_panel)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_14 = QtWidgets.QLabel(self.record_panel)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_9.addWidget(self.label_14, 0, 0, 1, 5)
        self.label_13 = QtWidgets.QLabel(self.record_panel)
        self.label_13.setObjectName("label_13")
        self.gridLayout_9.addWidget(self.label_13, 1, 0, 1, 1)
        self.freq_value = QtWidgets.QLineEdit(self.record_panel)
        self.freq_value.setObjectName("freq_value")
        self.gridLayout_9.addWidget(self.freq_value, 1, 1, 1, 1)
        self.freq_unit = QtWidgets.QComboBox(self.record_panel)
        self.freq_unit.setObjectName("freq_unit")
        self.freq_unit.addItem("")
        self.freq_unit.setItemText(0, "Hz")
        self.freq_unit.addItem("")
        self.freq_unit.setItemText(1, "kHz")
        self.freq_unit.addItem("")
        self.freq_unit.setItemText(2, "MHz")
        self.freq_unit.addItem("")
        self.freq_unit.setItemText(3, "GHz")
        self.gridLayout_9.addWidget(self.freq_unit, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.record_panel)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_9.addWidget(self.pushButton, 1, 3, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.record_panel)
        self.label_16.setObjectName("label_16")
        self.gridLayout_9.addWidget(self.label_16, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.record_panel)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_9.addWidget(self.lineEdit, 2, 1, 1, 3)
        self.toolButton = QtWidgets.QToolButton(self.record_panel)
        self.toolButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_9.addWidget(self.toolButton, 2, 4, 1, 1)
        self.gridLayout_10.addWidget(self.record_panel, 2, 2, 1, 1)
        self.meas_panel = QtWidgets.QFrame(self.centralwidget)
        self.meas_panel.setMaximumSize(QtCore.QSize(16777215, 175))
        self.meas_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.meas_panel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.meas_panel.setObjectName("meas_panel")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.meas_panel)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_9 = QtWidgets.QLabel(self.meas_panel)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 0, 0, 1, 2)
        self.start_meas_btn = QtWidgets.QPushButton(self.meas_panel)
        self.start_meas_btn.setObjectName("start_meas_btn")
        self.gridLayout_8.addWidget(self.start_meas_btn, 1, 0, 1, 2)
        self.stop_meas_btn = QtWidgets.QPushButton(self.meas_panel)
        self.stop_meas_btn.setEnabled(False)
        self.stop_meas_btn.setObjectName("stop_meas_btn")
        self.gridLayout_8.addWidget(self.stop_meas_btn, 2, 0, 1, 2)
        self.gridLayout_8.setColumnStretch(0, 1)
        self.gridLayout_10.addWidget(self.meas_panel, 2, 1, 1, 1)
        self.heater_panel = QtWidgets.QFrame(self.centralwidget)
        self.heater_panel.setMaximumSize(QtCore.QSize(16777215, 175))
        self.heater_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.heater_panel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.heater_panel.setObjectName("heater_panel")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.heater_panel)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_8 = QtWidgets.QLabel(self.heater_panel)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 1, 0, 1, 1)
        self.heater_value = QtWidgets.QLineEdit(self.heater_panel)
        self.heater_value.setObjectName("heater_value")
        self.gridLayout_7.addWidget(self.heater_value, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.heater_panel)
        self.label_11.setText("°C")
        self.label_11.setObjectName("label_11")
        self.gridLayout_7.addWidget(self.label_11, 1, 2, 1, 1)
        self.heater_toggle = QtWidgets.QPushButton(self.heater_panel)
        self.heater_toggle.setObjectName("heater_toggle")
        self.gridLayout_7.addWidget(self.heater_toggle, 2, 0, 1, 3)
        self.label_7 = QtWidgets.QLabel(self.heater_panel)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 3)
        self.gridLayout_10.addWidget(self.heater_panel, 2, 0, 1, 1)
        self.status_panel = QtWidgets.QFrame(self.centralwidget)
        self.status_panel.setMaximumSize(QtCore.QSize(16777215, 175))
        self.status_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.status_panel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.status_panel.setObjectName("status_panel")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.status_panel)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_17 = QtWidgets.QLabel(self.status_panel)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_12.addWidget(self.label_17, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.status_panel)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.heat_status_icon = QtWidgets.QLabel(self.frame)
        self.heat_status_icon.setTextFormat(QtCore.Qt.PlainText)
        self.heat_status_icon.setPixmap(QtGui.QPixmap(":/status/cross.png"))
        self.heat_status_icon.setObjectName("heat_status_icon")
        self.horizontalLayout.addWidget(self.heat_status_icon)
        self.gridLayout_12.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.status_panel)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.meas_status_icon = QtWidgets.QLabel(self.frame_2)
        self.meas_status_icon.setText("")
        self.meas_status_icon.setPixmap(QtGui.QPixmap(":/status/cross.png"))
        self.meas_status_icon.setObjectName("meas_status_icon")
        self.horizontalLayout_2.addWidget(self.meas_status_icon)
        self.gridLayout_12.addWidget(self.frame_2, 2, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.status_panel)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.record_icon = QtWidgets.QLabel(self.frame_3)
        self.record_icon.setText("")
        self.record_icon.setPixmap(QtGui.QPixmap(":/status/cross.png"))
        self.record_icon.setObjectName("record_icon")
        self.horizontalLayout_3.addWidget(self.record_icon)
        self.gridLayout_12.addWidget(self.frame_3, 3, 0, 1, 1)
        self.gridLayout_10.addWidget(self.status_panel, 2, 3, 1, 1)
        self.live_data_frame = QtWidgets.QFrame(self.centralwidget)
        self.live_data_frame.setMaximumSize(QtCore.QSize(16777215, 175))
        self.live_data_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.live_data_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.live_data_frame.setObjectName("live_data_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.live_data_frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_6 = QtWidgets.QLabel(self.live_data_frame)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 5)
        self.temp_heater = QtWidgets.QFrame(self.live_data_frame)
        self.temp_heater.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.temp_heater.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.temp_heater.setObjectName("temp_heater")
        self.gridLayout = QtWidgets.QGridLayout(self.temp_heater)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.temp_heater)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.temp_heater_view = QtWidgets.QLineEdit(self.temp_heater)
        self.temp_heater_view.setObjectName("temp_heater_view")
        self.gridLayout.addWidget(self.temp_heater_view, 1, 0, 1, 1)
        self.temp_heater_unit = QtWidgets.QLabel(self.temp_heater)
        self.temp_heater_unit.setText("°C")
        self.temp_heater_unit.setObjectName("temp_heater_unit")
        self.gridLayout.addWidget(self.temp_heater_unit, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.temp_heater, 1, 0, 1, 1)
        self.temp_amb = QtWidgets.QFrame(self.live_data_frame)
        self.temp_amb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.temp_amb.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.temp_amb.setObjectName("temp_amb")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.temp_amb)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.temp_amb)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)
        self.temp_amb_view = QtWidgets.QLineEdit(self.temp_amb)
        self.temp_amb_view.setObjectName("temp_amb_view")
        self.gridLayout_2.addWidget(self.temp_amb_view, 1, 0, 1, 1)
        self.temp_amb_unit = QtWidgets.QLabel(self.temp_amb)
        self.temp_amb_unit.setText("°C")
        self.temp_amb_unit.setObjectName("temp_amb_unit")
        self.gridLayout_2.addWidget(self.temp_amb_unit, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.temp_amb, 1, 1, 1, 1)
        self.pressure = QtWidgets.QFrame(self.live_data_frame)
        self.pressure.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pressure.setObjectName("pressure")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.pressure)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pressure_unit = QtWidgets.QLabel(self.pressure)
        self.pressure_unit.setText("psi")
        self.pressure_unit.setObjectName("pressure_unit")
        self.gridLayout_3.addWidget(self.pressure_unit, 1, 1, 1, 1)
        self.pressure_view = QtWidgets.QLineEdit(self.pressure)
        self.pressure_view.setObjectName("pressure_view")
        self.gridLayout_3.addWidget(self.pressure_view, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.pressure)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 2)
        self.gridLayout_6.addWidget(self.pressure, 1, 2, 1, 1)
        self.humidity = QtWidgets.QFrame(self.live_data_frame)
        self.humidity.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.humidity.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.humidity.setObjectName("humidity")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.humidity)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.humidity_unit = QtWidgets.QLabel(self.humidity)
        self.humidity_unit.setText("%RH")
        self.humidity_unit.setObjectName("humidity_unit")
        self.gridLayout_4.addWidget(self.humidity_unit, 1, 1, 1, 1)
        self.humidity_view = QtWidgets.QLineEdit(self.humidity)
        self.humidity_view.setObjectName("humidity_view")
        self.gridLayout_4.addWidget(self.humidity_view, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.humidity)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 2)
        self.gridLayout_6.addWidget(self.humidity, 1, 3, 1, 1)
        self.resistance = QtWidgets.QFrame(self.live_data_frame)
        self.resistance.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resistance.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.resistance.setObjectName("resistance")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.resistance)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_5 = QtWidgets.QLabel(self.resistance)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 2)
        self.resistance_unit = QtWidgets.QLabel(self.resistance)
        self.resistance_unit.setText("kΩ")
        self.resistance_unit.setObjectName("resistance_unit")
        self.gridLayout_5.addWidget(self.resistance_unit, 1, 1, 1, 1)
        self.resistance_view = QtWidgets.QLineEdit(self.resistance)
        self.resistance_view.setObjectName("resistance_view")
        self.gridLayout_5.addWidget(self.resistance_view, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.resistance, 1, 4, 1, 1)
        self.gridLayout_10.addWidget(self.live_data_frame, 1, 0, 1, 4)
        self.graph_frame = QtWidgets.QFrame(self.centralwidget)
        self.graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graph_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.graph_frame.setObjectName("graph_frame")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.graph_frame)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.temp_plot = LivePlotWidget(self.graph_frame)
        self.temp_plot.setObjectName("temp_plot")
        self.gridLayout_11.addWidget(self.temp_plot, 0, 0, 1, 1)
        self.resistance_plot = LivePlotWidget(self.graph_frame)
        self.resistance_plot.setObjectName("resistance_plot")
        self.gridLayout_11.addWidget(self.resistance_plot, 0, 1, 1, 1)
        self.pressure_plot = LivePlotWidget(self.graph_frame)
        self.pressure_plot.setObjectName("pressure_plot")
        self.gridLayout_11.addWidget(self.pressure_plot, 1, 0, 1, 1)
        self.humidity_plot = LivePlotWidget(self.graph_frame)
        self.humidity_plot.setObjectName("humidity_plot")
        self.gridLayout_11.addWidget(self.humidity_plot, 1, 1, 1, 1)
        self.gridLayout_10.addWidget(self.graph_frame, 0, 0, 1, 4)
        self.gridLayout_10.setColumnStretch(0, 1)
        self.gridLayout_10.setColumnStretch(1, 1)
        self.gridLayout_10.setColumnStretch(2, 3)
        self.gridLayout_10.setColumnStretch(3, 1)
        self.gridLayout_10.setRowStretch(0, 3)
        self.gridLayout_10.setRowStretch(1, 1)
        self.gridLayout_10.setRowStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_References = QtWidgets.QMenu(self.menu_Edit)
        self.menu_References.setObjectName("menu_References")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Connect = QtWidgets.QAction(MainWindow)
        self.action_Connect.setObjectName("action_Connect")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Resistance = QtWidgets.QAction(MainWindow)
        self.action_Resistance.setObjectName("action_Resistance")
        self.menu_File.addAction(self.action_Connect)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_References.addAction(self.action_Resistance)
        self.menu_Edit.addAction(self.menu_References.menuAction())
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.label_13.setBuddy(self.freq_value)
        self.label_16.setBuddy(self.lineEdit)
        self.label_8.setBuddy(self.heater_value)
        self.label.setBuddy(self.temp_heater_view)
        self.label_2.setBuddy(self.temp_amb_view)
        self.label_3.setBuddy(self.pressure_view)
        self.label_4.setBuddy(self.humidity_view)
        self.label_5.setBuddy(self.resistance_view)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gas Chamber Controller"))
        self.label_14.setText(_translate("MainWindow", "Recording Controls"))
        self.label_13.setText(_translate("MainWindow", "Frequency:"))
        self.pushButton.setText(_translate("MainWindow", "Start Recording"))
        self.label_16.setText(_translate("MainWindow", "File Destination:"))
        self.label_9.setText(_translate("MainWindow", "Measurement Controls"))
        self.start_meas_btn.setText(_translate("MainWindow", "Start Measuring"))
        self.stop_meas_btn.setText(_translate("MainWindow", "Stop Measuring"))
        self.label_8.setText(_translate("MainWindow", "Target Temperature:"))
        self.heater_toggle.setText(_translate("MainWindow", "Toggle"))
        self.label_7.setText(_translate("MainWindow", "Heater Controls"))
        self.label_17.setText(_translate("MainWindow", "Status"))
        self.label_10.setText(_translate("MainWindow", "Heater Status: "))
        self.label_12.setText(_translate("MainWindow", "Measurement Status:"))
        self.label_15.setText(_translate("MainWindow", "Recording Status:"))
        self.label_6.setText(_translate("MainWindow", "Live Data"))
        self.label.setText(_translate("MainWindow", "Temperature (Heater)"))
        self.label_2.setText(_translate("MainWindow", "Temperature (Ambient)"))
        self.label_3.setText(_translate("MainWindow", "Pressure"))
        self.label_4.setText(_translate("MainWindow", "Humidity"))
        self.label_5.setText(_translate("MainWindow", "Resistance"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit"))
        self.menu_References.setTitle(_translate("MainWindow", "&References"))
        self.action_Connect.setText(_translate("MainWindow", "&Connection"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.action_Resistance.setText(_translate("MainWindow", "&Resistor"))
from pglive.sources.live_plot_widget import LivePlotWidget
import main_rc

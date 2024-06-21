import ctypes, sys

from multiprocessing import freeze_support 

from constants import APPID

from PyQt5.QtWidgets import QApplication

from main_wrapper import Window

# Main Function
if __name__ == "__main__":

    # Freeze Support
    freeze_support()
    
    # Update App ID if Windows
    if sys.platform.startswith("win"):
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APPID)

    # Prep App Launch
    app = QApplication(sys.argv)

    # Setup Window
    win = Window()

    # Show
    win.show()

    # End
    sys.exit(app.exec())

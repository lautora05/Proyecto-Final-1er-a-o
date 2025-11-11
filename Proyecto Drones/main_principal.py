import sys
from PyQt5.QtWidgets import (QApplication)
from pestaña_window import VentanaMonitoreoDrones

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaMonitoreoDrones()
    ventana.show()
    sys.exit(app.exec_())
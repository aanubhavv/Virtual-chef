import sys
import warnings
from functions.ui_func import *
from ui_main import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        flags = self.windowFlags()
        flags &= ~Qt.WindowMaximizeButtonHint   # Remove maximize button
        flags |= Qt.WindowCloseButtonHint   # Add close 
        self.setWindowFlags(flags)

        self.ui.button.clicked.connect(lambda: UIFunc.reply(self))
        self.ui.speak_button.clicked.connect(lambda: UIFunc.speak(self))
        self.ui.talk_button.clicked.connect(lambda: UIFunc.talk(self))
        self.show()

    def update_output_label(self, text):
        self.ui.output_label.setText(text)
        print("recipe generated")

    def update_input_label(self, stt):
        self.ui.inpt.setText(stt)
        print("Finished Speaking")
  
        
warnings.filterwarnings("ignore")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

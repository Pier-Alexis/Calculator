import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
from math import sqrt, log, pi, e, sin, cos, tan, pow

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Calculator")
        self.setGeometry(100, 100, 400, 600)
        self.initUI()

    def initUI(self):
        # Principal layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        main_layout = QVBoxLayout(self.central_widget)

      
        self.display = QLineEdit()
        self.display.setFont(QFont("Arial", 18))
        self.display.setPlaceholderText("Enter your expression...")
        self.display.setReadOnly(True)
        self.display.setAlignment(1)  # Align to the center
        main_layout.addWidget(self.display)

        # button grid
        grid_layout = QGridLayout()
        main_layout.addLayout(grid_layout)

        # number and calculator icons grid
        buttons = {
            "7": (0, 0), "8": (0, 1), "9": (0, 2), "/": (0, 3),
            "4": (1, 0), "5": (1, 1), "6": (1, 2), "*": (1, 3),
            "1": (2, 0), "2": (2, 1), "3": (2, 2), "-": (2, 3),
            "0": (3, 0), ".": (3, 1), "=": (3, 2), "+": (3, 3),
            "√": (4, 0), "x²": (4, 1), "log": (4, 2), "C": (4, 3),
            "sin": (5, 0), "cos": (5, 1), "tan": (5, 2), "π": (5, 3),
            "e": (6, 0), "^": (6, 1), "(": (6, 2), ")": (6, 3),
        }

        # Create button
        for text, position in buttons.items():
            button = QPushButton(text)
            button.setFont(QFont("Arial", 14))
            button.setFixedSize(80, 60)
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, *position)

    def on_button_click(self):
        sender = self.sender().text()

        if sender == "C":
            self.display.clear()  # Clear the display
        elif sender == "=":
            try:
                expression = self.display.text()
                # Calculate the expression with support for mathematical functions
                result = eval(
                    expression,
                    {"__builtins__": None},
                    {"sqrt": sqrt, "log": log, "pi": pi, "e": e, "sin": sin, "cos": cos, "tan": tan, "pow": pow}
                )
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error")
        elif sender == "√":
            self.display.setText(self.display.text() + "sqrt(")
        elif sender == "x²":
            self.display.setText(self.display.text() + "**2")
        elif sender == "π":
            self.display.setText(self.display.text() + "pi")
        elif sender == "^":
            self.display.setText(self.display.text() + "**")
        else:
            self.display.setText(self.display.text() + sender)

# Lancer l'application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())

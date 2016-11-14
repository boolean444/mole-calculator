import sys
from PyQt4.QtGui import *
from conversions import give_conversion
from molecule import *


class Frame(QWidget):
    def __init__(self):
        super(Frame, self).__init__()
        layout = QFormLayout()

        hbox_pic = QHBoxLayout()
        mole = QLabel()
        mole.setPixmap(QPixmap("monty_mole_nsmbu_solo--1-.png"))
        hbox_pic.addWidget(QLabel("     " * 20))
        hbox_pic.addWidget(mole)
        layout.addRow(hbox_pic)

        molarmass = QLineEdit()
        molarmass.textChanged.connect(self.get_molecule)
        layout.addRow(QLabel("Molecule to grams:"), molarmass)

        self.molar_mass = QLabel("")
        layout.addRow(self.molar_mass)

        hline = QFrame()
        hline.setFrameStyle(QFrame.HLine)
        layout.addRow(hline)

        label2 = QLabel("\nConversion:")
        layout.addRow(label2)
        self.list1 = QComboBox()
        self.list1.activated.connect(self.get_conversion)
        self.list1.addItem("moles")
        self.list1.addItem("atoms")
        self.list1.addItem("grams")
        self.list2 = QComboBox()
        self.list2.activated.connect(self.get_conversion)
        self.list2.addItem("moles")
        self.list2.addItem("atoms")
        self.list2.addItem("grams")
        hbox = QHBoxLayout()
        hbox.addWidget(self.list1)
        hbox.addWidget(self.list2)
        layout.addRow(hbox)

        hbox2 = QHBoxLayout()
        self.item1 = QLineEdit()
        self.item1.textChanged.connect(self.get_conversion)
        self.item2 = QLineEdit()
        hbox2.addWidget(self.item1)
        hbox2.addWidget(QLabel("→"))
        hbox2.addWidget(self.item2)
        layout.addRow(hbox2)

        hbox3 = QHBoxLayout()
        self.molecule = QLineEdit()
        self.molecule.textChanged.connect(self.get_conversion)
        self.molecule.setEnabled(False)
        label3 = QLabel("Molecule:")
        hbox3.addWidget(label3)
        hbox3.addWidget(self.molecule)
        hbox3.addWidget(QLabel("    "*18))
        layout.addRow(hbox3)

        self.setLayout(layout)

    def get_molecule(self, text):
        if text:
            try:
                new = get_molarmass(text)
                self.molar_mass.setText(str(new))
            except:
                return

    def get_conversion(self, othertext):
        state = self.update_molecule()
        text = self.item1.text()
        item1 = str(self.list1.currentText())
        if text.isdigit():
                conversion_method = give_conversion(item1, str(self.list2.currentText()))
                kwarg = {item1:int(text)}
                if state:
                    kwarg['molecule'] = self.molecule.text()
                new = conversion_method(**kwarg)
                self.item2.setText(str(new))

    def update_molecule(self):
        if str(self.list1.currentText()) == "grams" or str(self.list2.currentText()) == "grams":
            self.molecule.setEnabled(True)
            return 1
        else:
            self.molecule.setEnabled(False)
            return 0


if __name__ == "__main__":
    main = QApplication(sys.argv)
    piclabel = QLabel()
    piclabel.setPixmap(QPixmap("table.gif"))
    piclabel.show()
    window = Frame()
    window.setWindowTitle("Mole Converter")
    window.setGeometry(400, 100, 400, 200)
    window.show()
    main.exec_()
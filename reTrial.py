#! /usr/bin/env python3
import sys, re
from PyQt5.QtWidgets import ( QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy,
    QScrollArea,
    QMainWindow )

from PyQt5.QtCore import Qt, QRect

from PyQt5.QtGui import QFont


class ScrollableLabel (QScrollArea):
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, **kwargs)

        #make widget resizable
        self.setWidgetResizable(True)

        # create content object
        content = QWidget(self)
        self.setWidget(content)

        # vertical box addLayout
        lay = QVBoxLayout(content)

        # create the label
        self.label = QLabel(content)

        # set alignment
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # make the label multi-line
        self.label.setWordWrap(True)

        # add the label to the layout
        lay.addWidget(self.label)

    def setText(self, text):
        self.label.setText(text)


class reTrial (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("re Trial")
        layout = QVBoxLayout()
        label = QLabel("Enter Regular Expression")
        layout.addWidget(label)
        self.reBox = QTextEdit()
        layout.addWidget(self.reBox)
        label = QLabel("Enter trial data")
        layout.addWidget(label)
        self.textBox = QTextEdit()
        layout.addWidget(self.textBox)
        label = QLabel("Results")
        layout.addWidget(label)
        self.resultsBox = ScrollableLabel("")
        self.resultsBox.setFixedHeight(200)
        self.resultsBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.resultsBox)
        buttons = QHBoxLayout()
        self.reClear = QPushButton("Clear re")
        buttons.addWidget(self.reClear)
        self.textClear = QPushButton("Clear trial data")
        buttons.addWidget(self.textClear)
        self.reTrial = QPushButton("Run re")
        buttons.addWidget(self.reTrial)
        self.endRun = QPushButton("Exit")
        buttons.addWidget(self.endRun)
        layout.addLayout(buttons)

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

        self.setGeometry(QRect(576, 250, 700, 700))

        self.reClear.clicked.connect(self.clearre)
        self.textClear.clicked.connect(self.clearText)
        self.reTrial.clicked.connect(self.runRe)
        self.endRun.clicked.connect(self.exitProgram)

        self.show()

    def clearre(self):
        self.reBox.clear()
        self.resultsBox.setText("")

    def clearText(self):
        self.textBox.clear()
        self.resultsBox.setText("")

    def runRe(self):
        regexp = self.reBox.toPlainText()
        testData = self.textBox.toPlainText()

        tests = testData.split("\n")
        regcomp = re.compile(regexp)
        results = []
        for test in tests:
            result = regcomp.search(test)
            if result:
                results.append(f"({result.start()},{result.end()}) - {result[0]}")
                matches = result.groups()
            else:
                matches = None
            results.append(str(matches))

        self.resultsBox.setText("\n".join(results))

    def exitProgram(self):
        self.close()


if __name__ == "__main__":
    app = QApplication([])

    window = reTrial()

    exit(app.exec_())

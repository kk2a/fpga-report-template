import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QListWidget, QMessageBox
from PyQt5.QtCore import Qt
from PyPDF2 import PdfMerger

class PDFMergerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PDF Merger')
        self.setGeometry(100, 100, 400, 300)

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)

        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)

        self.list_widget = QListWidget(self)
        self.layout.addWidget(self.list_widget)

        self.add_button = QPushButton('Add PDF Files', self)
        self.add_button.clicked.connect(self.add_files)
        self.layout.addWidget(self.add_button)

        self.merge_button = QPushButton('Merge PDF Files', self)
        self.merge_button.clicked.connect(self.merge_files)
        self.layout.addWidget(self.merge_button)

    def add_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select PDF files", "", "PDF Files (*.pdf)")
        if files:
            for file in files:
                self.list_widget.addItem(file)

    def merge_files(self):
        if self.list_widget.count() == 0:
            QMessageBox.warning(self, "No files", "Please add PDF files to merge.")
            return

        save_path, _ = QFileDialog.getSaveFileName(self, "Save Merged PDF", "", "PDF Files (*.pdf)")
        if not save_path:
            return

        merger = PdfMerger()

        for index in range(self.list_widget.count()):
            merger.append(self.list_widget.item(index).text())

        try:
            with open(save_path, 'wb') as f:
                merger.write(f)
            QMessageBox.information(self, "Success", "PDF files have been merged successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while merging PDF files:\n{str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = PDFMergerApp()
    mainWin.show()
    sys.exit(app.exec_())

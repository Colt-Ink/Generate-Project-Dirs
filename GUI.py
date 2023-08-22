from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QComboBox, QLineEdit, QPushButton, QMessageBox

def window(callback, job_number_default, part_number_default, project_name_default, part_name_default):
    app = QApplication([])
    win = QMainWindow()
    win.setWindowTitle('New Project')
    
    layout = QGridLayout()

    folder_type_label = QLabel('Folder type:')
    layout.addWidget(folder_type_label, 0, 0)

    folder_type = QComboBox()
    layout.addWidget(folder_type, 0, 1)
    folder_type.addItem('New Job')
    folder_type.addItem('New Part')

    job_number_label = QLabel('Job Number:')
    job_number_entry = QLineEdit()
    layout.addWidget(job_number_label, 1, 0)
    layout.addWidget(job_number_entry, 1, 1)

    part_number_label = QLabel('Part Number:')
    part_number_entry = QLineEdit()
    layout.addWidget(part_number_label, 2, 0)
    layout.addWidget(part_number_entry, 2, 1)

    project_name_label = QLabel('Project Name:')
    project_name_entry = QLineEdit()
    layout.addWidget(project_name_label, 3, 0)
    layout.addWidget(project_name_entry, 3, 1)

    part_name_label = QLabel('Part Name:')
    part_name_entry = QLineEdit()
    layout.addWidget(part_name_label, 4, 0)
    layout.addWidget(part_name_entry, 4, 1)

    def on_submit():
        # First validate the input fields, then proceed.
        job_number_input = job_number_entry.text()
        part_number_input = part_number_entry.text()
        project_name_input = project_name_entry.text()
        part_name_input = part_name_entry.text()

        if not (job_number_input and part_number_input and project_name_input and part_name_input):
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Critical)
            message_box.setWindowTitle("Error")
            message_box.setText("All fields must be filled in.")
            message_box.exec_()
            return

        folder_type_input = folder_type.currentText()
        callback(job_number_input, part_number_input, project_name_input, part_name_input, folder_type_input)
        win.close()

    submit_button = QPushButton('Create Folder Structure')
    submit_button.clicked.connect(on_submit)
    layout.addWidget(submit_button, 5, 0, 1, 2)

    central_widget = QWidget()
    central_widget.setLayout(layout)
    win.setCentralWidget(central_widget)

    win.show()
    app.exec_()  # Block until the window is closed.
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QComboBox, QLineEdit, QPushButton, QMessageBox


def window(callback, get_next_number_fn, job_number_default, part_number_default, project_name_default, part_name_default):
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

    folder_type.setCurrentIndex(1)  # Set "New Part" as the default value

    job_number_label = QLabel('Job Number:')
    job_number_entry = QLineEdit()
    job_number_entry.setText(job_number_default)
    layout.addWidget(job_number_label, 1, 0)
    layout.addWidget(job_number_entry, 1, 1)

    part_number_label = QLabel('Part Number:')
    part_number_entry = QLineEdit()
    part_number_entry.setText(part_number_default)
    layout.addWidget(part_number_label, 2, 0)
    layout.addWidget(part_number_entry, 2, 1)

    project_name_label = QLabel('Project Name:')
    project_name_entry = QLineEdit()
    project_name_entry.setText(project_name_default)
    layout.addWidget(project_name_label, 3, 0)
    layout.addWidget(project_name_entry, 3, 1)

    part_name_label = QLabel('Part Name:')
    part_name_entry = QLineEdit()
    part_name_entry.setText(part_name_default)
    layout.addWidget(part_name_label, 4, 0)
    layout.addWidget(part_name_entry, 4, 1)

    def on_submit():
        # First validate the input fields, then proceed.
        job_number_input = int(job_number_entry.text())
        part_number_input = int(part_number_entry.text())
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

    def folder_type_change(state):
        # If it's a new job, set the next part number to 1
        if state == "New Job":
            job_number_default, _, _ = get_next_number_fn("New Job")
            job_number_entry.setText(job_number_default)
            part_number_entry.setText("01")
        else: # "New Part"
            job_number_default, part_number_default, job_name_parent = get_next_number_fn("New Part")
            job_number_entry.setText(job_number_default) # Update job number
            part_number_entry.setText(str(int(part_number_default)).zfill(2))
            # project_name_entry.setText(job_name_parent)


    folder_type.currentTextChanged.connect(folder_type_change)
    
    submit_button = QPushButton('Create Folder Structure')
    submit_button.clicked.connect(on_submit)
    layout.addWidget(submit_button, 5, 0, 1, 2)

    central_widget = QWidget()
    central_widget.setLayout(layout)
    win.setCentralWidget(central_widget)

    win.show()
    app.exec_()  # Block until the window is closed.
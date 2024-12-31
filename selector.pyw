import subprocess
from subprocess import run
import os
import sys
import json
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton,
    QLineEdit, QPushButton, QHBoxLayout, QMessageBox, QComboBox
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Deskime Settings")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the full path to the logo image
        logo_path = os.path.join(script_dir, "apps\logo.png")
        pixmap = QPixmap(logo_path)  # Load logo.png from the same directory
        self.setWindowIcon(pixmap)

        self.resize(300,400)

        # Set the stylesheet
        self.setStyleSheet("""
            QWidget {
                background-color: #fefefe;
            }
            QPushButton#closeButn {
                border: 1px solid transparent;
                border-radius: 3px;
            }
            QPushButton#closeButn:hover {
                background-color: #d1d1d1;
            }
            QLineEdit, QComboBox {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px 5px;
                height: 60px;
                font-size: 12px;
                background-color: #fff;
            }
            QLineEdit:focus {
                border-color: #2781F2;
            }
            QComboBox:on {
                border-color: #2781F2;
            }
            QPushButton#save_settings {
                font-size: 10pt;
                padding: 5px;
                border: 1px solid darkgray;
                border-radius: 7px;
                background-color: #2781F2;
                color: #ffffff;
            }
            QPushButton#discard_changes {
                font-size: 10pt;
                background: transparent;
                border: 1px solid #FF0000;
                border-radius: 7px;
                padding: 5px;
            }
            QPushButton#save_settings:hover {
                background-color: #3185eb;
            }
            QPushButton#save_settings:pressed {
                background-color: #387cd1;
            }
            QPushButton#discard_changes:hover {
                background-color: #E81123;
                color: #fff;
            }
            QPushButton#discard_changes:pressed {
                background-color: #9B0B17;
            }
            QLabel {
                color: #606770;
            }
        """)

        # Create layout
        layout = QVBoxLayout()

        # Search Settings
        search_label = QLabel("<b>Search Settings</b>")
        layout.addWidget(search_label)

        # Dropdown for selecting search engine
        self.search_engine_combo = QComboBox()
        self.search_engine_combo.addItems(["Google", "Bing", "DuckDuckGo", "Yandex"])
        layout.addWidget(self.search_engine_combo)

        # Web Background Settings
        web_label = QLabel("<b>Web Background Settings</b>")
        layout.addWidget(web_label)

        # Main options for radio buttons
        self.default_template_radio = QRadioButton("Use default template")
        layout.addWidget(self.default_template_radio)

        self.custom_link_radio = QRadioButton("Use custom link")
        layout.addWidget(self.custom_link_radio)

        # Textbox for custom link under the second radio button
        self.link_textbox = QLineEdit()
        self.link_textbox.setPlaceholderText("example.com")
        self.link_textbox.setDisabled(True)
        layout.addWidget(self.link_textbox)

        # Connect radio buttons
        self.default_template_radio.toggled.connect(self.toggle_custom_link)
        self.custom_link_radio.toggled.connect(self.toggle_custom_link)

        # Web Widget Settings
        widget_label = QLabel("<b>Web Widget Settings</b>")
        layout.addWidget(widget_label)

        self.web_widget_combo = QComboBox()
        self.web_widget_combo.addItems(["Enabled", "Disabled"])
        layout.addWidget(self.web_widget_combo)

        # Buttons
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save", self)
        self.save_button.setObjectName("save_settings")
        self.save_button.clicked.connect(self.save_settings)
        button_layout.addWidget(self.save_button)

        self.discard_button = QPushButton("Discard", self)
        self.discard_button.setObjectName("discard_changes")
        self.discard_button.clicked.connect(self.discard_settings)
        button_layout.addWidget(self.discard_button)

        layout.addLayout(button_layout)

        # Set the layout for the main window
        self.setLayout(layout)

    def toggle_custom_link(self):
        if self.custom_link_radio.isChecked():
            self.link_textbox.setEnabled(True)
        else:
            self.link_textbox.setDisabled(True)

    def save_settings(self):
        settings = {
            "search_engine": self.search_engine_combo.currentText(),
            "default_template": self.default_template_radio.isChecked(),
            "custom_link": self.link_textbox.text() if self.custom_link_radio.isChecked() else None,
            "web_widget": self.web_widget_combo.currentText()  # Save the web widget setting
        }

        # Save settings to settings.json
        with open("settings.json", "w") as f:
            json.dump(settings, f, indent=4)
        QMessageBox.information(self, "Settings Saved", "Your settings have been saved. Restart your PC to enable changes.")
        os.system("copy settings.json apps")
    def discard_settings(self):
        QMessageBox.information(self, "Settings Discarded", "Your settings have been discarded.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
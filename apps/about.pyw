import os
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialogButtonBox,
    QDialog,
    QVBoxLayout,
    QLabel,
    QApplication
)


class AboutDialog(QDialog):
    def __init__(self, parent=None, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.layout = QVBoxLayout()

        ok_btn = QDialogButtonBox.Ok
        self.button_box = QDialogButtonBox(ok_btn)

        self.init_ui()

    def init_ui(self):
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        # Set up the logo
        logo = QLabel()
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the full path to the logo image
        logo_path = os.path.join(script_dir, "logo.png")
        pixmap = QPixmap(logo_path)  # Load logo.png from the same directory
        pixmap = pixmap.scaled(80, 80)
        logo.setPixmap(pixmap)
        self.layout.addWidget(logo)

        # Set up the title with "MyFont Bold"
        title = QLabel("Deskime")
        title.setFont(QFont("MyFont Bold", 20))  # Use MyFont Bold for the title
        self.layout.addWidget(title)
        self.setWindowIcon(pixmap)

        # Set up version and copyright information with "JetBrains Mono"
        lbl1 = QLabel(
            '<center>Version 2.4<br>Your one-stop Desktop Customization App</center>'
        )
        lbl1.setFont(QFont("JetBrains Mono", 10))  # Use JetBrains Mono for the rest
        lbl1.setOpenExternalLinks(True)
        self.layout.addWidget(lbl1)

        # Set up the GitHub link
        github_pg = QLabel(
            '<a href="https://github.com/Deskime">Learn More </a>'
        )
        github_pg.setFont(QFont("JetBrains Mono", 10))  # Use JetBrains Mono for the link
        github_pg.setOpenExternalLinks(True)
        self.layout.addWidget(github_pg)

        # Center align all items
        for i in range(0, self.layout.count()):
            self.layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        self.layout.addWidget(self.button_box)

        self.setLayout(self.layout)

        # Apply the button stylesheet directly
        self.set_button_stylesheet()

        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)
        self.resize(400, 250)
        self.setMaximumHeight(300)
        self.setMaximumWidth(500)
        self.setWindowTitle("About")

    def set_button_stylesheet(self):
        stylesheet = """
        QPushButton {
            background-color: #2B5DD1;
            color: #FFFFFF;
            padding: 10px 30px;
            font: bold 14px;
            border-radius: 3px;
        }
        QPushButton:hover {
            background-color: #3769df;
        }
        """
        self.button_box.button(QDialogButtonBox.Ok).setStyleSheet(stylesheet)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    dialog = AboutDialog()
    dialog.exec()
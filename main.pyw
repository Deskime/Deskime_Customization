import os
import sys
import webbrowser
from logging import disable

import pystray
from pystray import Icon, MenuItem, Menu
from PIL import Image
import subprocess
import json

# Function to open the website
def open_website(icon, item):
    webbrowser.open("https://www.google.com")

# Function to open the settings
def open_settings(icon, item):
    # Assuming you want to open selector.pyw in the apps directory
    script_path = os.path.join(os.getcwd(),"selector.pyw")
    subprocess.Popen([sys.executable, script_path])

def open_about(icon, item):
    # Assuming you want to open selector.pyw in the apps directory
    script_path = os.path.join(os.getcwd(), "apps", "about.pyw")
    subprocess.Popen([sys.executable, script_path])

# Function to create the system tray icon
def create_icon():
    # Load the icon image
    image = Image.open("core/icons/logo.png")  # Adjusted path to the icon
    # Create the menu with the new "Open Settings" and "Check for Updates" items
    menu = Menu(
        MenuItem("Open Website", open_website),
        MenuItem("Open Settings", open_settings),
        MenuItem("About", open_about),
        MenuItem("Check for Updates", open_website)  # Reusing open_website for updates
    )
    # Create the icon
    icon = Icon("test_icon", image, "Deskime", menu)
    icon.run()

# Function to start other scripts
def start_scripts():
    scripts = ["apps/search.pyw", "apps/timewidget.pyw", "apps/web-bk.pyw"]
    for script in scripts:
        subprocess.Popen([sys.executable, script])

# Function to check settings and open web widget if enabled
def check_web_widget():
    if os.path.exists("settings.json"):
        with open("settings.json", "r") as f:
            settings = json.load(f)
            if settings.get("web_widget") == "Enabled":
                subprocess.Popen([sys.executable, "apps/webwidget.pyw"])  # Adjust the script name as needed

if __name__ == "__main__":
    # Start the other scripts
    start_scripts()
    # Check if the web widget should be opened
    check_web_widget()
    # Create the system tray icon
    create_icon()
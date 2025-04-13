import subprocess

installed = subprocess.check_output(['pip', 'list']).decode()
print(installed)

from app import app as application  # Ensure 'app' is your Flask object
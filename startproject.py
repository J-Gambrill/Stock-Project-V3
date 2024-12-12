#This project was created by chat gpt to run commands to start the online server so that i do not have to write them every time

import subprocess
import os

# Path to your Git Bash executable
git_bash_path = r"C:\Program Files\Git\bin\bash.exe"

# Commands to run in Git Bash
commands = """
source .venv/Scripts/activate
cd mystockproject
py manage.py runserver
"""

# Execute the commands in Git Bash
process = subprocess.Popen(
    [git_bash_path, "-c", commands],
    cwd=os.getcwd(),  # Set the working directory to the current script's directory
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Capture and print the output
stdout, stderr = process.communicate()
print(stdout)
if stderr:
    print(f"Error:\n{stderr}")

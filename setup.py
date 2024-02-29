import sys
import subprocess
import os
import urllib.request

def connect(host="https://google.com/"):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

package_q = ["pycryptodomex"]

def setup_a(module_name):
    subprocess.run("python -m pip install --upgrade pip")
    p = subprocess.run(f"python -m pip install {module_name}", shell=True)
    if p.returncode == 0:
        print(f"{module_name} is installed successfully.")
    elif p.returncode == 1 and connect():
        print("Error occurred. Check module name.")
    elif not connect():
        print("Error occurred. Check internet connection.")

print("Installing")
print("Please wait....")
print("Do not close this program")
for package in package_q:
    setup_a(package)
print("Installation finished")
subprocess.run("python EncrypC.py", shell=True)

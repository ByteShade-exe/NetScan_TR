import subprocess

def nikto_tarama():
    hedef = input("Hedef URL/IP: ")
    subprocess.run(["nikto", "-h", hedef])
import subprocess

def waf_tespiti():
    hedef = input("Hedef URL: ")
    subprocess.run(["wafw00f", hedef])
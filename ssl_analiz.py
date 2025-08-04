import subprocess

def ssl_analiz():
    hedef = input("Hedef domain (örnek: site.com): ")
    subprocess.run(["sslscan", hedef])
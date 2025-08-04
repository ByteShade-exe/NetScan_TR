import os
import socket
import threading
import ipaddress
from datetime import datetime

# Banner
def banner():
    print("\033[95m" + """
███╗   ██╗███████╗████████╗ ██████╗ █████╗ ███╗   ██╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗  ██║
██╔██╗ ██║█████╗     ██║   ██║     ███████║██╔██╗ ██║
██║╚██╗██║██╔══╝     ██║   ██║     ██╔══██║██║╚██╗██║
██║ ╚████║███████╗   ██║   ╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
""" + "\033[0m")
    print("Created by ByteShade | Discord: byteshade.py")
    print("Versiyon: NetScan_TR v2.1\n")

# IP port tarama
def scan_ip(ip):
    print(f"[+] IP taranıyor: {ip}")
    common_ports = [80, 443, 8080, 8443]
    for port in common_ports:
        sock = socket.socket()
        sock.settimeout(0.5)
        try:
            sock.connect((ip, port))
            print(f"    [✓] Port {port} açık")
        except:
            pass
        finally:
            sock.close()

# CIDR tarama
def scan_range(cidr):
    try:
        net = ipaddress.ip_network(cidr, strict=False)
        for ip in net.hosts():
            threading.Thread(target=scan_ip, args=(str(ip),)).start()
    except:
        print("[-] Geçersiz CIDR formatı!")

# HTML rapor oluştur
def generate_html_report():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("scan_report.html", "w") as file:
        file.write(f"<html><body><h2>Tarama Raporu - {now}</h2></body></html>")
    print("[✓] Rapor oluşturuldu: scan_report.html")

# Hakkında
def about():
    print("NetScan_TR, basit IP ve port tarayıcıdır.")
    print("Geliştirici: ByteShade | Discord: byteshade.py")

# Ana Menü
def menu():
    banner()
    while True:
        print("\n--- NetScan_TR Ana Menü ---")
        print("[1] Tek IP Taraması Başlat")
        print("[2] IP Aralığı Tara (CIDR)")
        print("[3] HTML Raporu Oluştur")
        print("[4] Hakkında")
        print("[5] Çıkış")

        choice = input("Seçiminizi girin: ")
        if choice == "1":
            ip = input("Taranacak IP: ")
            scan_ip(ip)
        elif choice == "2":
            cidr = input("CIDR formatı (örn: 192.168.1.0/24): ")
            scan_range(cidr)
        elif choice == "3":
            generate_html_report()
        elif choice == "4":
            about()
        elif choice == "5":
            print("Çıkılıyor...")
            break
        else:
            print("[-] Geçersiz seçim!")

if __name__ == "__main__":
    menu()
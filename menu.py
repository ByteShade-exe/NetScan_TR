import os
import time
import socket
import subprocess
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.MAGENTA + """
███╗   ██╗███████╗████████╗ ██████╗ █████╗ ███╗   ██╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗  ██║
██╔██╗ ██║█████╗     ██║   ██║     ███████║██╔██╗ ██║
██║╚██╗██║██╔══╝     ██║   ██║     ██╔══██║██║╚██╗██║
██║ ╚████║███████╗   ██║   ╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
""" + Fore.CYAN + "Created by ByteShade | Discord: byteshade.py")
    print(Fore.YELLOW + "Versiyon: NetScan_TR v2.1\n")
    time.sleep(0.5)

def show_menu():
    print(Fore.GREEN + "====== NETSCAN_TR ANA MENÜ ======")
    print(Fore.CYAN + "[1] Port Tarama")
    print("[2] IP Bilgisi (Whois)")
    print("[3] MAC Adresi Değiştir")
    print("[4] DNS Sorgulama")
    print("[5] Ağ Cihazlarını Listele")
    print("[6] Exploit Tarama (Searchsploit)")
    print("[7] WAF Tespiti (wafw00f)")
    print("[8] Zaafiyet Analizi (Nikto)")
    print("[9] SSL Analizi (sslscan)")
    print("[10] Hakkında")
    print(Fore.RED + "[0] Çıkış\n")

def port_taramasi():
    hedef = input(Fore.CYAN + "📍 Hedef IP: ")
    ports = [21,22,23,25,53,80,110,143,443,445,993,995,3306,8080]
    print(Fore.BLUE + f"[+] {hedef} IP üzerinde portlar taranıyor...")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((hedef, port))
            print(Fore.GREEN + f"    [✓] Port {port} açık")
            sock.close()
        except:
            print(Fore.LIGHTBLACK_EX + f"    [-] Port {port} kapalı")

def whois_bilgisi():
    hedef = input(Fore.CYAN + "🌍 IP adresi girin: ")
    try:
        r = requests.get(f"https://ipwhois.app/json/{hedef}").json()
        print(Fore.BLUE + f"{r['ip']} → {r['country']} | {r['org']} | {r['region']}")
    except:
        print(Fore.RED + "[!] Whois bilgisi alınamadı.")

def mac_degistir():
    iface = input(Fore.CYAN + "📶 Arayüz adı (örnek: eth0): ")
    yeni_mac = input("🆕 Yeni MAC adresi: ")
    try:
        subprocess.call(["ifconfig", iface, "down"])
        subprocess.call(["ifconfig", iface, "hw", "ether", yeni_mac])
        subprocess.call(["ifconfig", iface, "up"])
        print(Fore.GREEN + f"[✓] MAC adresi değiştirildi → {yeni_mac}")
    except:
        print(Fore.RED + "[!] MAC değişimi başarısız!")

def dns_sorgula():
    alan = input(Fore.CYAN + "🔎 Alan adı (örnek: google.com): ")
    try:
        ip = socket.gethostbyname(alan)
        print(Fore.GREEN + f"{alan} → IP: {ip}")
    except:
        print(Fore.RED + "[!] DNS çözümlemesi başarısız.")

def ag_cihazlarini_listele():
    print(Fore.BLUE + "[*] Ağ cihazları taranıyor...")
    os.system("arp -a")

def exploit_tarama():
    query = input(Fore.CYAN + "💥 Exploit araması için anahtar kelime: ")
    os.system(f"searchsploit {query}")

def waf_tespiti():
    hedef = input(Fore.CYAN + "🛡 URL girin (örn: https://site.com): ")
    os.system(f"wafw00f {hedef}")

def nikto_tarama():
    hedef = input(Fore.CYAN + "🔬 Hedef host: ")
    os.system(f"nikto -h {hedef}")

def ssl_analiz():
    host = input(Fore.CYAN + "🔐 Site (örn: google.com): ")
    os.system(f"sslscan {host}")

def hakkinda():
    print(Fore.YELLOW + "\n🛠 NetScan_TR - Terminal Güvenlik Aracı")
    print("👨‍💻 Geliştirici: ByteShade")
    print("📌 Discord: byteshade.py")
    print("📦 Sürüm: v2.1\n")

def run_menu():
    banner()
    while True:
        show_menu()
        secim = input(Fore.WHITE + "Seçiminizi yapın: ").strip()
        if secim == "1": port_taramasi()
        elif secim == "2": whois_bilgisi()
        elif secim == "3": mac_degistir()
        elif secim == "4": dns_sorgula()
        elif secim == "5": ag_cihazlarini_listele()
        elif secim == "6": exploit_tarama()
        elif secim == "7": waf_tespiti()
        elif secim == "8": nikto_tarama()
        elif secim == "9": ssl_analiz()
        elif secim == "10": hakkinda()
        elif secim == "0":
            print(Fore.LIGHTBLACK_EX + "👋 Çıkış yapılıyor... Görüşürüz Kerem!")
            break
        else:
            print(Fore.RED + "⚠ Geçersiz seçim, tekrar dene.")
        time.sleep(1)

if __name__ == "__main__":
    run_menu()
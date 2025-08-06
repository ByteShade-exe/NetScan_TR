import os
import time
import socket
import subprocess
import requests
from colorama import Fore, Style, init

init(autoreset=True)

# 🌐 Dil seçimi
def select_language():
    print("🌐 Dil seçin / Select language:")
    print("[1] Türkçe")
    print("[2] English")
    choice = input("Seçim / Choice: ").strip()
    return "TR" if choice == "1" else "EN"

# 🌐 Dil paketleri
def get_language_pack(lang):
    return {
        "banner": {
            "TR": "Versiyon: NetScan_TR v2.1",
            "EN": "Version: NetScan_TR v2.1"
        },
        "menu": {
            "TR": [
                "====== NETSCAN_TR ANA MENÜ ======",
                "[1] Port Tarama",
                "[2] IP Bilgisi (Whois)",
                "[3] MAC Adresi Değiştir",
                "[4] DNS Sorgulama",
                "[5] Ağ Cihazlarını Listele",
                "[6] Exploit Tarama (Searchsploit)",
                "[7] WAF Tespiti (wafw00f)",
                "[8] Zaafiyet Analizi (Nikto)",
                "[9] SSL Analizi (sslscan)",
                "[10] Hakkında",
                "[0] Çıkış"
            ],
            "EN": [
                "====== NETSCAN_TR MAIN MENU ======",
                "[1] Port Scan",
                "[2] IP Info (Whois)",
                "[3] Change MAC Address",
                "[4] DNS Lookup",
                "[5] List Network Devices",
                "[6] Exploit Search (Searchsploit)",
                "[7] WAF Detection (wafw00f)",
                "[8] Vulnerability Scan (Nikto)",
                "[9] SSL Analysis (sslscan)",
                "[10] About",
                "[0] Exit"
            ]
        },
        "exit": {
            "TR": "👋 Çıkış yapılıyor... Görüşürüz Kerem!",
            "EN": "👋 Exiting... See you Kerem!"
        },
        "invalid": {
            "TR": "⚠ Geçersiz seçim, tekrar dene.",
            "EN": "⚠ Invalid choice, try again."
        },
        "prompt": {
            "TR": "Seçiminizi yapın: ",
            "EN": "Make your choice: "
        }
    }

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

def show_menu(lang_pack, lang):
    print(Fore.GREEN + lang_pack["menu"][lang][0])
    for line in lang_pack["menu"][lang][1:]:
        print(Fore.CYAN + line)

def port_taramasi():
    hedef = input(Fore.CYAN + "📍 Target IP: ")
    ports = [21,22,23,25,53,80,110,143,443,445,993,995,3306,8080]
    print(Fore.BLUE + f"[+] Scanning ports on {hedef}...")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((hedef, port))
            print(Fore.GREEN + f"    [✓] Port {port} is open")
            sock.close()
        except:
            print(Fore.LIGHTBLACK_EX + f"    [-] Port {port} is closed")

def whois_bilgisi():
    hedef = input(Fore.CYAN + "🌍 Enter IP address: ")
    try:
        r = requests.get(f"https://ipwhois.app/json/{hedef}").json()
        print(Fore.BLUE + f"{r['ip']} → {r['country']} | {r['org']} | {r['region']}")
    except:
        print(Fore.RED + "[!] Failed to retrieve Whois info.")

def mac_degistir():
    iface = input(Fore.CYAN + "📶 Interface name (e.g., eth0): ")
    yeni_mac = input("🆕 New MAC address: ")
    try:
        subprocess.call(["ifconfig", iface, "down"])
        subprocess.call(["ifconfig", iface, "hw", "ether", yeni_mac])
        subprocess.call(["ifconfig", iface, "up"])
        print(Fore.GREEN + f"[✓] MAC address changed → {yeni_mac}")
    except:
        print(Fore.RED + "[!] MAC change failed!")

def dns_sorgula():
    alan = input(Fore.CYAN + "🔎 Domain name (e.g., google.com): ")
    try:
        ip = socket.gethostbyname(alan)
        print(Fore.GREEN + f"{alan} → IP: {ip}")
    except:
        print(Fore.RED + "[!] DNS resolution failed.")

def ag_cihazlarini_listele():
    print(Fore.BLUE + "[*] Scanning network devices...")
    os.system("arp -a")

def exploit_tarama():
    query = input(Fore.CYAN + "💥 Keyword for exploit search: ")
    os.system(f"searchsploit {query}")

def waf_tespiti():
    hedef = input(Fore.CYAN + "🛡 Enter URL (e.g., https://site.com): ")
    os.system(f"wafw00f {hedef}")

def nikto_tarama():
    hedef = input(Fore.CYAN + "🔬 Target host: ")
    os.system(f"nikto -h {hedef}")

def ssl_analiz():
    host = input(Fore.CYAN + "🔐 Site (e.g., google.com): ")
    os.system(f"sslscan {host}")

def hakkinda():
    print(Fore.YELLOW + "\n🛠 NetScan_TR - Terminal Security Tool")
    print("👨‍💻 Developer: ByteShade")
    print("📌 Discord: byteshade.py")
    print("📦 Version: v2.1\n")

def run_menu():
    banner()
    lang = select_language()
    lang_pack = get_language_pack(lang)

    print(Fore.YELLOW + lang_pack["banner"][lang] + "\n")
    time.sleep(0.5)

    while True:
        show_menu(lang_pack, lang)
        secim = input(Fore.WHITE + lang_pack["prompt"][lang]).strip()
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
            print(Fore.LIGHTBLACK_EX + lang_pack["exit"][lang])
            break
        else:
            print(Fore.RED + lang_pack["invalid"][lang])
        time.sleep(1)

if __name__ == "__main__":
    run_menu()

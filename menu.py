import os
import time
import socket
import subprocess
import requests
from colorama import Fore, Style, init

init(autoreset=True)

lang = "tr"  # Varsayılan dil Türkçe

def select_language():
    global lang
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.YELLOW + "🗣 Select language / Dili seçin:")
    print("[1] Türkçe")
    print("[2] English")
    choice = input("👉 Seçiminiz / Your choice: ").strip()
    if choice == "2":
        lang = "en"
    else:
        lang = "tr"

def banner():
    print(Fore.MAGENTA + """
███╗   ██╗███████╗████████╗ ██████╗ █████╗ ███╗   ██╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗  ██║
██╔██╗ ██║█████╗     ██║   ██║     ███████║██╔██╗ ██║
██║╚██╗██║██╔══╝     ██║   ██║     ██╔══██║██║╚██╗██║
██║ ╚████║███████╗   ██║   ╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
""" + Fore.CYAN + "Created by ByteShade | Discord: byteshade.py")
    print(Fore.YELLOW + "Versiyon: NetScan_TR v2.1\n")

def show_menu():
    if lang == "tr":
        print(Fore.GREEN + "📋 Ana Menü:")
        print("[1] Port Taraması")
        print("[2] IP Bilgisi (Whois)")
        print("[3] MAC Adresi Değiştir")
        print("[4] DNS Sorgulama")
        print("[5] Ağ Cihazlarını Listele")
        print("[6] Exploit Arama (Searchsploit)")
        print("[7] WAF Tespiti (wafw00f)")
        print("[8] Zaafiyet Analizi (Nikto)")
        print("[9] SSL Analizi (sslscan)")
        print("[10] Hakkında")
        print("[0] Çıkış\n")
    else:
        print(Fore.GREEN + "📋 Main Menu:")
        print("[1] Port Scan")
        print("[2] IP Info (Whois)")
        print("[3] Change MAC Address")
        print("[4] DNS Lookup")
        print("[5] List Network Devices")
        print("[6] Exploit Search (Searchsploit)")
        print("[7] WAF Detection (wafw00f)")
        print("[8] Vulnerability Scan (Nikto)")
        print("[9] SSL Analysis (sslscan)")
        print("[10] About")
        print("[0] Exit\n")

def run_menu():
    select_language()
    banner()
    while True:
        show_menu()
        choice = input(Fore.WHITE + "👉 Seçiminiz / Your choice: ").strip()
        if choice == "1":
            print(Fore.CYAN + ("Port taraması başlatılıyor..." if lang == "tr" else "Starting port scan..."))
        elif choice == "10":
            print(Fore.YELLOW + ("NetScan_TR, ByteShade tarafından geliştirildi. Sürüm: v2.1" if lang == "tr" else
                                 "NetScan_TR, developed by ByteShade. Version: v2.1"))
        elif choice == "0":
            print(Fore.LIGHTBLACK_EX + ("Çıkış yapılıyor... 👋" if lang == "tr" else "Exiting... 👋"))
            break
        else:
            print(Fore.RED + ("Geçersiz seçim!" if lang == "tr" else "Invalid selection!"))
        time.sleep(1)

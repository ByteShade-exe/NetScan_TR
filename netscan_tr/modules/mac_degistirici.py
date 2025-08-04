import subprocess

def mac_degistirici():
    arayuz = input("Ağ arayüzü (örnek: eth0): ")
    subprocess.run(["ifconfig", arayuz, "down"])
    subprocess.run(["macchanger", "-r", arayuz])
    subprocess.run(["ifconfig", arayuz, "up"])
    print(f"{arayuz} için rastgele MAC adresi atandı.")
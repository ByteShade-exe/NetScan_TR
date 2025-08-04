# scanner.py – Port ve Subnet Tarayıcı

import nmap
import ipaddress

# 🌐 Tekil IP adresi için port taraması
def scan_ports(ip):
    scanner = nmap.PortScanner()
    try:
        scanner.scan(ip, '22,80,443', arguments='-T4')
        open_ports = []
        for proto in scanner[ip].all_protocols():
            for port in scanner[ip][proto]:
                state = scanner[ip][proto][port]['state']
                if state == 'open':
                    open_ports.append(port)
        return {
            'ip': ip,
            'status': scanner[ip].state(),
            'open_ports': open_ports
        }
    except Exception as e:
        return {'error': str(e)}

# 🧱 IP aralığı (subnet) taraması
def scan_subnet(cidr):
    scanner = nmap.PortScanner()
    active_hosts = []

    try:
        ip_net = ipaddress.ip_network(cidr, strict=False)
        for ip in ip_net.hosts():
            ip_str = str(ip)
            scanner.scan(ip_str, '22,80,443', arguments='-T4')
            if scanner[ip_str].state() == 'up':
                host_result = {
                    'ip': ip_str,
                    'status': scanner[ip_str].state(),
                    'open_ports': []
                }
                for proto in scanner[ip_str].all_protocols():
                    for port in scanner[ip_str][proto]:
                        state = scanner[ip_str][proto][port]['state']
                        if state == 'open':
                            host_result['open_ports'].append(port)
                active_hosts.append(host_result)
    except Exception as e:
        return {'error': str(e)}

    return active_hosts
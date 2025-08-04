# reporter.py – HTML Tarama Raporu Üretimi

import os
from datetime import datetime

def save_html_report(data, filename="scan_report.html"):
    os.makedirs("reports", exist_ok=True)
    full_path = os.path.join("reports", filename)

    html = "<html><head><title>NetScan_TR Report</title></head><body>"
    html += f"<h2>Tarama Raporu – {datetime.now().strftime('%Y-%m-%d %H:%M')}</h2><hr>"
    html += "<ul>"

    for host in data:
        html += f"<li><b>IP:</b> {host['ip']} – <b>Status:</b> {host['status']}"
        if host["open_ports"]:
            html += "<br><b>Açık Portlar:</b> " + ", ".join(map(str, host["open_ports"]))
        else:
            html += "<br><i>Açık port bulunamadı.</i>"
        html += "</li><br>"
    html += "</ul></body></html>"

    with open(full_path, "w") as f:
        f.write(html)

    print(f"📁 Rapor kaydedildi: {full_path}")
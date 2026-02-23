# Hostname; IP; Latency(ms); Status
nodes = [
    "Srv-Web-01;192.168.1.10;15;UP",
    "Srv-DB-01;192.168.1.20;450;UP",
    "Srv-Backup;10.0.0.5;0;DOWN",
    "Workstation-A;192.168.1.105;5;UP",
    "Srv-Proxy-01;172.16.0.1;10;up",
    "Srv-Mail;10.0.0.10;120;UP",
    "Router-Core;192.168.1.1;2;UP",
    "Srv-Dev-01;192.168.2.50;500;UP",
    "Printer-Main;192.168.1.200;0;down",
    "Srv-Log;10.0.0.15;105;UP" 
    
]

up_serveri = []
for node in nodes:
    dati = node.split(';')
    statuss = dati[3].strip().upper()
    if statuss == "UP":
        up_serveri.append(dati[0])
        print(dati[0])

print(f"Kopa atrasti: {len(up_serveri)}")
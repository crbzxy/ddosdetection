from scapy.all import *

# Direcciones IP y puertos para monitorear
target_ip = "0.0.0.0"
target_port = 80

# Lista de últimos X paquetes
packet_history = []

# Umbral para detección de anomalías
anomaly_threshold = 2

def packet_callback(packet):
    global packet_history
    if IP in packet and packet[IP].src == target_ip and packet[TCP].dport == target_port:
        packet_history.append(packet)
        if len(packet_history) > 10:
            packet_history.pop(0)  # Mantener un historial limitado de paquetes
        if len(packet_history) > anomaly_threshold:
            # Calcula la desviación estándar del intervalo entre paquetes
            intervals = [packet_history[i + 1].time - packet_history[i].time for i in 
range(len(packet_history) - 1)]
            std_dev = statistics.stdev(intervals)
            
            if std_dev < 0.001:  # Establece un umbral para detectar anomalías
                print(f"¡Posible ataque DDoS detectado desde {target_ip}!")
                packet_history = []

# Captura de paquetes
sniff(filter=f"src host {target_ip} and dst port {target_port}", prn=packet_callback)

from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    """Callback function to process captured packets."""
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "OTHER"
        
        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        else:
            src_port = dst_port = "N/A"

        print(f"[*] {protocol} Packet: {src_ip}:{src_port} --> {dst_ip}:{dst_port}")

def track_local_traffic(interface="eth0", packet_count=0):
    """
    Monitors local network traffic and displays packet information.

    :param interface: The network interface to sniff packets on (e.g., "eth0" or "wlan0").
    :param packet_count: Number of packets to capture (0 for unlimited).
    """
    print(f"[*] Starting packet sniffing on {interface}...")
    sniff(iface=interface, prn=packet_callback, store=False, count=packet_count)

# Example call for a specific interface (change according to your system)
if __name__ == "__main__":
    track_local_traffic(interface="wlan0")  # Use "wlan0" for Wi-Fi, "eth0" for Ethernet
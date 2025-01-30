import socket

def scan_ports(ip_address):
    """Scans all ports (0-65535) on the given IP address and prints open ports."""
    open_ports = []
    print(f"Scanning ports on {ip_address}...")

    for port in range(0, 65536):  # Scanning all 65536 ports
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Timeout to avoid long waits
        result = sock.connect_ex((ip_address, port))  # Returns 0 if port is open
        
        if result == 0:
            print(f"Port {port} is open.")
            open_ports.append(port)

        sock.close()
    
    print("\nScan complete.")
    return open_ports

# Example usage:
# scan_ports("192.168.1.1")  # Replace with the target IP
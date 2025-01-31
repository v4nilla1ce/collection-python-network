import subprocess
import platform
import re

def ping_ip(ip_address: str):
    """Pings an IP address and returns detailed information along with response time in milliseconds."""
    system = platform.system().lower()
    
    if system == "windows":
        command = ["ping", "-n", "1", ip_address]
    else:
        command = ["ping", "-c", "1", ip_address]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=5)
        output = result.stdout
        
        # Extract response time
        if system == "windows":
            match = re.search(r"Zeit[=<]([0-9]+)ms", output)
        else:
            match = re.search(r"time=([0-9\.]+) ms", output)
        
        rtt = float(match.group(1)) if match else None
        
        return {
            "ip": ip_address,
            "reachable": result.returncode == 0,
            "output": output,
            "rtt_ms": rtt
        }
    
    except subprocess.TimeoutExpired:
        return {"ip": ip_address, "reachable": False, "error": "Ping request timed out."}
    except Exception as e:
        return {"ip": ip_address, "reachable": False, "error": str(e)}

# Example usage:
if __name__ == "__main__":
    ip = "8.8.8.8"  # Google's public DNS server
    result = ping_ip(ip)
    print(result)

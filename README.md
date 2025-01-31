# collection-python-network

This repository is a collection of useful python functions for networking.

![Logo](resources/logo.png)

# Network Tools

This repository contains three Python scripts designed for network reconnaissance and diagnostics:

1. `find_subdomains.py` - Finds subdomains for a given domain.
2. `ping.py` - Pings an IP address and provides response details.
3. `scan_ports.py` - Scans for open ports on a specified IP address.

## Installation

Ensure you have Python installed on your system. You may need to install dependencies using:

```sh
pip install requests
```

## Usage

### 1. Find Subdomains

This script queries an online certificate transparency log API to find subdomains of a given domain.

#### Usage:

```sh
python find_subdomains.py example.com
```

#### Output:
A list of subdomains and their resolved IP addresses.

### 2. Ping an IP Address

This script sends a ping request to an IP and returns the response time.

#### Usage:

```sh
python ping.py 8.8.8.8
```

#### Output:
Ping results, including latency and status.

### 3. Scan Open Ports

This script scans all ports (0-65535) of a given IP and lists open ports.

#### Usage:

```sh
python scan_ports.py 192.168.1.1
```

#### Output:
A list of open ports on the target machine.

## Disclaimer

These scripts are intended for educational and ethical use only. Ensure you have permission before scanning any networks.

## License

MIT License


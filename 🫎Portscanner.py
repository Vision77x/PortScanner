import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print('\n[+] Scanning Target: ' + str(target))
    for port in range(1, 100):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    try:
        return s.recv(1024).decode().strip()
    except:
        return ''

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            if banner:
                print(f'[+] Open Port {port} : {banner}')
            else:
                print(f'[+] Open Port {port}')
        except:
            print(f'[+] Open Port {port}')
        sock.close()
    except:
        pass

# Get user input
targets = input('[+] Enter target(s) to scan (separate multiple with commas, e.g. google.com, facebook.com): ')
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip())
else:
    scan(targets)

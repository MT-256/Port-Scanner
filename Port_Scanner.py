# Credits for s4vitar in https://hack4u.io
#!/usr/bin/env python3

import socket
from termcolor import colored
import argparse
from concurrent.futures import ThreadPoolExecutor
import signal
import sys

open_sockets = []

def def_handler(sig, frame): # Function to exit Ctrl + C
    print(colored(f"\n[!] Exit...", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments(): # Help Panel
    
    parser = argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t", "--target", dest="target", required=True, help="Target (Example: -t 172.16.0.111)")
    parser.add_argument("-p", "--port", dest="port", required=True, help="Port Range (Example: -p 100-10000) or (Example: -p 1,2,3,4,5)") 
    options = parser.parse_args()
    return options.target, options.port

def new_socket():  # Function responsible for connecting to the IP via TCP

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.09)
    open_sockets.append(s)
    return s

def scan_port(port, host):

    s = new_socket()
    try:
        with s:
            result = s.connect_ex((host, port))
            if result == 0:
                print(colored(f"\n[+] Port {port} open", 'green'))
    except (socket.timeout, ConnectionRefusedError):
        pass
    finally:
        s.close()

def thread_ports(port_range, target): # Function in charge of threads

    with ThreadPoolExecutor(max_workers=50) as execute:
        execute.map(lambda port: scan_port(port, target), port_range) 

def parse_port_range(port_range_str):   # Filter function

    if '-' in port_range_str:
       start, end  = map(int, port_range_str.split('-')) 
       return range(start, end+1)
    elif ',' in port_range_str:
       return map(int, port_range_str.split(',')) 
    else:
       return (int(port_range_str),) 

def main():

    target, port_range_str = get_arguments()
    port_range = parse_port_range(port_range_str) 
    thread_ports(port_range, target)

if __name__ == '__main__':
    main() 

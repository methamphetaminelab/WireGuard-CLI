#!/usr/bin/env python3

import sys
import os
import subprocess
import threading
import time
from prompt_toolkit import PromptSession
from prompt_toolkit.shortcuts import clear
from prompt_toolkit.key_binding import KeyBindings
import requests

def colorize(text, color_code):
    return f'\033[{color_code}m{text}\033[0m'

def get_ip():
    try:
        response = requests.get('https://ifconfig.me')
        return response.text.strip()
    except requests.RequestException:
        return "Error fetching IP"

def update_ip(ip_status):
    while True:
        ip = get_ip()
        ip_status['ip'] = ip
        time.sleep(1)

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def get_status(config):
    try:
        result = subprocess.run(['wg', 'show'], capture_output=True, text=True, check=True)
        return "ENABLED" if config in result.stdout else "DISABLED"
    except subprocess.CalledProcessError:
        return "Error checking status"

def print_menu(status, ip, selected, expected_ip=None):
    clear()
    status_colors = {
        "ENABLED": '92',
        "DISABLED": '91',
        "Fetching...": '94',
        "Error": '91'
    }
    menu_colors = {
        "Enable": '92',
        "Disable": '91',
        "Exit": '94'
    }
    ip_color = '92' if ip == expected_ip else '91'
        
    print(f"{colorize('Status:', '96')} {colorize(status, status_colors.get(status, '91'))}")
    print(f"{colorize('IP:', '96')} {colorize(ip, ip_color)}\n")
    
    options = ["Enable", "Disable", "Exit"]
    for i, option in enumerate(options):
        color = menu_colors.get(option, '97')
        if i == selected:
            print(f"{colorize('>', '97')} {colorize(option, f'{color}')}")  
        else:
            print(f"  {colorize(option, f'{color}')}")  

def main(config):
    status = get_status(config)
    selected = 0
    options = ["Enable", "Disable", "Exit"]
    ip_status = {'ip': 'Fetching...'}
    config_file = open(f"/etc/wireguard/{config}.conf", "r")
    lines = config_file.readlines()
    for line in lines:
        if "Endpoint" in line:
            line = line.split(':')[0]
            expected_ip = line.split(' ')[2]
    threading.Thread(target=update_ip, args=(ip_status,), daemon=True).start()
    session = PromptSession()
    bindings = KeyBindings()

    @bindings.add('up')
    def move_up(event):
        nonlocal selected
        selected = (selected - 1) % len(options)
        print_menu(status, ip_status['ip'], selected, expected_ip)
    
    @bindings.add('down')
    def move_down(event):
        nonlocal selected
        selected = (selected + 1) % len(options)
        print_menu(status, ip_status['ip'], selected, expected_ip)
    
    @bindings.add('enter')
    def select(event):
        nonlocal status
        if selected == 0:
            execute_command(f"sudo wg-quick up {config}")
            status = get_status(config)
        elif selected == 1:
            execute_command(f"sudo wg-quick down {config}")
            status = get_status(config)
        elif selected == 2:
            raise KeyboardInterrupt

    try:
        while True:
            print_menu(status, ip_status['ip'], selected, expected_ip)
            session.prompt(key_bindings=bindings)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("This script must be run as root (use 'sudo').")
        sys.exit(1)
    
    config = None

    if len(sys.argv) == 3 and sys.argv[1] in ['--config', '-c']:
        config = sys.argv[2]
    else:
        configs = [f for f in os.listdir('/etc/wireguard') if f.endswith('.conf')]
        if configs:
            config = configs[0].replace('.conf', '')
        else:
            print("No WireGuard configuration files found in /etc/wireguard/")
            sys.exit(1)
    
    main(config)

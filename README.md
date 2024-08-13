# WireGuard-TUI
A simple utility providing a Wireguard console interface

# This Is Important
1. You need to install wireguard on your system.
2. There must be at least one config in /etc/wireguard/

# Automatic installation
1. ```git clone https://github.com/methamphetaminelab/WireGuard-TUI```
2. ```cd WireGuard-TUI/```
3. ```chmod +x install.sh```
4. ```./install.sh```

# Manual Installation
1. ```git clone https://github.com/methamphetaminelab/WireGuard-TUI```
2. ```cd WireGuard-TUI/```
3. ```pip install -r requirements.txt``` or ```python -m venv venv``` >> ```venv/bin/pip install -r requirements.txt```
4. ```chmod +x tuiguard.py```
5. ```sudo cp tuiguard.py /usr/local/bin/tuiguard```

# Usage
1. ```sudo tuiguard --config(-c) <config name file>```
2. Example: ```sudo tuiguard --config wg0```
3. Example: ```sudo tuiguard -c wg0```
4. Example: ```sudo tuiguard```

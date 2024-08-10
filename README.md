# WireGuard-CLI
Utility providing wireguard console interface

# Automatic installation
1. ```git clone https://github.com/methamphetaminelab/WireGuard-CLI```
2. ```cd WireGuard-CLI/```
3. ```chmod +x install.sh```
4. ```./install.sh```

# Manual Installation
1. ```git clone https://github.com/methamphetaminelab/WireGuard-CLI```
2. ```cd WireGuard-CLI/```
3. ```pip install -r requirements.txt``` or ```venv/bin/pip install -r requirements.txt```
4. ```chmod +x cliguard.py```
5. ```sudo cp cliguard.py /usr/local/bin/cliguard```

# Usage
1. ```sudo cliguard --config(-c) <config name file>```
2. Example: ```sudo cliguard --config wg0```
3. Example: ```sudo cliguard -c wg0```
4. Example: ```sudo cliguard```

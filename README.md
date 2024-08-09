# WireGuard-CLI
Utility providing wireguard console interface

# Automatic installation
```git clone https://github.com/methamphetaminelab/WireGuard-CLI```
```cd WireGuard-CLI/```
```chmod +x install.sh```
```./install.sh```

# Manual Installation
```git clone https://github.com/methamphetaminelab/WireGuard-CLI```
```cd WireGuard-CLI/```
```pip install -r requirements.txt``` or ```venv/bin/pip install -r requirements.txt```
```chmod +x cliguard.py```
```sudo cp cliguard.py /usr/local/bin/cliguard```

# Usage
```sudo cliguard --config(-c) <config name file>```
Example: ```sudo cliguard --config wg0```
Example: ```sudo cliguard -c wg0```
Example: ```sudo cliguard```

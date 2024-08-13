#!/bin/bash

if [ ! -f "requirements.txt" ]; then
    echo "The requirements.txt file was not found!"
    exit 1
fi

python -m venv venv

# Установка зависимостей из requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt
venv/bin/pip install -r requirements.txt    

# Проверка наличия tuiguard.py
if [ ! -f "tuiguard.py" ]; then
    echo "File tuiguard.py not found!"
    exit 1
fi

# Изменение прав доступа
echo "Changing access rights to tuiguard.py..."
chmod +x tuiguard.py

# Перемещение файла
echo "Moving tuiguard.py to /usr/local/bin/tuiguard..."
sudo cp tuiguard.py /usr/local/bin/tuiguard

echo "-----------------------------------       -"
echo "Installation completed successfully!"
echo "Usage example: sudo tuiguard --config(c) wg0 "
echo "Usage example: sudo tuiguard        "
echo "------------------------------------"

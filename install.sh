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

# Проверка наличия cliguard.py
if [ ! -f "cliguard.py" ]; then
    echo "File cliguard.py not found!"
    exit 1
fi

# Изменение прав доступа
echo "Changing access rights to cliguard.py..."
chmod +x cliguard.py

# Перемещение файла
echo "Moving cliguard.py to /usr/local/bin/cliguard..."
sudo cp cliguard.py /usr/local/bin/cliguard

echo "-----------------------------------       -"
echo "Installation completed successfully!"
echo "Usage example: sudo cliguard --config(c) wg0 "
echo "Usage example: sudo cliguard        "
echo "------------------------------------"

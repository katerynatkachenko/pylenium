#!/bin/bash -e

sudo apt update
sudo apt install -y firefox-geckodriver

wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm chromedriver_linux64.zip

sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver

python -m pip install --upgrade pip
pip install -r requirements.txt
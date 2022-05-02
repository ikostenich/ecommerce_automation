#!/usr/bin/bash

echo "Install prerequisite packages..."
apt install wget curl unzip -y

echo "Download the latest Chrome .deb file..."
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

apt-get update -y
apt-get install -y libgconf2-4 libnss3-1d libxss1

echo "Install Google Chrome..."
apt-get install -y ./google-chrome-stable_current_amd64.deb

echo "Fix dependencies..."
apt --fix-broken install -y



chromedriver_version=$(curl "https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
echo "Chromedriver version: ${chromedriver_version}"

echo "Downloading latest Chromedriver..."
curl -Lo chromedriver_linux64.zip "https://chromedriver.storage.googleapis.com/${chromedriver_version}/chromedriver_linux64.zip"

echo "Unzip the binary file and make it executable..."
mkdir -p "chromedriver/stable"

echo "unzip chromedriver"
unzip -q "chromedriver_linux64.zip" -d "chromedriver/stable"
chmod +x "chromedriver/stable/chromedriver"
mv "chromedriver/stable/chromedriver" "/usr/local/bin"
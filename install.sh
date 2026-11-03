#!/bin/bash

echo "[*] Installing Skybound Network..."

# Check for Docker
if ! command -v docker &> /dev/null; then
    echo "[!] Docker is not installed. Please install Docker first."
    echo "    On Kali: sudo apt install docker.io"
    echo "    On Windows: Install Docker Desktop and enable WSL2 integration."
    exit 1
fi

# Build the Docker Image
echo "[*] Building the Skybound Docker Image..."
sudo docker build -t skybound-image .

# Create the Launcher
echo "[*] Creating the 'skyward' command..."
sudo tee /usr/local/bin/skyward > /dev/null << 'LAUNCHER'
#!/bin/bash
if [ "$1" != "--init" ] || [ "$2" != "secure-recon" ]; then
    echo "Usage: skyward --init secure-recon"
    exit 1
fi

if ! sudo docker info >/dev/null 2>&1; then
    echo "[*] Starting Docker engine..."
    if command -v systemctl &> /dev/null; then
        sudo systemctl start docker
    else
        sudo dockerd > /tmp/dockerd.log 2>&1 &
        sleep 4
    fi
fi

if [ "$(sudo docker ps -q -f name=skybound-sandbox)" ]; then
    sudo docker exec -it skybound-sandbox python3 /usr/local/bin/skybound.py --boot
else
    if [ "$(sudo docker ps -aq -f name=skybound-sandbox)" ]; then
        sudo docker start -ai skybound-sandbox
    else
        sudo docker run -it --name skybound-sandbox -v ~/osint_results:/results skybound-image
    fi
fi
LAUNCHER

sudo chmod +x /usr/local/bin/skyward
echo "[+] Installation complete! Run: skyward --init secure-recon"

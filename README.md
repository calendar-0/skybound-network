[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-yellow.svg)](https://buymeacoffee.com/calendar0)

# 🛰️ Skybound Network

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Platform](https://img.shields.io/badge/platform-Kali%20Linux-red)
![Docker](https://img.shields.io/badge/docker-enabled-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**Skybound Network** is a Docker-isolated Open-Source Intelligence (OSINT) framework built for security researchers and analysts. It provides a secure, unified terminal environment to run reconnaissance tools without exposing your host machine to malicious payloads.

## ✨ Features
- **Isolated Sandbox:** All tools run inside a secure Docker container.
- **Unified Terminal UI:** A clean, interactive Python-based command-line interface.
- **20+ Built-in Tools:** Pre-installed and configured for immediate use.
- **Persistent Output:** Saves your terminal logs and data to your host machine.

## 🛠️ Included Tools
*   **Identity:** `sherlock`, `maigret`, `holehe`, `social-analyzer`
*   **Infrastructure:** `theHarvester`, `amass`, `subfinder`, `dnsx`, `dig`, `whois`, `whatweb`, `wafw00f`, `ffuf`, `dirb`
*   **Network:** `nmap`, `masscan`
*   **Secrets:** `trufflehog`, `gitleaks`
*   **General:** `exiftool`

## 🚀 Installation

### Prerequisites
- **Kali Linux** (or any Debian-based distro)
- **Docker** installed and running (`sudo apt install docker.io`)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/calendar-0/skybound-network.git
   cd skybound-network



2. Build the Docker image:
   sudo docker build -t skybound-image .

3. Run the Skybound Terminal:
   sudo docker run -it --name skybound-sandbox -v ~/osint_results:/results skybound-image

## Usage

Once inside the container, you will see the prompt. Type 'help' to see the full list of commands.

Example Commands:
sherlock <username>      # Find social media accounts
nmap <ip>                # Scan open ports
theharvester <domain>    # Gather emails and subdomains

### Installing Docker Desktop (Windows 10/11)

Docker Desktop is required to run Skybound on Windows. It provides the Docker engine and integrates with WSL 2.

1. Download Docker Desktop:
   Download the installer from the official website: https://www.docker.com/products/docker-desktop/

2. Run the Installer:
   Double-click the downloaded installer and follow the on-screen instructions. Ensure "Use WSL 2 instead of Hyper-V" is checked during installation.

3. Start Docker Desktop:
   After installation, launch Docker Desktop from your Start Menu. Wait for the whale icon in your system tray to stop animating.

4. Enable WSL Integration (Crucial Step):
   - Click the gear icon (Settings) in the top right of Docker Desktop.
   - Go to Resources > WSL Integration.
   - Toggle on "Enable integration with my default WSL distro".
   - Find Kali Linux in the list below and toggle it ON.
   - Click Apply & Restart.

5. Verify Installation:
   Open your Kali Linux terminal and run: docker --version
   If it prints a version number, you are ready to continue.

### Windows Installation (WSL)

If you are on Windows 10 or 11, you do not need to dual-boot. You can run Skybound using the Windows Subsystem for Linux (WSL).

1. Install WSL and Kali Linux:
   Open PowerShell as Administrator and run: wsl --install -d kali-linux
   (Restart your computer if prompted).

2. Open Kali Linux:
   Open the Kali Linux app from your Windows Start Menu. Once the terminal opens, run the clone, build, and run commands exactly as written in the setup section above.

## Disclaimer

This tool is for educational purposes and authorized security testing only. The developers are not responsible for any misuse or illegal activities performed with this software. Always ensure you have permission to investigate a target.

## License

This project is licensed under the MIT License.

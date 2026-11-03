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

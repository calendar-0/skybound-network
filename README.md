# Skybound Network

An isolated, Docker-based OSINT environment designed for Kali Linux.

## Features
- Isolated Docker sandbox to safely run tools.
- Interactive Python CLI wrapper.
- Includes: Sherlock, Maigret, Holehe, Nmap, theHarvester, dnsx, gitleaks, trufflehog.

## Requirements
- **Linux (Kali preferred):** Docker (sudo apt install docker.io)
- **Windows:** WSL2 with Kali Linux installed, and Docker Desktop installed with WSL2 integration enabled.

## Installation
1. git clone https://github.com/calendar-0/skybound-network.git
2. cd skybound-network
3. sudo bash install.sh

## Usage
skyward --init secure-recon

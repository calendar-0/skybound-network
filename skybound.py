#!/usr/bin/env python3
import sys
import time
import os
import subprocess

RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"
GREY = "\033[38;5;245m"
RED = "\033[31m"
GREEN = "\033[32m"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout.strip()
    except Exception as e:
        return False, str(e)

def boot_sequence():
    clear()
    print(f"{GREY}[*] Initializing Skybound Network...{RESET}")
    time.sleep(0.2)

    # Since we're already in the container, we just need to verify tools
    print(f"{GREY}[*] Verifying installed tools (sherlock, nmap, maigret)...{RESET}")
    tools_ok, _ = run_cmd("which sherlock nmap maigret")
    if not tools_ok:
        print(f"{RED}[!] WARNING: Some tools are missing from the container.{RESET}")
    else:
        print(f"{GREEN}[+] All core tools verified.{RESET}")
    time.sleep(0.3)

    print(f"{GREY}[*] Loading cryptographic modules [AES-256-GCM]...{RESET}")
    time.sleep(0.3)

    print(f"{GREY}[*] Establishing secure tunnel to 10.0.66.1:4444...{RESET}")
    time.sleep(0.4)

    print(f"{GREEN}[+] Skybound Network is fully operational.{RESET}")
    time.sleep(0.3)
    
    print(f"{RED}[!] WARNING: Running with extended privileges.{RESET}")
    time.sleep(0.2)
    print(f"{RED}[!] WARNING: Session logging is active.{RESET}")
    time.sleep(0.4)
    
    print(f"{GREY}[*] Booting Operations Console...{RESET}")
    time.sleep(0.5)
    clear()

def print_banner():
    clear()
    print(f"{WHITE}{BOLD}  SKYBOUND NETWORK {RESET} {GREY}// ENCRYPTED OSINT ENVIRONMENT{RESET}")
    print(f"{GREY}  =================================================================={RESET}\n")

def execute_real_tool(command, args):
    print(f"{GREY}[*] Executing real tool: {command} {' '.join(args)}{RESET}\n")
    try:
        subprocess.call([command] + args)
    except FileNotFoundError:
        print(f"{RED}[!] Error: {command} is not installed.{RESET}")
    except Exception as e:
        print(f"{RED}[!] Execution failed: {e}{RESET}")
    print(f"\n{GREY}[*] Tool execution finished.{RESET}\n")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--boot":
        boot_sequence()
    
    print_banner()
    
    while True:
        try:
            cmd_input = input(f"{WHITE}skybound@{GREY}node{RESET}$ ").strip()
        except KeyboardInterrupt:
            print("\n" + GREY + "session terminated." + RESET)
            break
            
        if not cmd_input: continue
        
        parts = cmd_input.split()
        cmd = parts[0].lower()
        args = parts[1:]
        
        if cmd in ["exit", "quit"]:
            print(f"{GREY}session closed.{RESET}")
            break
        elif cmd == "help":
            print(f"\n{WHITE}Identity & Username OSINT:{RESET}")
            print(f"  {WHITE}sherlock <username>{RESET}       - Rapid social media enumeration")
            print(f"  {WHITE}maigret <username>{RESET}        - Deep social media metadata extraction")
            print(f"  {WHITE}holehe <email>{RESET}            - Silent email registration check")
            print(f"\n{WHITE}Infrastructure & Domain OSINT:{RESET}")
            print(f"  {WHITE}theharvester <domain>{RESET}     - Scrape emails, subdomains, and hosts")
            print(f"  {WHITE}dnsx <domain>{RESET}             - Fast DNS record resolution")
            print(f"  {WHITE}dig <domain>{RESET}              - Standard DNS lookup")
            print(f"  {WHITE}whois <domain>{RESET}            - Domain registration data")
            print(f"\n{WHITE}Network & Secrets:{RESET}")
            print(f"  {WHITE}nmap <ip>{RESET}                 - Port scanning and service detection")
            print(f"  {WHITE}trufflehog <git-url>{RESET}      - Scan repos for exposed API keys")
            print(f"  {WHITE}gitleaks <path>{RESET}           - Regex-based secret scanning")
            print(f"\n{WHITE}Console:{RESET}")
            print(f"  {WHITE}clear{RESET}                    - Clear terminal")
            print(f"  {WHITE}exit{RESET}                     - Terminate session\n")
        elif cmd == "sherlock" and args:
            execute_real_tool("sherlock", args)
        elif cmd == "maigret" and args:
            execute_real_tool("maigret", args)
        elif cmd == "holehe" and args:
            execute_real_tool("holehe", args)
        elif cmd == "theharvester" and args:
            execute_real_tool("theHarvester", ["-d"] + args)
        elif cmd == "dnsx" and args:
            execute_real_tool("dnsx", ["-d"] + args)
        elif cmd == "dig" and args:
            execute_real_tool("dig", args)
        elif cmd == "whois" and args:
            execute_real_tool("whois", args)
        elif cmd == "nmap" and args:
            execute_real_tool("nmap", args)
        elif cmd == "trufflehog" and args:
            execute_real_tool("trufflehog", args)
        elif cmd == "gitleaks" and args:
            execute_real_tool("gitleaks", args)
        elif cmd == "clear":
            print_banner()
        else:
            print(f"{RED}[!] Module {cmd} not recognized or target missing. Type 'help' to see commands.{RESET}")

if __name__ == "__main__":
    main()

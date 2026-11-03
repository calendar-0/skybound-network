FROM kalilinux/kali-rolling

RUN apt update && apt install -y \
    nmap whois dnsutils theharvester dnsx gitleaks \
    curl git python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install sherlock-project maigret holehe --break-system-packages --ignore-installed certifi

COPY skybound.py /usr/local/bin/skybound.py
RUN chmod +x /usr/local/bin/skybound.py

RUN mkdir /results

# Run the script with the --boot flag when the container starts
CMD ["python3", "/usr/local/bin/skybound.py", "--boot"]

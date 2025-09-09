#  Cybersecurity Offense, Defense & Anonymity Lab Series

Six Cybersecurity Projects on Attack, Defense, and Anonymity

This repository is a collection of six cybersecurity projects developed
for academic research and demonstration.\
All experiments are conducted in **legal, controlled environments**,
focusing on **Wi-Fi security, packet analysis, penetration testing,
system defense, automation, anonymity, and C2 architecture**.

------------------------------------------------------------------------

＃＃　Projects Overview
＃＃＃　1. Fake Wi-Fi Hotspot & Phishing Login Page Attack

-   Description: Simulates how an attacker sets up a fake Wi-Fi hotspot and phishing page to demonstrate login risks in public networks, combined with user awareness training.

-   Key Techniques:

        １. Fake AP setup: Using airbase-ng to broadcast a virtual SSID, with dnsmasq providing DHCP and DNS spoofing.

        ２. Phishing login page: HTML + PHP fake login page simulating credential submission.

        ３. Controlled environment demo: Credentials are destroyed instantly after input; login redirects to a warning page emphasizing awareness and defense.

------------------------------------------------------------------------

###　2. Wi-Fi Packet Detection & Analysis (Passive)

-   Description: Captures Beacon, Probe, and Data Frames in Monitor Mode and analyzes them with Wireshark and Python.

-   Key Techniques:

        １. Packet capture in Monitor Mode: USB Wi-Fi adapter + airodump-ng/tcpdump.

        ２. Wireshark analysis: Filtering Beacon/Probe/Deauth frames and analyzing traffic patterns.

        ３. Automated statistics: Python (Scapy/pyshark) script mac_stats.py for MAC address statistics and traffic trend analysis.

------------------------------------------------------------------------

＃＃＃ 3. From Exploitation to Defense (Reverse Shell & Backdoor Exercise)

-   Description: Establishes a reverse shell on an OWASP BWA target VM, escalates to root, and validates defense measures.

-   Key Techniques:

        1. Reverse shell: Using bash TCP + Netcat to obtain root access.

        2. Sensitive data access: Reading /etc/shadow and /etc/passwd.

        3. Defense validation: Testing fail2ban, auditd, and tripwire against brute-force, backdoors, and file tampering.

------------------------------------------------------------------------

###　4. Linux Automated Backup & Monitoring

-   Description: Designs an automated backup system integrating Shell scripts, systemd, Docker, and log management with one-click deployment.

-   Key Techniques:

        １. Automated backup: Shell script compresses and removes outdated files.

        ２. Containerization & scheduling: Docker packaging with systemd timer for scheduled tasks.

        ３. Error monitoring & notifications: Slack/LINE Notify integration; automatic restarts to ensure reliability.

------------------------------------------------------------------------

### 5. Dynamic Identity Obfuscation with Tor & SOCKS5 Proxy

-   Description: Develops ghost_mode3.py, a script that rotates IP addresses through Tor + SOCKS5 every few seconds, with obfs4 obfuscation support.

-   Key Techniques:

        1. Tor + SOCKS5 integration: Python stem controls Tor via socks5h://127.0.0.1:9050.

        2. Automatic IP switching: ghost_mode3.py issues NEWNYM requests periodically.

        3. Anti-blocking obfuscation: obfs4 bridge protocol to bypass DPI and censorship.

------------------------------------------------------------------------

### 6. Experimental C2 Architecture & Defense Analysis

-   Description: Implements a basic C2 architecture in Python sockets for remote command/control simulation and explores defensive strategies.

-   Key Techniques:

        1. C2 implementation: Python socket server-client with exec, upload/download, and scan_lan.

        2. Simulated malicious functions: screenshot, camera capture, mic recording, and keylogging (for demonstration only).
    
        3. Defense research: Detecting C2 traffic and anomalies with auditd, lsof, and syslog.

------------------------------------------------------------------------

### Legal & Ethical Disclaimer

-   All projects are executed in isolated lab environments only, with no unauthorized third-party testing.

-   The sole purpose of this research is cybersecurity education and demonstration, with no malicious intent.

------------------------------------------------------------------------

##  Topics

`cybersecurity` `penetration-testing` `reverse-shell` `tor` `c2` `linux`
`wireshark`

------------------------------------------------------------------------

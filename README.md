#  Cybersecurity Offense, Defense & Anonymity Lab Series

六個資安攻防與匿名技術實驗專題合集

This repository is a collection of six cybersecurity projects developed
for academic research and demonstration.\
All experiments are conducted in **legal, controlled environments**,
focusing on **Wi-Fi security, packet analysis, penetration testing,
system defense, automation, anonymity, and C2 architecture**.

------------------------------------------------------------------------

##  專題總覽 Projects Overview

### 1 假 Wi-Fi 熱點與釣魚登入頁攻擊實作

-   **簡介**：模擬駭客建立假 Wi-Fi
    熱點與釣魚頁，展示公共網路下的登入風險，並加入使用者教育。\
-   **技術重點**：
    1.  Fake AP 建立：使用 airbase-ng 廣播虛擬 SSID，透過 dnsmasq 提供
        DHCP 與 DNS 偽導。\
    2.  釣魚登入頁設計：HTML + PHP 假登入頁，模擬帳密輸入與回傳。\
    3.  封閉環境展示：輸入帳密即時銷毀，登入後顯示警示頁，強調教育與防禦。\

------------------------------------------------------------------------

### 2 Wi-Fi 封包偵測與分析（被動式）

-   **簡介**：使用 Monitor Mode 被動擷取 Beacon、Probe、Data Frame，並以
    Wireshark + Python 分析。\
-   **技術重點**：
    1.  Monitor Mode 封包擷取：USB 無線網卡 + airodump-ng/tcpdump
        擷取。\
    2.  Wireshark 分析：過濾 Beacon/Probe/Deauth，統計流量特徵。\
    3.  自動化統計：Python (Scapy/pyshark) 腳本 `mac_stats.py` 統計 MAC
        與流量趨勢。\

------------------------------------------------------------------------

### 3 從滲透到防禦 (反向 Shell 與後門實戰演練)

-   **簡介**：在 OWASP BWA 靶機上建立反向 Shell，取得 root
    權限並進行防禦驗證。\
-   **技術重點**：
    1.  反向 Shell 建立：bash TCP + Netcat 成功取得 root 權限。\
    2.  敏感資訊存取：讀取 /etc/shadow 與 /etc/passwd。\
    3.  防禦驗證：fail2ban、auditd、tripwire
        實測防禦爆破、後門與檔案竄改。\

------------------------------------------------------------------------

### 4 Linux 系統自動化備份與監控

-   **簡介**：設計自動化備份系統，整合 Shell Script、systemd、Docker 與
    log 管理，支援一鍵部署。\
-   **技術重點**：
    1.  自動化備份：Shell Script 壓縮與清理舊檔。\
    2.  容器化與排程：Docker 封裝，systemd timer 定時執行。\
    3.  錯誤監控與通知：Slack/LINE Notify
        傳送狀態，自動重啟確保可靠性。\

------------------------------------------------------------------------

### 5 結合 Tor 與 SOCKS5 Proxy 的動態身份隱藏系統

-   **簡介**：開發 `ghost_mode3.py` 腳本，每隔數秒透過 Tor + SOCKS5
    自動換 IP，並支援 obfs4 混淆。\
-   **技術重點**：
    1.  Tor + SOCKS5 整合：Python stem 控制 Tor，導入
        socks5h://127.0.0.1:9050。\
    2.  自動 IP 切換：ghost_mode3.py 每隔數秒發送 NEWNYM 指令。\
    3.  抗封鎖混淆：obfs4 橋接協議，繞過 DPI 與網路審查。\

------------------------------------------------------------------------

### 6 C2 架構之實驗性實作與資安防禦探討

-   **簡介**：以 Python Socket 開發簡易 C2
    架構，模擬檔案傳輸、遠端指令與 Keylogger，並探討防禦對策。\
-   **技術重點**：
    1.  C2 架構實作：Python socket 建立 server-client，支援
        exec、upload/download、scan_lan。\
    2.  模擬惡意功能：screenshot、camera_snap、mic_record、keylog
        模擬實作。\
    3.  防禦研究：auditd、lsof、syslog 偵測 C2 流量與異常行為。\

------------------------------------------------------------------------

##  合法性與道德聲明

-   所有專題皆於 **封閉實驗環境** 進行，未涉及第三方未授權測試。\
-   研究目的為 **資訊安全教育、研究展示**，無任何惡意用途。

------------------------------------------------------------------------

##  Topics

`cybersecurity` `penetration-testing` `reverse-shell` `tor` `c2` `linux`
`wireshark`

------------------------------------------------------------------------

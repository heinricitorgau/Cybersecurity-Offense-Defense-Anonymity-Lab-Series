#  Cybersecurity Offense, Defense & Anonymity Lab Series  
六個資安攻防與匿名技術實驗專題合集

This repository is a collection of six cybersecurity projects developed for academic research and demonstration.  
All experiments are conducted in **legal, controlled environments**, focusing on **Wi-Fi security, packet analysis, penetration testing, system defense, automation, anonymity, and C2 architecture**.

---

##  專題總覽 Projects Overview

### 1 假 Wi-Fi 熱點與釣魚登入頁攻擊實作
- **簡介**：模擬駭客建立假 Wi-Fi 熱點與釣魚頁，展示公共網路下的登入風險，並加入使用者教育。  
- **關鍵字**：Fake AP, Phishing, Captive Portal  
-  *(可插入釣魚頁面截圖或流程圖)*

---

### 2 Wi-Fi 封包偵測與分析（被動式）
- **簡介**：使用 Monitor Mode 被動擷取 Beacon、Probe、Data Frame，並以 Wireshark + Python 分析。  
- **關鍵字**：Wireshark, Passive Sniffing, Packet Analysis  
-  *(可插入 Wireshark Beacon/Probe Response 截圖)*

---

### 3 從滲透到防禦 (反向 Shell 與後門實戰演練)
- **簡介**：在 OWASP BWA 靶機上建立反向 Shell，取得 root 權限並進行防禦驗證。  
- **關鍵字**：Reverse Shell, Privilege Escalation, Defense  
-  *(可插入反向 shell 建立截圖)*

---

### 4 Linux 系統自動化備份與監控
- **簡介**：設計自動化備份系統，整合 Shell Script、systemd、Docker 與 log 管理，支援一鍵部署。  
- **關鍵字**：Linux, Automation, Backup, Docker  
-  *(可插入流程圖或 deploy.sh 部署截圖)*

---

### 5 結合 Tor 與 SOCKS5 Proxy 的動態身份隱藏系統
- **簡介**：開發 `ghost_mode3.py` 腳本，每隔數秒透過 Tor + SOCKS5 自動換 IP，並支援 obfs4 混淆。  
- **關鍵字**：Tor, SOCKS5, Anonymity, Obfs4  

---

### 6 C2 架構之實驗性實作與資安防禦探討
- **簡介**：以 Python Socket 開發簡易 C2 架構，模擬檔案傳輸、遠端指令、Keylogger（模擬），並探討防禦對策。  
- **關鍵字**：C2, Command & Control, Red/Blue Team, Detection  

---

##  合法性與道德聲明
- 所有專題皆於 **封閉實驗環境** 進行，未涉及第三方未授權測試。  
- 研究目的為 **資訊安全教育、研究展示**，無任何惡意用途。  

---

import time
import csv
import requests
from stem import Signal
from stem.control import Controller
from datetime import datetime

# === Configurable Parameters ===
WAIT_TIME = 10              # Seconds to wait after NEWNYM
TOTAL_CYCLES = 20           # Number of IP rotations to test
LOG_FILE = "log_geo.csv"    # Output CSV file

PROXIES = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

def get_current_ip():
    try:
        response = requests.get("http://httpbin.org/ip", proxies=PROXIES, timeout=10)
        return response.json()['origin']
    except:
        return None

def get_geo_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=country,city,org", timeout=5)
        data = response.json()
        return data.get("country", ""), data.get("city", ""), data.get("org", "")
    except:
        return "", "", ""

def run_test():
    with open(LOG_FILE, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Cycle", "Timestamp", "Duration (s)", "IP", "Status", "Country", "City", "Organization"])

        success_count = 0
        total_duration = 0

        for i in range(1, TOTAL_CYCLES + 1):
            print(f" Cycle {i}: Requesting new IP...")

            start_time = time.time()
            renew_tor_ip()
            time.sleep(WAIT_TIME)
            ip = get_current_ip()
            duration = round(time.time() - start_time, 2)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if ip:
                country, city, org = get_geo_info(ip)
                status = "Success"
                success_count += 1
                total_duration += duration
                print(f"V Success: {ip} ({country}, {city}, {org}) - {duration} seconds")
            else:
                ip, country, city, org = "-", "", "", ""
                status = "Failed"
                print(f"X Failed - {duration} seconds")

            writer.writerow([i, timestamp, duration, ip, status, country, city, org])
            time.sleep(1)

        print("\n Test Completed!")
        print(f"Total Successes: {success_count}/{TOTAL_CYCLES}")
        print(f"Success Rate: {round(success_count / TOTAL_CYCLES * 100, 2)}%")
        if success_count > 0:
            print(f"Average Successful Duration: {round(total_duration / success_count, 2)} seconds")

if __name__ == "__main__":
    run_test()

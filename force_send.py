import requests
import time

# Target: cosmicph.serv.nu
HOST = "104.225.253.34"
PORT = 25565
USERNAME = "Bonjur123" 
COMMANDS = [
    "/register password123 password123", 
    "/login password123",
    "Hello from the pentest bot!",
    "/help",
    "/plugins"
]

print(f"[*] Disconnecting any stale bot first...")
try:
    requests.post('http://localhost:6969/disconnect', json={"host": HOST, "port": PORT, "username": USERNAME}, timeout=2)
except:
    pass

print(f"[*] Connecting {USERNAME} to {HOST}:{PORT}...")
# Connecting directly (mineflayer handles the connection)
resp = requests.post('http://localhost:6969/connect', json={"host": HOST, "port": PORT, "username": USERNAME})
print(f"[*] API Response: {resp.status_code} - {resp.text}")

print("[*] Waiting 20 seconds for connection/handshake...")
time.sleep(20)

for cmd in COMMANDS:
    print(f"[*] Sending: {cmd}")
    try:
        r = requests.post('http://localhost:6969/send', json={"host": HOST, "port": PORT, "username": USERNAME, "message": cmd}, timeout=5)
        print(f"    Response: {r.status_code} - {r.text}")
    except Exception as e:
        print(f"    Error: {e}")
    time.sleep(3)

print("[*] Done.")

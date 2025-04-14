import requests
import time
from datetime import datetime

# === CONFIGURATION ===
URLS = [
    "https://polytex-toolkit.streamlit.app/?keepalive=true",
    "https://polytex-alerts.streamlit.app/?keepalive=true",
    "https://polytex-repeatedcalls.streamlit.app/?keepalive=true"
]

INTERVAL_MINUTES = 5

# === FUNCTIONALITY ===
def ping_all():
    print(f"🔁 Pinging apps at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    for url in URLS:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                print(f"✅ {url} is UP")
            else:
                print(f"⚠️ {url} responded with status: {response.status_code}")
        except Exception as e:
            print(f"❌ Error pinging {url}: {e}")

# === MAIN LOOP ===
if __name__ == "__main__":
    while True:
        ping_all()
        print(f"🕒 Waiting {INTERVAL_MINUTES} minutes...\n")
        time.sleep(INTERVAL_MINUTES * 60)
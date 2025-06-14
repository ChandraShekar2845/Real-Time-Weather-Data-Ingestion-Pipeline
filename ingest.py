# ingest.py
import requests, json, os
from datetime import datetime
import pandas as pd

CONFIG = json.load(open("config/config.json"))
url = f"https://api.openweathermap.org/data/2.5/weather?q={CONFIG['city']}&appid={CONFIG['api_key']}&units={CONFIG['units']}"

response = requests.get(url)
data = response.json()

# Save raw JSON
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs("data/raw", exist_ok=True)
with open(f"data/raw/weather_{timestamp}.json", "w") as f:
    json.dump(data, f)

# Convert to flat CSV
df = pd.json_normalize(data)
os.makedirs("data/processed", exist_ok=True)
df.to_csv(f"data/processed/weather_{timestamp}.csv", index=False)

print("Data ingested and saved!")

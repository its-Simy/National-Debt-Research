import requests, pandas as pd, os
from dotenv import load_dotenv

load_dotenv()                              # pulls your FRED_API_KEY
api_key = os.getenv("FRED_API_KEY")

endpoint = "https://api.stlouisfed.org/fred/series/observations"
params = {
    "series_id": "NGDPSAXDCUSQ",           # <- swap if you want NSA or BEA GDP
    "api_key": api_key,
    "file_type": "json",
    "observation_start": "2000-01-01",
    "observation_end":   "2025-12-31"
}

raw = requests.get(endpoint, params=params).json()

if "observations" not in raw:                # quick sanity-check
    raise ValueError(f"API problem:\n{raw}")

df = pd.DataFrame(raw["observations"])
df["value"] = pd.to_numeric(df["value"], errors="coerce")  # <-- numeric GDP
df["date"]  = pd.to_datetime(df["date"])

print(df.head())       # first few rows
print(df.tail())       # last few rows
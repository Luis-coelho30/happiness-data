import zipfile
import requests
import io
import pandas as pd

def read_zip_wbd(indicator: str) -> pd.DataFrame:
  url = f"https://api.worldbank.org/v2/en/indicator/{indicator}?downloadformat=csv"
  response = requests.get(url)
  
  with zipfile.ZipFile(io.BytesIO(response.content)) as z:
      csv_files = [f for f in z.namelist() if f.startswith("API_")]
      
      if not csv_files:
          return pd.NA
      
      with z.open(csv_files[0]) as f:
          df = pd.read_csv(f, skiprows=4)
  
  return df

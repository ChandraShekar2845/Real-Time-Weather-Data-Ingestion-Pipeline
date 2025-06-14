import pandas as pd
import sys

def validate(file_path):
    df = pd.read_csv(file_path)
    assert not df.isnull().values.any(), "Null values found!"
    assert "main.temp" in df.columns, "Missing temperature data!"
    print("Data validation passed ✅")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate.py <file_path>")
    else:
        validate(sys.argv[1])
    
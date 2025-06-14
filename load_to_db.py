import psycopg2
import pandas as pd

df = pd.read_csv("data/processed/latest_weather.csv")

conn = psycopg2.connect(database="weatherdb", user="postgres", password="yourpass", host="localhost", port="5432")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_data (
    city TEXT, temp FLOAT, humidity INT, timestamp TIMESTAMP
);
""")

cursor.execute("DELETE FROM weather_data")

for _, row in df.iterrows():
    cursor.execute("INSERT INTO weather_data (city, temp, humidity, timestamp) VALUES (%s, %s, %s, now())",
                   ("Hyderabad", row["main.temp"], row["main.humidity"]))

conn.commit()
conn.close()
print("Data loaded into PostgreSQL ✅")

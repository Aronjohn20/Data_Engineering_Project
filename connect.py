import mysql.connector
import pandas as pd

# MySQL connection configuration
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "rko111--",
    "database": "weather_pipeline"
}

# Connect to MySQL
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    print("Connected to MySQL successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

# Load cleaned data
hourly_df = pd.read_csv("hourly_data_cleaned.csv")
daily_df = pd.read_csv("daily_data_cleaned.csv")

# Create tables if they don't exist
create_hourly_table = """
CREATE TABLE IF NOT EXISTS hourly_weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATETIME,
    temperature_2m FLOAT,
    relative_humidity_2m FLOAT,
    precipitation FLOAT,
    precipitation_probability FLOAT
)
"""

create_daily_table = """
CREATE TABLE IF NOT EXISTS daily_weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATETIME,
    weather_code INT
)
"""

cursor.execute(create_hourly_table)
cursor.execute(create_daily_table)
print("Tables created successfully!")

# Insert data into tables
for index, row in hourly_df.iterrows():
    insert_hourly = "INSERT INTO hourly_weather (date, temperature_2m, relative_humidity_2m, precipitation, precipitation_probability) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_hourly, (row['date'], row['temperature_2m'], row['relative_humidity_2m'], row['precipitation'], row['precipitation_probability']))

for index, row in daily_df.iterrows():
    insert_daily = "INSERT INTO daily_weather (date, weather_code) VALUES (%s, %s)"
    cursor.execute(insert_daily, (row['date'], row['weather_code']))

connection.commit()
print("Data inserted successfully!")

cursor.close()
connection.close()
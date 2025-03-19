import pandas as pd

# Load the CSV file
file_path = "USDDKK2024_used.csv"  # Update to your actual filename
df = pd.read_csv(file_path)

# Convert "Time" column to datetime format
df["Time"] = pd.to_datetime(df["Time"], format="%Y.%m.%d.%H:%M")

# Set "Time" as the index
df.set_index("Time", inplace=True)

# Resample to 5-minute intervals with proper OHLC aggregation
df_resampled = df.resample("5T").agg({
    "Open": "first",   # First value in the interval
    "High": "max",     # Highest value in the interval
    "Low": "min",      # Lowest value in the interval
    "Close": "last"    # Last value in the interval
})

# Drop rows with NaN (in case of missing data)
df_resampled.dropna(inplace=True)

# Save to CSV with the same date format as input
df_resampled.to_csv("usd_dkk_5min.csv", date_format="%Y.%m.%d.%H:%M")

print("Resampling complete! Saved as 'usd_dkk_5min.csv'.")

import pandas as pd


hourly_dataframe = pd.read_csv("hourly_data.csv")
daily_dataframe = pd.read_csv("daily_data.csv")

date_columns = ["date"]
for df in [hourly_dataframe, daily_dataframe]:
    for date_col in date_columns:
        if date_col in df.columns:
            df[date_col] = pd.to_datetime(df[date_col], format="ISO8601")

# print(hourly_dataframe.columns)
hourly_dataframe.drop(columns=["dew_point_2m", "snow_depth"], inplace=True)

# Add metadata for the loaded and cleaned dataframes after dropping columns
hourly_dataframe.attrs["metadata"] = {
    "source_file": "hourly_data.csv",
    "rows": len(hourly_dataframe),
    "columns": list(hourly_dataframe.columns),
    "load_time": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
}
daily_dataframe.attrs["metadata"] = {
    "source_file": "daily_data.csv",
    "rows": len(daily_dataframe),
    "columns": list(daily_dataframe.columns),
    "load_time": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
}
print("Hourly metadata:", hourly_dataframe.attrs["metadata"])
print("Daily metadata:", daily_dataframe.attrs["metadata"])
print(hourly_dataframe.dtypes)

hourly_metadata_df = pd.DataFrame([hourly_dataframe.attrs["metadata"]])
daily_metadata_df = pd.DataFrame([daily_dataframe.attrs["metadata"]])
hourly_metadata_df.to_csv("hourly_metadata.csv", index=False)
daily_metadata_df.to_csv("daily_metadata.csv", index=False)
print("\nMetadata exported to hourly_metadata.csv and daily_metadata.csv")


hourly_dataframe.to_csv("hourly_data_cleaned.csv", index=False)
daily_dataframe.to_csv("daily_data_cleaned.csv", index=False)
print("Cleaned data exported to hourly_data_cleaned.csv and daily_data_cleaned.csv")


import pandas as pd


def extract_data():
    print("Starting Extract...")
    data = pd.read_csv("raw_rides.csv")
    print(f"Extracted {len(data)} records")
    return data


def transform_data(data):
    print("Starting Transform...")

    data = data.copy()

    data["ride_date"] = pd.to_datetime(data["ride_date"])

    # Data quality checks
    if (data["distance_km"] <= 0).any():
        raise ValueError("Invalid distance detected!")

    if (data["duration_min"] <= 0).any():
        raise ValueError("Invalid duration detected!")

    if (data["fare"] < 0).any():
        raise ValueError("Invalid fare detected!")

    # Transformations
    data["ride_month"] = data["ride_date"].dt.month
    data["ride_day"] = data["ride_date"].dt.day
    data["ride_hour"] = data["ride_date"].dt.hour
    data["fare_per_km"] = data["fare"] / data["distance_km"]

    print("Transformation completed")

    return data


def load_data(data):
    print("Starting Load...")
    data.to_csv("processed_rides.csv", index=False)
    print(f"Loaded {len(data)} records")
    print("Processed data saved successfully!")


def run_pipeline():
    raw_data = extract_data()
    transformed_data = transform_data(raw_data)
    load_data(transformed_data)

    print("\n===== ETL PIPELINE COMPLETED =====")


if __name__ == "__main__":
    run_pipeline()

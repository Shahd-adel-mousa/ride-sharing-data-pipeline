import pandas as pd


def extract_data():
    print("Starting Extract...")

    data = pd.read_csv("../data/raw/raw_rides.csv")

    print(f"Extracted {len(data)} records")

    return data


def validate_data(data):
    print("Running Data Quality Checks...")

    # Check for duplicate ride IDs
    if data["ride_id"].duplicated().any():
        raise ValueError("Duplicate ride_id detected!")

    # Check for missing values
    if data.isnull().any().any():
        missing_columns = data.columns[data.isnull().any()].tolist()

        # Rating can be missing for cancelled rides
        unexpected_missing = [
            col for col in missing_columns
            if col != "rating"
        ]

        if unexpected_missing:
            raise ValueError(
                f"Missing values detected in: {unexpected_missing}"
            )

    # Check distance
    if (data["distance_km"] <= 0).any():
        raise ValueError("Invalid distance detected!")

    # Check duration
    if (data["duration_min"] <= 0).any():
        raise ValueError("Invalid duration detected!")

    # Check fare
    if (data["fare"] < 0).any():
        raise ValueError("Invalid fare detected!")

    # Check ride status
    valid_statuses = {"Completed", "Cancelled"}

    if not data["ride_status"].isin(valid_statuses).all():
        raise ValueError("Invalid ride status detected!")

    print("All Data Quality Checks passed!")


def transform_data(data):
    print("Starting Transform...")

    data = data.copy()

    data["ride_date"] = pd.to_datetime(data["ride_date"])

    # Run data quality checks
    validate_data(data)

    # Transformations
    data["ride_month"] = data["ride_date"].dt.month
    data["ride_day"] = data["ride_date"].dt.day
    data["ride_hour"] = data["ride_date"].dt.hour

    data["fare_per_km"] = (
        data["fare"] / data["distance_km"]
    )

    print("Transformation completed")

    return data


def load_data(data):
    print("Starting Load...")

    data.to_csv(
        "../data/processed/processed_rides.csv",
        index=False
    )

    print(f"Loaded {len(data)} records")
    print("Processed data saved successfully!")


def run_pipeline():
    raw_data = extract_data()

    transformed_data = transform_data(raw_data)

    load_data(transformed_data)

    print("\n===== ETL PIPELINE COMPLETED =====")


if __name__ == "__main__":
    run_pipeline()

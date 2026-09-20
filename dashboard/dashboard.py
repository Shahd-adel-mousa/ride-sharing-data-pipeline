import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# Connect to the SQLite database
conn = sqlite3.connect("../ride_sharing.db")


# Load rides data
rides = pd.read_sql("SELECT * FROM rides", conn)

# Convert ride_date to datetime
rides["ride_date"] = pd.to_datetime(rides["ride_date"])


# ==========================================
# 1. Ride Status Distribution
# ==========================================

status_counts = rides["ride_status"].value_counts()

plt.figure(figsize=(6, 4))
status_counts.plot(kind="bar")

plt.title("Ride Status Distribution")
plt.xlabel("Ride Status")
plt.ylabel("Number of Rides")

plt.tight_layout()
plt.show()


# ==========================================
# 2. Revenue by Payment Method
# ==========================================

revenue_payment = (
    rides[rides["ride_status"] == "Completed"]
    .groupby("payment_method")["fare"]
    .sum()
)

plt.figure(figsize=(6, 4))
revenue_payment.plot(kind="bar")

plt.title("Revenue by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()


# ==========================================
# 3. Rides by Pickup Location
# ==========================================

pickup_counts = rides["pickup_location"].value_counts()

plt.figure(figsize=(7, 4))
pickup_counts.plot(kind="bar")

plt.title("Rides by Pickup Location")
plt.xlabel("Pickup Location")
plt.ylabel("Number of Rides")

plt.tight_layout()
plt.show()


# ==========================================
# 4. Rides by Hour
# ==========================================

rides_by_hour = rides.groupby("ride_hour").size()

plt.figure(figsize=(7, 4))
rides_by_hour.plot(kind="line", marker="o")

plt.title("Rides by Hour")
plt.xlabel("Hour")
plt.ylabel("Number of Rides")

plt.grid(True)
plt.tight_layout()
plt.show()


# Close database connection
conn.close()

print("Dashboard generated successfully!")

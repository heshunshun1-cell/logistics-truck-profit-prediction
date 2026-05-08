import pandas as pd
import matplotlib.pyplot as plt
import os

# Create visuals folder if it does not exist
os.makedirs("visuals", exist_ok=True)

# Read data
df = pd.read_csv("data/truck_operations_processed.csv")

# Convert trip_date to datetime
df["trip_date"] = pd.to_datetime(df["trip_date"])

# Calculate business metrics
df["total_cost"] = (
    df["fuel_cost"]
    + df["maintenance_cost"]
    + df["toll_cost"]
    + df["other_cost"]
)

df["profit"] = df["revenue"] - df["total_cost"]
df["cost_per_km"] = df["total_cost"] / df["distance_km"]
df["profit_per_km"] = df["profit"] / df["distance_km"]
df["profit_margin"] = df["profit"] / df["revenue"]

# Show first rows
print("=== First 5 Rows ===")
print(df.head())

print("\n=== Basic Summary ===")
print(df[["revenue", "total_cost", "profit", "cost_per_km", "profit_margin"]].describe())

# Analysis 1: Profit by route
route_profit = df.groupby("route")["profit"].sum().sort_values(ascending=False)

print("\n=== Profit by Route ===")
print(route_profit)

# Analysis 2: Average cost per km by fuel type
fuel_cost = df.groupby("fuel_type")["cost_per_km"].mean()

print("\n=== Average Cost per KM by Fuel Type ===")
print(fuel_cost)

# Analysis 3: Profit by truck
truck_profit = df.groupby("truck_id")["profit"].sum().sort_values(ascending=False)

print("\n=== Profit by Truck ===")
print(truck_profit)

# Chart 1: Profit by route
plt.figure(figsize=(10, 6))
route_profit.plot(kind="bar")
plt.title("Total Profit by Route")
plt.xlabel("Route")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/profit_by_route.png")
plt.show()

# Chart 2: Average cost per km by fuel type
plt.figure(figsize=(6, 5))
fuel_cost.plot(kind="bar")
plt.title("Average Cost per KM by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Cost per KM")
plt.tight_layout()
plt.savefig("visuals/cost_per_km_by_fuel_type.png")
plt.show()

# Chart 3: Profit by truck
plt.figure(figsize=(8, 5))
truck_profit.plot(kind="bar")
plt.title("Total Profit by Truck")
plt.xlabel("Truck ID")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/profit_by_truck.png")
plt.show()
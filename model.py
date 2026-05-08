import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Read data
df = pd.read_csv("data/truck_operations_processed.csv")

# Convert date
df["trip_date"] = pd.to_datetime(df["trip_date"])
df["month"] = df["trip_date"].dt.month

# Calculate cost and profit
df["total_cost"] = (
    df["fuel_cost"]
    + df["maintenance_cost"]
    + df["toll_cost"]
    + df["other_cost"]
)

df["profit"] = df["revenue"] - df["total_cost"]

# Select features that are available before the trip
features = [
    "distance_km",
    "month",
    "truck_type",
    "fuel_type",
    "route"
]

X = df[features]
y = df["profit"]

# Convert categorical variables into numbers
X = pd.get_dummies(X, columns=["truck_type", "fuel_type", "route"], drop_first=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Build model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("=== Improved Model Results ===")
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

# Show actual vs predicted
result = pd.DataFrame({
    "Actual Profit": y_test,
    "Predicted Profit": y_pred
})

print("\n=== Actual vs Predicted Profit ===")
print(result)
import numpy as np
import pandas as pd

# Reproducibility
np.random.seed(42)

# Number of days (2 years)
n_days = 365 * 2

# Date range
dates = pd.date_range(start="2023-01-01", periods=n_days, freq="D")

# Trend: upward then downward
trend_up = np.linspace(50, 200, n_days // 2)
trend_down = np.linspace(200, 120, n_days - len(trend_up))
trend = np.concatenate([trend_up, trend_down])

# Weekly seasonality
weekly = 10 * np.sin(2 * np.pi * dates.dayofweek.to_numpy() / 7)

# Random noise
noise_cases = np.random.normal(0, 8, size=n_days)
noise_symptoms = np.random.normal(0, 0.05, size=n_days)
noise_testing = np.random.normal(0, 50, size=n_days)

# Generate signals
reported_cases = trend + weekly + noise_cases
symptom_rate = 0.3 + (trend / 1000) + weekly / 500 + noise_symptoms
testing_volume = 1000 + trend * 3 + weekly * 5 + noise_testing

# Assemble DataFrame
df = pd.DataFrame({
    "date": dates,
    "reported_cases": reported_cases.round().astype(float),
    "symptom_rate": np.clip(symptom_rate, 0, 1),
    "testing_volume": testing_volume.round().astype(float)
})

# Introduce missing values (10–15%)
for col in ["reported_cases", "symptom_rate", "testing_volume"]:
    miss_rate = np.random.uniform(0.10, 0.15)
    mask = np.random.rand(n_days) < miss_rate
    df.loc[mask, col] = np.nan

# Save to CSV
df.to_csv("synthetic_outbreak.csv", index=False)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuration
start_year = 2004
end_year = 2024
years = np.arange(start_year, end_year + 1)

# Linear weight: from 0.1 to 1.0
linear_weights = np.linspace(0.1, 1.0, len(years))

# Exponential weight: e^(0.1 * (year - start_year)), normalized to max = 1
decay_rate = 0.1
exp_weights = np.exp(decay_rate * (years - start_year))
exp_weights = exp_weights / np.max(exp_weights)  # normalize to 0–1

# Create DataFrame
weights_df = pd.DataFrame({
    'Year': years,
    'Linear_Weight': linear_weights,
    'Exponential_Weight': exp_weights
})

# Save to CSV
weights_df.to_csv('Allegheny County Crash Data/3 Time Series Crash Map/year_weight_models.csv', index=False)

# Print model equations
print("\nWeight Model Equations:")
print("Linear Model: y = {:.4f} * x + {:.4f}".format(
    (linear_weights[-1] - linear_weights[0]) / (years[-1] - years[0]),
    linear_weights[0] - ((linear_weights[-1] - linear_weights[0]) / (years[-1] - years[0])) * years[0]
))
print("Exponential Model: y = e^({:.2f} * (x - {})) normalized to max=1".format(decay_rate, start_year))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(years, linear_weights, label='Linear Weight')
plt.plot(years, exp_weights, label='Exponential Weight')
plt.title('Yearly Weight Models (2004-2024)')
plt.xlabel('Year')
plt.ylabel('Weight')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

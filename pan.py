import pandas as pd
import os

# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Account Number": [123456, 234567, 345678],
    "Balance": [5000.0, 3000.5, 1500.75]
}

# Create DataFrame
df = pd.DataFrame(data)

# Define directory and file path
directory = "bank_data"
filename = "bank_accounts.csv"
filepath = os.path.join(directory, filename)

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Save DataFrame to CSV
df.to_csv(filepath, index=False)

print(f"CSV file saved successfully at: {filepath}")

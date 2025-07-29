import pandas as pd
import os

# Path to the CSV
directory = "bank_data"
filename = "bank_accounts.csv"
filepath = os.path.join(directory, filename)

# Load existing data
if os.path.exists(filepath):
    df = pd.read_csv(filepath)
else:
    df = pd.DataFrame(columns=["Name", "Account Number", "Balance"])

# New row data
new_row = {
    "Name": "David",
    "Account Number": 456789,
    "Balance": 4200.0
}

# Append new row to DataFrame
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Save updated DataFrame back to CSV
df.to_csv(filepath, index=False)

print(f"New row added and CSV updated at: {filepath}")

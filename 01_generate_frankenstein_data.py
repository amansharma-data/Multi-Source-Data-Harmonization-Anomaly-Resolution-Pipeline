import pandas as pd
import numpy as np
import json
import random
import os

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Creating a data folder
OUTPUT_DIR = os.path.join("DATA", "RAW")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---DATASET SIZE---
NUM_NOIDA_ROWS = 100000
NUM_MOHALI_ROWS = 250000

print(f"Generating Noida Office Dataset ({NUM_NOIDA_ROWS} rows)... This might take a moment.")
# --- DATASET 1: Noida Office ---
noida_data = []
for i in range(1, NUM_NOIDA_ROWS + 1):
    location_json = json.dumps({
        "city": random.choice(["Noida", "New Delhi", "Gurugram", None]),
        "zip": random.choice(["201301", "110001", "122018", "N/A"])
    })

    # Create text column with hidden emails and phone numbers
    if random.random() > 0.3:
        email = f"contact{i}@example.com"
        phone = f"+91-{random.randint(9000000000, 9999999999)}"
        notes = f"Spoke with the client today. Reach them at {email} or call {phone} for updates."
    else:
        notes = "Left a voicemail. Will try again next week."

    noida_data.append({
        "client_id": f"ND-{1000 + i}",
        "client_details": location_json,
        "contact_notes": notes,
        "monthly_sales_inr": np.random.normal(50000, 15000) if random.random() > 0.1 else np.nan  # 10% missing values
    })

df_noida = pd.DataFrame(noida_data)
df_noida.to_csv(os.path.join(OUTPUT_DIR, "noida_clients.csv"), index=False)
print(f"-> Saved noida_clients.csv ({len(df_noida)} rows)")

print(f"\nGenerating Mohali Office Dataset ({NUM_MOHALI_ROWS} rows)... This might take a moment.")
# --- DATASET 2: Mohali Office (Fuzzy matching & Statistical outliers) ---
mohali_data = []
companies = ["HCLTech", "TCS", "Infosys", "Wipro"]
misspellings = {
    "HCLTech": ["HCL Technologies", "hcl tech ltd", "HCL-Tech", "hcl"],
    "TCS": ["Tata Consultancy Services", "tcs ltd", "Tata Consult"],
    "Infosys": ["Infy", "infosys limited", "info-sys"],
    "Wipro": ["Wipro Ltd", "wipro technologies", "WIPRO"]
}

for i in range(1, NUM_MOHALI_ROWS + 1):
    base_company = random.choice(companies)
    # 40% chance to misspell the company name
    if random.random() > 0.6:
        company_name = random.choice(misspellings[base_company])
    else:
        company_name = base_company

    # Generate revenue with massive currency/typographical outliers
    revenue = np.random.normal(600, 200)  # Assuming USD
    if random.random() > 0.95:
        revenue = revenue * 10000  # Massive outlier (e.g., entered INR instead of USD)

    # Generate age with impossible outliers
    account_age = random.randint(1, 15)
    if random.random() > 0.98:
        account_age = random.randint(200, 500)  # Impossible age

    mohali_data.append({
        "AccountID": f"MH-{5000 + i}",  # Mismatched ID column name
        "Company": company_name,
        "Revenue_USD": revenue if random.random() > 0.05 else np.nan,  # 5% missing
        "Age_of_Account_Years": account_age
    })

df_mohali = pd.DataFrame(mohali_data)
df_mohali.to_csv(os.path.join(OUTPUT_DIR, "mohali_accounts.csv"), index=False)
print(f"-> Saved mohali_accounts.csv ({len(df_mohali)} rows)")

print(f"\nDone! Successfully generated large datasets in the {OUTPUT_DIR} folder.")
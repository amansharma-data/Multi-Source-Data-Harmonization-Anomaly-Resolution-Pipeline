# Multi-Source Enterprise Data Harmonization & ETL Pipeline

An automated ETL (Extract, Transform, Load) workflow built in Python to ingest, clean, and harmonize 350,000 synthetic enterprise records originating from disparate regional datasets. This project transforms messy, semi-structured, and highly anomalous raw data into a clean, normalized relational schema ready for downstream business intelligence.

## 🚀 Key Features

* **Semi-Structured Data Parsing:** Unpacks nested JSON objects within tabular columns to extract structured location and demographic data.
* **Regex Entity Extraction:** Utilizes Regular Expressions (RegEx) to mine embedded email addresses and phone numbers hidden within unstructured contact notes.
* **Fuzzy String Matching:** Standardizes highly inconsistent categorical data (e.g., typos in enterprise names like "hcl tech ltd" vs. "HCLTech") using token-based fuzzy string matching (`thefuzz`) with a 75% similarity threshold and dictionary alias mapping.
* **Statistical Outlier Handling:** Applies median imputation for missing revenue values and utilizes Interquartile Range (IQR) bounds to cap extreme typographical outliers (e.g., impossible account ages or mismatched currency multipliers).
* **Schema Harmonization:** Aligns completely disparate table schemas (Noida vs. Mohali) and vertically concatenates the sanitized data into a single, normalized 10-column master dataset.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Text Processing:** `re` (Regular Expressions), `thefuzz` (Fuzzy String Matching), `json`
* **Environment:** Jupyter Notebook

## 📂 Project Structure

```text
├── DATA/
│   └── RAW/
│       ├── noida_clients.csv          # Raw dataset 1 (Contains nested JSON & text blobs)
│       └── mohali_accounts.csv        # Raw dataset 2 (Contains extreme outliers & typos)
├── 01_generate_frankenstein_data.py   # Script to generate the synthetic messy datasets
├── 02_data_cleaning.ipynb             # Core ETL pipeline and harmonization logic
├── noida_cleaned.csv                  # Intermediate cleaned dataset 1
├── mohali_cleaned.csv                 # Intermediate cleaned dataset 2
├── harmonized_master_companies.csv    # Final 10-column normalized master dataset
└── README.md
```

## ⚙️ How to Run Locally

**1. Clone the repository and install dependencies:**
Ensure you have Python installed, then install the required libraries:
```bash
pip install pandas numpy thefuzz
```

**2. Generate the Raw Data:**
Run the data generation script to create the `DATA/RAW/` folder with 350,000 rows of messy, anomalous data.
```bash
python 01_generate_frankenstein_data.py
```

**3. Execute the ETL Pipeline:**
Open the Jupyter Notebook and run all cells to execute the data harmonization process.
```bash
jupyter notebook 02_data_cleaning.ipynb
```

## 📊 Pipeline Results

The final output is a strictly typed, normalized CSV file (`harmonized_master_companies.csv`) containing 350,000 rows and 10 standardized columns:
`Account_ID` | `Region` | `Company` | `Revenue_USD` | `Revenue_INR` | `Age_of_Account_Years` | `City` | `Zip` | `Email` | `Phone`
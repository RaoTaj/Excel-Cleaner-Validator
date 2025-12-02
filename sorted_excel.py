import pandas as pd 
import re
# === File Paths ===
input_file = "" # Put Excel File Name 
output_csv = "" # Only required name of file which want as output in csv
output_xlsx = "" # Same as above but in xlsx this file will be sorted.
error_xlsx = "" # error data will be extract into this file 
duplicates_xlsx = "" # If duplicate rows found then will be extracted to this file 
# === Regex Patterns ===
mobile_pattern = re.compile(r"^03\d{9}$")  # Must start with 03 and be 11 digits
cnic_pattern = re.compile(r"^\d{5}-?\d{7}-?\d{1}$")
print(":inbox_tray: Reading Excel file...")
df = pd.read_excel(input_file, dtype=str)
df = df.fillna("").applymap(str.strip)
print(f":white_check_mark: Loaded {len(df):,} rows from Excel")
# === Step :one: — Fix mobile numbers (ensure leading 0) ===
df["Mobile Number"] = df["Mobile Number"].apply(lambda x: x if x.startswith("0") else "0" + x)
# === Step :two: — Validate Mobile & CNIC ===
print(":mag_right: Validating Mobile Number & CNIC...")
valid_mask = df["Mobile Number"].apply(lambda x: bool(mobile_pattern.match(x))) & \
             df["Cnic"].apply(lambda x: bool(cnic_pattern.match(x)))
valid_df = df[valid_mask].copy()
error_df = df[~valid_mask].copy()
print(f":x: Invalid/Formatting Errors: {len(error_df):,} rows")
if not error_df.empty:
    print(error_df[["Mobile Number", "Cnic"]].head(10))  # show sample
    error_df.to_excel(error_xlsx, index=False)
    print(f":file_folder: Invalid data saved to: {error_xlsx}")
# === Step :three: — Remove Duplicates ===
print(":broom: Checking duplicates...")
duplicates_df = valid_df[valid_df.duplicated(subset=["Mobile Number", "Cnic"], keep=False)]
unique_df = valid_df.drop_duplicates(subset=["Mobile Number", "Cnic"], keep="first")
print(f":repeat: Found {len(duplicates_df):,} duplicate rows")
if not duplicates_df.empty:
    print(duplicates_df[["Mobile Number", "Cnic"]].head(10))  # show sample
    duplicates_df.to_excel(duplicates_xlsx, index=False)
    print(f":file_folder: Duplicate data saved to: {duplicates_xlsx}")
# === Step :four: — Sort Data ===
sorted_df = unique_df.sort_values(by=["Mobile Number", "Cnic"])
# === Step :five: — Save CSV (for backend use) ===
# Add a quote before mobile numbers to preserve leading zero in Excel view
csv_df = sorted_df.copy()
csv_df["Mobile Number"] = "'" + csv_df["Mobile Number"]
csv_df.to_csv(output_csv, index=False, encoding="utf-8-sig")
# === Step :six: — Save Excel (for review) ===
sorted_df.to_excel(output_xlsx, index=False)
print(":white_check_mark: Cleaned and sorted files saved successfully!")
print(f":file_folder: CSV: {output_csv}")
print(f":file_folder: Excel: {output_xlsx}")
print(f":bar_chart: Total valid rows: {len(valid_df):,}")
print(f":bar_chart: Total unique rows (final): {len(unique_df):,}")
print(f":warning: Invalid rows: {len(error_df):,}")
print(f":repeat: Duplicate rows: {len(duplicates_df):,}")
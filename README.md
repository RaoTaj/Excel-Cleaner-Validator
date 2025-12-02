🧩 Technologies Used
1. Python
2. Pandas
3. Regex (re)
4. Excel & CSV processing

🛠️ Script Workflow

1. Read Excel file
2. Trim + normalize all fields
3. Auo-fix mobile format
4. Validate Mobile & CNIC
5. Extract invalid rows
6. Find duplicates
7. Sort final dataset
8. Export all files (CSV + Excel)

💡 Real Use-Case Example (Banking Scenario)

Example:
A bank wants to send notifications to customers who are using an older version of their mobile banking app.
The bank exports a customer list from their system, but the data often contains:

1. Wrong mobile numbers

2. Invalid or incorrectly formatted CNICs

3. Duplicate entries

4. Blank or missing values

5. Extra spaces or text formatting issues

By running this script:

The exported Excel file is loaded
  Mobile numbers and CNICs are validated and auto-corrected
  Invalid or missing values are removed and saved separately
  Duplicates are detected and extracted
  A new clean and sorted file is created

💡The bank can safely send notifications only to valid, unique, registered customers

This ensures accuracy, prevents sending messages to wrong numbers, and reduces SMS/API costs.

🚀 Features
✔ 1. Automatic Data Cleaning & Normalization

Trims whitespace

Converts all values to strings

Ensures consistent formatting

✔ 2. Mobile Number Auto-Correction

Ensures mobile numbers start with 0

Validates Pakistani mobile format: 03XXXXXXXXX

✔ 3. CNIC Validation

Supports formats:

12345-1234567-1

1234512345671

✔ 4. Error Detection & Export

Invalid rows due to mobile or CNIC mismatch are moved to an error Excel file.

✔ 5. Duplicate Detection

Duplicates based on both Mobile Number + CNIC are extracted into a separate file.

✔ 6. Clean Output for Backend / Campaign Use

Final CSV file optimized for backend imports

Clean Excel file for manual review

Mobile numbers preserved with leading zero in CSV

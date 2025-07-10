# File Integrity Checker

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MONICA REMOLA.K

*INTERN ID*:CT06DF1639

*DOMAIN*:FRONT END DEVELOPMENT

*DURATION*:6 WEEKS

*MENTOR*:NEELA SANTOSH



# File Integrity Checker

## Overview

The File Integrity Checker is a Python-based tool designed to help users monitor and ensure the integrity of files within a specified directory. File integrity is crucial in many scenarios, such as system administration, software development, and data security, where unauthorized or accidental changes to files can lead to data loss, security breaches, or system malfunctions. This script provides a simple yet effective way to detect any changes, additions, or deletions of files by calculating and comparing their cryptographic hash values over time.

## Purpose

The primary purpose of this tool is to provide users with a means to:
- Detect unauthorized or accidental modifications to files.
- Monitor directories for new or deleted files.
- Maintain a record of the original state of files for auditing or backup purposes.

By leveraging cryptographic hash functions (SHA256), the script ensures that even the smallest change in a file will be detected, making it a reliable solution for file integrity monitoring.

## Features

- **Recursive Directory Scanning:** Scans all files in the specified folder and its subfolders.
- **SHA256 Hash Calculation:** Uses the secure SHA256 algorithm to generate unique hash values for each file.
- **Baseline Hash Storage:** Saves the initial state of all file hashes in a `hashes.json` file.
- **Change Detection:** On subsequent runs, compares current file hashes to the baseline and reports any added, deleted, or modified files.
- **User-Friendly Output:** Clearly lists all detected changes in the terminal for easy review.

## How It Works

1. **Initial Run:**
   - The script scans the specified directory, calculates the SHA256 hash for each file, and saves these hashes in `hashes.json` as a baseline.
2. **Subsequent Runs:**
   - The script rescans the directory, recalculates hashes, and compares them to the baseline.
   - It reports any files that have been added, deleted, or modified since the last run.
   - The baseline is then updated to reflect the current state.

## Usage Instructions

1. Ensure you have Python 3 installed on your system.
2. Place `file_integrity_checker.py` in the directory you want to monitor, or anywhere on your system.
3. Open a terminal and navigate to the script's directory.
4. Run the script with:
   ```
   python file_integrity_checker.py
   ```
5. When prompted, enter the path to the folder you wish to monitor (e.g., `.` for the current directory).
6. Review the output for any reported changes.

## Example Output

```
Enter the folder path to check: .
Scanning files...
Added files:
  + testfile.txt
Modified files:
  * file_integrity_checker.py
Deleted files:
  - oldfile.txt
```

## Technical Details

- **Hashing Algorithm:** The script uses Python's built-in `hashlib` library with the SHA256 algorithm for strong, collision-resistant hashing.
- **Data Storage:** File hashes are stored in a JSON file (`hashes.json`) for easy reading and updating.
- **Cross-Platform:** The script works on Windows, macOS, and Linux systems.
- **Extensibility:** The script can be easily modified to ignore certain files (such as `hashes.json` itself) or to support other hash algorithms if needed.

## Notes

- The script will also detect changes to `hashes.json` itself. You can modify the script to ignore this file if desired.
- Make sure to run the script from the same directory or provide the correct path to ensure accurate monitoring.
- Regularly running the script helps maintain up-to-date integrity records.



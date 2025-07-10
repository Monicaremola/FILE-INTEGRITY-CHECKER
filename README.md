# File Integrity Checker

This Python script monitors changes in files within a specified folder by calculating and comparing SHA256 hash values. It helps ensure file integrity by detecting added, modified, or deleted files.

## Features

- Scans all files in a folder (including subfolders)
- Calculates SHA256 hashes for each file
- Stores baseline hashes in `hashes.json`
- Reports added, deleted, or modified files on subsequent runs

## How to Use

1. **Run the script:**
   ```
   python file_integrity_checker.py
   ```

2. **Enter the folder path** you want to monitor (e.g., `.` for the current folder).

3. **First run:**  
   - The script saves the current state as a baseline in `hashes.json`.

4. **Subsequent runs:**  
   - The script compares the current state to the baseline and reports any changes.

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

## Notes

- The script will also detect changes to `hashes.json` itself. You can modify the script to ignore this file if desired.
- Make sure you have Python 3 installed.

## Author

Your Name 
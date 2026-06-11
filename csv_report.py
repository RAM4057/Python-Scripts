#!/usr/bin/env python3
import os
import sys
import csv
import glob

def get_csv_report(csv_file):
    """Generate a report for a CSV file."""
    if not os.path.exists(csv_file):
        print(f"Error: File '{csv_file}' not found.")
        return
    
    # Get full path
    full_path = os.path.abspath(csv_file)
    
    # Get file size in bytes
    file_size = os.path.getsize(csv_file)
    
    # Read CSV file
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            
            # Get headers (first row)
            try:
                headers = next(csv_reader)
            except StopIteration:
                headers = []
            
            # Count rows (excluding header)
            row_count = sum(1 for row in csv_reader)
            
            # Count columns (from headers)
            col_count = len(headers)
        
        # Generate report
        print("CSV File Report")
        print("=" * 40)
        print(f"Full path: {full_path}")
        print(f"Filesize (bytes): {file_size}")
        print(f"# of cols: {col_count}")
        print(f"# of rows: {row_count}")
        print(f"Headers: {headers}")
        
    except Exception as e:
        print(f"Error reading CSV file: {e}")

def main():
    if len(sys.argv) > 1:
        # Use the file provided as argument
        csv_file = sys.argv[1]
        get_csv_report(csv_file)
    else:
        # Look for CSV files in current directory
        csv_files = glob.glob("*.csv")
        
        if not csv_files:
            print("No CSV files found in the current directory.")
            print("Usage: python csv_report.py <csv_file>")
            return
        
        if len(csv_files) == 1:
            # Only one CSV file, use it
            csv_file = csv_files[0]
            print(f"Using CSV file: {csv_file}")
            get_csv_report(csv_file)
        else:
            # Multiple CSV files, ask user to choose
            print("Multiple CSV files found:")
            for i, file in enumerate(csv_files, 1):
                print(f"  {i}. {file}")
            print("\nPlease specify which file to analyze:")
            print(f"Usage: python csv_report.py <csv_file>")
            print(f"Available files: {', '.join(csv_files)}")

if __name__ == "__main__":
    main()

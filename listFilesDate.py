import os
import datetime

def list_files_older_than(root_dir, cutoff_date):
    """List full paths of all files older than cutoff_date (YYYY-MM-DD)"""
    cutoff = datetime.datetime.strptime(cutoff_date, "%Y-%m-%d").timestamp()
    
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                if os.path.getmtime(filepath) < cutoff:
                    print(filepath)
            except (PermissionError, OSError):
                continue  # Skip files with access issues

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python listFilesDate.py YYYY-MM-DD")
        sys.exit(1)
    
    # Windows: Use "C:\\" | Linux/macOS: Use "/"
    root_directory = "C:\\" if os.name == "nt" else "/"
    
    print(f"[*] Scanning ALL files in {root_directory} older than {sys.argv[1]}...")
    list_files_older_than(root_directory, sys.argv[1])
# Old Files Viewer

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)

A simple yet powerful command-line utility to find and list files on your system that were last modified before a specific date.


## Motivation

Over time, computer systems accumulate countless files. Many of these become obsolete, but finding them can be a challenge. This script was created to address this problem by providing a straightforward way to recursively scan a directory (or an entire drive) and identify all files older than a specified date. It's a useful first step for anyone looking to perform a manual review and cleanup of old data to free up disk space.

---

## Key Features

-   **Recursive Search**: Scans every subdirectory within the specified starting path using `os.walk`.
-   **Date-Based Filtering**: Lists only the files whose last modification date is older than the provided cutoff date.
-   **Cross-Platform**: Automatically detects the OS (Windows, Linux, macOS) to scan the entire root drive by default.
-   **Robust Error Handling**: Gracefully skips files that cannot be accessed due to permission errors, preventing the script from crashing during a long scan.
-   **Simple Command-Line Interface**: Easy to use with a single command and one argument.
-   **Zero Dependencies**: Runs using only Python's standard libraries, so no `pip install` is needed.

---

## Requirements

-   **Python 3.6** or newer.

---

## Installation

No special installation is required. Just clone the repository or download the `listFilesDate.py` script.

```bash
git clone https://github.com/jaikumar-kpv/Old-Files-Viewer.git
cd Old-Files-Viewer


# Folder-synchronization-program

## Table of Contents
- [Overview](#overview)
- [Usage](#usage)
- [Configuration](#configuration)
- [File Comparison](#file-comparison)
- [Logging](#logging)
  
## Overview
The provided Python script is a file synchronization program that continuously monitors a source directory and synchronizes any changes (additions, modifications, or deletions) to a replica directory. It uses a simple hash-based file comparison to determine if a file needs synchronization.
The program runs in an infinite loop with a specified time interval, allowing it to react promptly to changes in the source directory. It logs all synchronization activities to a specified log file.

## Usage

To use the synchronization program, follow these steps:

1. **Clone or Download the Script:** Clone this repository or download the Python script to your local machine.

2. **Requirements:** Ensure you have Python 3.x installed on your system.

3. **Configuration (Optional):** You can configure the source directory, replica directory, log file path, and synchronization time interval by using command-line arguments (see [Configuration](#configuration)).

4. **Run the Script:** Open your terminal or command prompt and run the script using the following command:
   ```bash
   python main.py
  
## Configuration

The synchronization program can be configured using command-line arguments. Here are the available configuration options:

- `--source`: Specify the source folder path (default: "source"). This is the directory that will be monitored for changes.

- `--replica`: Specify the replica folder path (default: "replica"). This is the directory where changes from the source directory will be synchronized.

- `--log-file`: Specify the log file path (default: "log.txt"). All synchronization activities will be logged to this file.

- `--time-interval`: Specify the time interval in seconds for checking changes (default: 10 seconds). You can adjust this interval based on how frequently you want the program to check for changes.


You can override the default settings by providing these arguments when running the script. For example:

```bash
python main.py --source source --replica replica --log-file log.txt --time-interval 30
```
## File Comparison

The synchronization program uses MD5 hashing to compare files between the source and replica directories. When the program detects a change in the source directory, it performs the following steps for file comparison:

1. Calculate the MD5 hash of the file in the source directory.

2. Calculate the MD5 hash of the corresponding file in the replica directory (if it exists).

3. Compare the two MD5 hashes. If they match, it means the files are identical, and no further action is taken.

4. If the MD5 hashes do not match, the program replaces the replica file with the source file to ensure synchronization.

This file comparison method ensures that only changed or modified files are synchronized between the directories.

## Logging

All synchronization activities are logged to a specified log file in a structured format. Here's what you can expect in the log file:

- `<timestamp>`: This is the date and time when the activity occurred. It helps you track when each synchronization action took place.

- `[INFO]`: This log level indicates normal synchronization activities. It's followed by a colon and space.

- `<message>`: Describes the synchronization activity that took place. For example:
    - `[INFO]: File example.txt has been copied.` - Indicates a successful file copy.

You can configure the log file path using the `--log-file` command-line argument. By examining the log file, you can keep track of all synchronization activities and troubleshoot any issues that may arise during the process.



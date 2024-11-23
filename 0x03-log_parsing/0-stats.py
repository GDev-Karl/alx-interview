#!/usr/bin/python3
"""Log parsing script that reads stdin line by line and computes metrics."""

import sys

# Initialize metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
valid_codes = set(status_codes.keys())

def print_stats():
    """Print the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

try:
    line_count = 0

    for line in sys.stdin:
        try:
            # Split the line and parse it
            parts = line.split()
            if len(parts) < 7:
                continue  # Skip malformed lines
            
            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update metrics
            total_size += file_size
            if status_code in valid_codes:
                status_codes[status_code] += 1

        except (ValueError, IndexError):
            # Skip lines with parsing errors
            continue

        line_count += 1

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats on keyboard interruption
    print_stats()
    raise
else:
    # Print stats when EOF is reached
    print_stats()

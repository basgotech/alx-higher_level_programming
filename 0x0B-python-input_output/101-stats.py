#!/usr/bin/python3
import sys
import signal

def print_metrics(stats):
    """Prints the computed metrics.

    Args:
        stats (dict): A dictionary containing metrics.
    """
    print("Total file size: {}".format(stats['total_size']))
    for status_code in sorted(stats['status_codes']):
        print("{}: {}".format(status_code, stats['status_codes'][status_code]))

def process_line(line, stats):
    """Processes a line and updates the metrics.

    Args:
        line (str): The input line.
        stats (dict): A dictionary containing metrics.
    """
    try:
        _, _, _, status_code, file_size = line.split(" ")[-5:]
        file_size = int(file_size)
        status_code = int(status_code)

        stats['total_size'] += file_size
        stats['lines_count'] += 1

        if status_code in stats['status_codes']:
            stats['status_codes'][status_code] += 1
        else:
            stats['status_codes'][status_code] = 1

    except ValueError:
        pass  # Ignore lines that don't match the expected format

def main():
    stats = {
        'total_size': 0,
        'lines_count': 0,
        'status_codes': {}
    }

    try:
        for line in sys.stdin:
            process_line(line, stats)
            if stats['lines_count'] % 10 == 0:
                print_metrics(stats)

    except KeyboardInterrupt:
        print_metrics(stats)

if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_metrics(total_size, status_codes_count):
    """Print accumulated metrics.

    Args:
        total_size (int): The accumulated read file size.
        status_codes_count (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes_count.items()):
        print("{}: {}".format(code, count))


if __name__ == "__main__":
    import sys

    total_size = 0
    status_codes_count = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_metrics(total_size, status_codes_count)
                line_count = 1
            else:
                line_count += 1

            line_parts = line.split()

            try:
                total_size += int(line_parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line_parts[-2] in valid_codes:
                    status_code = line_parts[-2]
                    status_codes_count[status_code] = status_codes_count.get(status_code, 0) + 1
            except IndexError:
                pass

        print_metrics(total_size, status_codes_count)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes_count)
        raise

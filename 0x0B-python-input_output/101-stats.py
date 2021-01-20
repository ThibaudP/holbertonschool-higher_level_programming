#!/usr/bin/python3
"""101-stats module"""
import sys
import signal


def print_stats(file_size, status_codes):
    """prints the stats"""
    print("File size: {:d}".format(file_size))
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print("{:s}: {:d}".format(k, v))


def sigint_handler(sig, frame):
    """calls print_stats when SIGINT is captured"""
    print_stats(file_size, status_codes)

file_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
cnt = 0

for line in sys.stdin:
    print(cnt)
    if cnt > 0 and cnt % 10 == 0:
        print_stats(file_size, status_codes)

    words = line.split()
    file_size += int(words[8])
    status_codes[words[7]] += 1
    cnt += 1

    signal.signal(signal.SIGINT, sigint_handler)

print_stats(file_size, status_codes)

#!/usr/bin/python3
"""101-stats module"""
import sys

file_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
cnt = 0

try:
    for line in sys.stdin:
        words = line.split()
        file_size += int(words[8])
        status_codes[words[7]] += 1
        cnt += 1
        if cnt > 0 and cnt % 10 == 0:
            print("File size: {:d}".format(file_size))
            for k, v in sorted(status_codes.items()):
                if v != 0:
                    print("{:s}: {:d}".format(k, v))

    print("File size: {:d}".format(file_size))
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print("{:s}: {:d}".format(k, v))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print("{:s}: {:d}".format(k, v))

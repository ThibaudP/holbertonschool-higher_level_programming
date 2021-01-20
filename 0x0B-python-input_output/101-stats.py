#!/usr/bin/python3
"""101-stats module"""
import sys


def print_stats(file_size, status_codes):
    """prints the stats"""
    print("File size: {:d}".format(file_size))
    for k, v in sorted(status_codes.items()):
        if v:
            print("{:s}: {:d}".format(k, v))

file_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
cnt = 0

try:
    for line in sys.stdin:
        words = line.split()
        if len(words) == 9:
            chk = cnt
            if words[-2] in status_codes:
                status_codes[words[-2]] += 1
                cnt += 1
            try:
                file_size += int(words[-1])
                if chk == cnt:
                    cnt += 1
            except:
                if chk == cnt:
                    continue
        if cnt % 10 == 0:
            print_stats(file_size, status_codes)

    print_stats(file_size, status_codes)

except KeyboardInterrupt:
    print_stats(file_size, status_codes)

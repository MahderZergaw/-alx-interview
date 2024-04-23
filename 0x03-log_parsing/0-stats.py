#!/usr/bin/python3
""" Reads stdin line by line and computes metrics"""

import sys


def printstats_code(dic, size):
    """ Prints file size and status codes """
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            printstats_code(status_codes, size)

        split_list = line.split()
        count += 1

        try:
            size += int(split_list[-1])
        except ValueError:
            pass

        try:
            if split_list[-2] in status_codes:
                status_codes[split_list[-2]] += 1
        except IndexError:
            pass
    printstats_code(status_codes, size)


except KeyboardInterrupt:
    printstats_code(status_codes, size)
    raise

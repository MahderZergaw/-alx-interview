#!/usr/bin/python3

import sys


def print_msg(dict_sc, total_file_size):
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
code = 0
counter = 0
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # Split the input line by whitespace
        # Check if there are enough elements in the parsed line
        if len(parsed_line) >= 10:
            counter += 1

            # Extract file size and status code from the parsed line
            file_size = int(parsed_line[-1])  # last element is the file size
            code = parsed_line[-2]  # second to last element is the status code

            # Update total file size
            total_file_size += file_size

            # Update the dictionary with status codes
            dict_sc[code] = dict_sc.get(code, 0) + 1

            # Print stats for every 10 lines
            if counter == 10:
                print_msg(dict_sc, total_file_size)
                counter = 0

finally:
    # Print the final stats at the end of input
    print_msg(dict_sc, total_file_size)

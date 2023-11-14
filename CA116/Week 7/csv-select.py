#!/usr/bin/env python3

import sys

# Part 1:

command_line = sys.argv[1]

find_header = 0

header = field = ""

while command_line[find_header] != "=":
    find_header += 1

header = command_line[:find_header]
field = command_line[find_header + 1:]

# Part 2:

fields = input()

header_pos = 0
left_pos = 0
i = 0

while i < len(fields):

    if fields[i] == ",":

        header_pos += 1

        if fields[left_pos:i] == header:

            i = len(fields) + 1

        left_pos = i + 1

    if i + 1 == len(fields):

        header_pos += 1

        i = len(fields) + 1

    i += 1

# Part 3:

entry = input()

while entry != "end":

    if header_pos == 10:

        if entry[-2:] == field:

            print(entry)

    else:

        i = 0
        left_pos = i
        comma_count = 0

        while i < len(entry):

            if entry[i] == ",":

                comma_count += 1

                if comma_count == header_pos - 1:

                    left_pos = i + 1

                    i = len(entry) + 1

            i += 1

        right_pos = left_pos

        while entry[right_pos] != ",":
            right_pos += 1

        if entry[left_pos:right_pos] == field:
            print(entry)

    entry = input()

#! /usr/bin/env python3


import sys
from gethex import findhex
from id_type import identify_filetype


filepath = sys.argv[1]
file_hex = findhex(filepath)
file_extension = identify_filetype(file_hex)
print(file_extension)
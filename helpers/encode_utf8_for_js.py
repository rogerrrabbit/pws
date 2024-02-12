#!/usr/bin/env python3
# -*- coding: utf-8 -*
##########################################################################
#                                                                        #
#  Copyright (C) INTERSEC SA                                             #
#                                                                        #
#  Should you receive a copy of this source code, you must check you     #
#  have a proper, written authorization of INTERSEC to hold it. If you   #
#  don't have such an authorization, you must DELETE all source code     #
#  files in your possession, and inform INTERSEC of the fact you obtain  #
#  these files. Should you not comply to these terms, you can be         #
#  prosecuted in the extent permitted by applicable law.                 #
#                                                                        #
##########################################################################

"""
This script encodes big UTF-8 characters using '\\u{xxxxx}' format.
Made to fix emojis into the right format for vue3-tutorial (JavaScript).
"""

import argparse

def encode_utf8_for_js(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        encoded_content = ''
        for char in content:
            code = ord(char)

            """
            Fix is needed when a unicode character requires more than 2 Bytes
            (more than 4 hexadecimal glyphs) to be coded.
            """
            if code > 0xFFFF:
                encoded_content += '\\u{%x}' % code
            else:
                encoded_content += char

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(encoded_content)
        print(f"File was successfully encoded to:'{output_file}'")
    except Exception as e:
        print(f"Error while encoding file: {e}")

def main():
    parser = argparse.ArgumentParser(description="Encodes big UTF-8 chars.")
    parser.add_argument('input_file', type=str, help="Source file path.")
    parser.add_argument('output_file', type=str, help="Destination file path.")

    args = parser.parse_args()
    encode_utf8_for_js(args.input_file, args.output_file)

if __name__ == "__main__":
    main()

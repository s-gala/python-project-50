#!/usr/bin/env python3

import argparse

from gendiff.engine import generate_diff


def pars():
    parser = argparse.ArgumentParser(description='Compares two \
    configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return (args)


def main():
    args = pars()
    generate_diff(args.first_file, args.second_file)


if __name__ == "__main__":
    main()

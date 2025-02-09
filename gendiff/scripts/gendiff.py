#!/usr/bin/env python3

import argparse


def pars():
    parser = argparse.ArgumentParser(description='Difference calculator.')
    parser.add_argument(dest = 'first_file')
    parser.add_argument(dest = 'second_file')
    args = parser.parse_args()
    print(args)


def main():
    pars()

if __name__ == "__main__":
    main()

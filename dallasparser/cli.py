#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CLI
---
Command-line script for running TXDallasParser.
"""
from dallasparser.parser import TXDallasParser
import argparse
import sys
import os

def parse_arg():
    """
    Argument parser for CLI usage.
    """
    parser = argparse.ArgumentParser(
        description=(
            'Parse court recoreds from TX Dallas County Felony and Misdemeanor Courts'
        ),
        epilog='nobeedee@gmail.com'
    )
    parser.add_argument(
        '-i',
        '--input',
        help='absolute path of HTML folder',
        type=str,
        required=True
    )
    parser.add_argument(
        '-o',
        '--output',
        help='absolute path of XLSX output files',
        type=str,
        default=os.getcwd()
    )
    return parser.parse_args()

def main():
    """
    Main function to run when parsing using CLI.
    """
    args = parse_arg()
    input = args.input
    output = args.output
    if not input:
        raise Exception('HTML directory path is required.')
    if not output:
        cwd = os.getcwd()
        print('Setting {} as default output path'.format(cwd))
    parser = TXDallasParser(input, output)
    parser.run()
    return

#!/usr/bin/env python

"""clido is a command line interface (CLI) to do list"""

__author__ = "Edward Khou"
__copyright__ = ""
__credits__ = ""
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Edward Khou"
__email__ = "ed@edkhou.com"
__status__ = "prototype"


import argparse
import operator

parser = argparse.ArgumentParser(description="Process some integers. ")
parser.add_argument('integers',
                    metavar='N',
                    type=int,
                    nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum',
                    dest='accumulate',
                    action='store_const',
                    const=sum,
                    default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print args.accumulate(args.integers)

print(1 + 1)

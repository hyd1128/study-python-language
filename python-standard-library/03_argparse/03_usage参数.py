import argparse

# parser = argparse.ArgumentParser(prog='PROG')
# parser.add_argument('--foo', nargs='?', help='foo help')
# parser.add_argument('bar', nargs='+', help='bar help')
# parser.print_help()

"""
usage: PROG [-h] [--foo [FOO]] bar [bar ...]

positional arguments:
  bar          bar help

options:
  -h, --help   show this help message and exit
  --foo [FOO]  foo help
"""

parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
parser.add_argument('--foo', nargs='?', help='foo help')
parser.add_argument('bar', nargs='+', help='bar help')
parser.print_help()

"""
usage: PROG [options]

positional arguments:
  bar          bar help

options:
  -h, --help   show this help message and exit
  --foo [FOO]  foo help
"""
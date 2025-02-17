import argparse

parser = argparse.ArgumentParser(prog="PROG")

parser.add_argument('-f', '--foo')
parser.add_argument('bar')
args = parser.parse_args()
print(args)


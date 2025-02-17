import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', help='foo help')
# args = parser.parse_args()

parser = argparse.ArgumentParser(prog='myprogram')
parser.add_argument('--foo', help='foo of the %(prog)s program')
args = parser.parse_args()
# 和在命令行 --help的作用一致
parser.print_help()

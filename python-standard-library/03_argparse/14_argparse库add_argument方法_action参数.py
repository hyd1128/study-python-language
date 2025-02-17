import argparse

parser = argparse.ArgumentParser(prog="PROG")

# action="store"
# parser.add_argument('--foo', action="store")

# action=“store_const"
# parser.add_argument('--foo', action="store_const", const=43)

# action="store_trur" or action="store_false"
# parser.add_argument('--arg1', action='store_true')
# parser.add_argument('--arg2', action='store_false')

# action="append"
# python 14_argparse库add_argument方法_action参数.py --foo 1 --foo 2 --foo 3
# Namespace(foo=['1', '2', '3'])
# parser.add_argument('--a1', action="append")
# parser.add_argument('--a2', action="append")

# action="extend"
parser.add_argument("--a1", action="extend", nargs="+", type=str)
parser.add_argument("--a2", action="extend", nargs="+", type=str)

args = parser.parse_args()
print(args)


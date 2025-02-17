import argparse
import textwrap

# parser = argparse.ArgumentParser(
#     prog='PROG',
#     description='''this description
#         was indented weird
#             but that is okay''',
#     epilog='''
#             likewise for this epilog whose whitespace will
#         be cleaned up and whose words will be wrapped
#         across a couple lines''')
# parser.print_help()

"""
usage: PROG [-h]

this description was indented weird but that is okay

options:
  -h, --help  show this help message and exit

likewise for this epilog whose whitespace will be cleaned up and whose words
will be wrapped across a couple lines
"""

parser = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
        Please do not mess up this text!
        --------------------------------
            I have indented it
            exactly the way
            I want it
        '''))
parser.print_help()

"""
usage: PROG [-h]

Please do not mess up this text!
--------------------------------
    I have indented it
    exactly the way
    I want it

options:
  -h, --help  show this help message and exit
"""

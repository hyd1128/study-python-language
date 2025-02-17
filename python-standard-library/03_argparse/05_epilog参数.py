import argparse

parser = argparse.ArgumentParser(
    description='A foo that bars')
parser.print_help()
"""
usage: 05_epilog参数.py [-h]

A foo that bars

options:
  -h, --help  show this help message and exit
"""



# parser = argparse.ArgumentParser(
#     description='A foo that bars',
#     epilog="And that's how you'd foo a bar")
# parser.print_help()
"""
usage: 05_epilog参数.py [-h]

A foo that bars

options:
  -h, --help  show this help message and exit

And that's how you'd foo a bar
"""
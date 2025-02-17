import argparse

parser = argparse.ArgumentParser()
parser.print_help()
"""
usage: 04_description参数.py [-h]

options:
  -h, --help  show this help message and exit
"""

# parser = argparse.ArgumentParser(description='A foo that bars')
# parser.print_help()

"""
usage: 04_description参数.py [-h]

A foo that bars

options:
  -h, --help  show this help message and exit

在默认情况下，description 将被换行以便适应给定的空间。如果想改变这种行为
"""






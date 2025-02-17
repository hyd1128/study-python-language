#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import argparse

parser = argparse.ArgumentParser(prog='PROG',  # prog参数
                                 usage='%(prog)s [options]',  # usage参数
                                 description='A foo that bars',  # description参数
                                 epilog="And that's how you'd foo a bar",  # epilog参数
                                 prefix_chars='-+',  # 添加前缀
                                 )

"""
prefix_chars: 
    许多命令行会使用 - 当作前缀，比如 -f/--foo。如果解析器需要支持不同的或者额外的字符，比如像 +f 或者 /foo 的选项，
    可以在参数解析构建器中使用 prefix_chars= 参数。
    prefix_chars= 参数默认使用 '-'。 提供一组不包括 - 的字符将导致 -f/--foo 选项不被允许。
    

"""

# parser.add_argument('--foo', nargs='?', help='foo help')
# parser.add_argument('bar', nargs='+', help='bar help')
parser.add_argument('+f')
parser.add_argument('++bar')
parser.parse_args('+f X ++bar Y'.split())
parser.print_help()

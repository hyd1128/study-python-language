#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import argparse

parser = argparse.ArgumentParser(prog="prompt")

parser.add_argument("--script_content_path", required=True, type=str, metavar="/root/xxx.json")
parser.add_argument("--run_times", required=True, type=int, metavar=1)
parser.add_argument("--device_id", required=True, type=str, metavar="JIANCHENGYUNA")
args = parser.parse_args()
print(f"脚本文件位置: {args.script_content_path}")
print(f"执行次数: {args.run_times}")
print(f"设备id: {args.device_id}")





import argparse
parser = argparse.ArgumentParser(description=" ")

parser.add_argument("--name", help="要问候的人的名字")
parser.add_argument("--age", type=int, help="年龄（可选）")

args = parser.parse_args()

# 使用参数
if args.name:
    print(f"Hello, {args.name}!")
if args.age:
    print(f"You are {args.age} years old.")
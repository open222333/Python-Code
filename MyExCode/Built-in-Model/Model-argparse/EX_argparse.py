import argparse

'''https://docs.python.org/zh-tw/3/library/argparse.html#module-argparse'''
msg = """幫助訊息 

-h test"""

parser = argparse.ArgumentParser(description=msg)

parser.add_argument('-o', '--output', help='show output')
parser.add_argument('-n', '--name', type=str, default='nobady')

# 從命令列讀取參數
args = parser.parse_args()

if args.output:
    print(f'{args.name} 測試輸出訊息 {args.output}')

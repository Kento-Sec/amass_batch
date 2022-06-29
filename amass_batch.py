import argparse
import sys
import os

parser = argparse.ArgumentParser(description="amass_batch.py")
parser.add_argument("-f", "--file", type=str, metavar="file", help="txt目标路径 eg:\"/XX/XX/xx.txt\"")
args = parser.parse_args()

if len(sys.argv) != 3:
    print(
        "[-]  参数错误！\neg1:>>>python amass_batch.py -p txt存放路径 ")

target_file = args.file
open_target = open(target_file)

for line in open_target:
    print(line+"准备扫描=========")
    targeturl = line.strip('\n')
    scan_command = r"./amass enum -active -d {} -o {}.text".format(targeturl,targeturl)
    print(scan_command)
    run = os.system(scan_command)
    print(run)

print("完成！！！！！！！！！！")
open_target.close(target_file)
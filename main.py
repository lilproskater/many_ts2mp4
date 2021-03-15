import re
import os
import subprocess
from sys import argv

if len(argv) != 2:
    exit('Specify .ts chunks folder location')


def tryint(s):
    try:
        return int(s)
    except ValueError:
        return s

def alphanum_key(s):
    return [tryint(c) for c in re.split('([0-9]+)', s)]

def sort_nicely(l):
    return sorted(l, key=alphanum_key)


current_path = os.getcwd()
os.chdir(argv[1])
chunks_folder_path = os.getcwd()
files = os.listdir()
if argv[0] in files:
    files.pop(files.index(argv[0]))
files = sort_nicely(files)
with open('merge.txt', 'w') as f:
    for file in files:
        f.write("file '" + file + "'\n")
subprocess.call('ffmpeg -f concat -i merge.txt -c copy merge.ts', shell=True)
subprocess.call('ffmpeg -i merge.ts -c copy output.mp4', shell=True)
os.remove('./merge.ts')
os.remove('./merge.txt')
os.rename(chunks_folder_path + os.sep + 'output.mp4', current_path + os.sep + 'output.mp4')

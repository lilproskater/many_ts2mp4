# many_ts2mp4
Requirements
Python3 and ffmpeg converter has to be installed on your system

## Usage
```
python3 main.py <filename>
```
filename - path to a folder where your .ts chunks located  

## Notice
1. Order - .ts files are sorted alpha-numericaly.  
2. Your folder should NOT contain merge.ts merge.txt and output.mp4 files.  
3. Final output.mp4 file will appear in the folder where you called a script, so make sure you do NOT already have output.mp4 file there. Otherwise it will be overriden.

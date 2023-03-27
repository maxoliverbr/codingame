import sys
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

mimetype = {}

def is_valid_filename(fn):
    return 0

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    try:
        ext, mt = input().split()
        mimetype[ext.lower()] = mt
    except:
        continue

for i in range(q):
    fname = ""
    ext = ""

    filename = input().lower()
    #print(filename, file=sys.stderr, flush=True)

    if "." not in filename:
        print("UNKNOWN")
    else:
        ext = filename.split(".")[-1]  # One file name per line.
               
        regex = r"^[a-zA-Z0-9]{1,10}$"

        if re.match(regex, ext) and ext.lower() in mimetype:
            print(mimetype[ext])
        else:
            print("UNKNOWN")

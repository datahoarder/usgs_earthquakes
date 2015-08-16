"""
run:
    $ python3 -m scripts.compile.compile_data

Simply concats all files in fetched/ and creates COMPILED_PATH
"""
from scripts.settings import setup_space
from scripts.settings import COMPILED_PATH, FETCHED_DIR
import os.path
from glob import glob

files = glob(os.path.join(FETCHED_DIR, '*.csv'))
with open(COMPILED_PATH, 'w') as o:
    # write headers from the first file
    o.write(open(files[0]).readline())
    for fname in files:
        with open(fname) as f:
            f.readline() # skip first line
            o.write(f.read())

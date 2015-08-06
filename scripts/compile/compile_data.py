"""
run:
    $ python3 -m scripts.compile.compile_data

Simply concats all files in fetched/ and creates compiled/usgs-earthquakes.csv
"""
from scripts.settings import setup_space
from scripts.settings import COMPILED_DIR, FETCHED_DIR
import os.path
from glob import glob

oname = os.path.join(COMPILED_DIR, "usgs-earthquakes.csv")
files = glob(os.path.join(FETCHED_DIR, '*.csv'))
with open(oname, 'w') as o:
    # write headers from the first file
    o.write(open(files[0]).readline())
    for fname in files:
        with open(fname) as f:
            f.readline() # skip first line
            o.write(f.read())

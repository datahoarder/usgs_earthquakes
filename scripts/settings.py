import os

DATA_DIR = "./stash/"
FETCHED_DIR = os.path.join(DATA_DIR, "fetched")
COMPILED_DIR = os.path.join(DATA_DIR, "compiled")
COMPILED_PATH = os.path.join(COMPILED_DIR, "usgs_earthquakes.csv")
BASE_DATA_URL = "http://earthquake.usgs.gov/fdsnws/event/1/query.csv"


def setup_space():
    os.makedirs(FETCHED_DIR, exist_ok = True)
    os.makedirs(COMPILED_DIR, exist_ok = True)

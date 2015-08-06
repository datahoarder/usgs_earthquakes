"""
run:
    $ python3 -m scripts.fetch.fetch_data

Does a month-by-month query of the USGS site for earthquake data
"""
from scripts.settings import setup_space
from scripts.settings import FETCHED_DIR
from scripts.settings import BASE_DATA_URL
import os.path
import requests
from dateutil import rrule
from datetime import datetime, timedelta

START_DATE = datetime(1970, 1, 1)
END_DATE = datetime(2015,8,1) # script will end at the month before

if __name__ == '__main__':
    setup_space()
    timespan = rrule.rrule(rrule.MONTHLY, dtstart = START_DATE, until = END_DATE)
    u_params = {'orderby': 'time-asc'}
    u_params['starttime'] = START_DATE
    for dt in timespan[1:]:
        u_params['endtime'] = dt
        # call the API
        resp = requests.get(BASE_DATA_URL, params = u_params)
        # Save the resulting text
        # as: "2015-05.csv"
        fname = os.path.join(FETCHED_DIR, u_params['starttime'].strftime("%Y-%m.csv"))
        with open(fname, 'w') as f:
            print(fname)
            f.write(resp.text)
        # set the starttime to the next date for the next iteration
        u_params['starttime'] = u_params['endtime']


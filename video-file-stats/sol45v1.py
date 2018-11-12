#!/usr/bin/env python3

import tinytag
import glob
import datetime
import pandas as pd
import sys

if len(sys.argv) < 2:
    print("please provide a directory name")
    sys.exit()

dir_name = sys.argv[1].rstrip('/')
print(f'Looking for "{dir_name}"')
timings = []

for one_filename in glob.glob(f'{dir_name}/*.mp4'):
    t = tinytag.TinyTag.get(one_filename)
    timings.append(t.duration / 60)

s = pd.Series(timings)
print(s.describe())
print(f"Total time is: {datetime.timedelta(minutes=s.sum())}")

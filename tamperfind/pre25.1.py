import sys
import os
import hashlib
from pprint import pprint


pathname = sys.argv[1]
print(f'Searching through {pathname}')

file_info = []
for root, dirs, files in os.walk(pathname):
    for one_filename in files:
        try:
            full_filename = os.path.join(root, one_filename)
            print(full_filename)
            file_info.append({'filename': full_filename,
                              'timestamp': os.stat(full_filename).st_mtime,
                              'sha1': hashlib.sha1(open(full_filename, 'rb').read()).hexdigest()})

        except IOError as e:
            print(f'Error reading {full_filename}: {e}')

pprint(file_info)

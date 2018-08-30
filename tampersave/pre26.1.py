
from pprint import pprint
import os
import sys
import hashlib
import time
import pickle
import operator

filename = 'file_list.pkl'

pathname = sys.argv[1]
print(f"Searching through {pathname}... \n")


class FileInfo(object):
    def __init__(self, filename, mtime, sha1):
        self.filename = filename
        self.mtime = mtime
        self.sha1 = sha1

    def __repr__(self):
        return f"FileInfo for {self.filename}, mtime {self.mtime}, sha1 {self.sha1}"


class FileList(object):
    def __init__(self, pathname):
        self.pathname = pathname
        self.timestamp = time.time()
        self.all_file_infos = [ ]

    def scan(self):

        for root, dirs, files in os.walk(self.pathname):
            for one_filename in files:
                try:
                    full_filename = os.path.join(root, one_filename)

                    self.all_file_infos.append(FileInfo(full_filename,
                                                        os.stat(full_filename).st_mtime,
                                                        hashlib.sha1(open(full_filename, 'rb').read()).hexdigest()))
                except IOError as e:
                    print(f"Error reading {full_filename}: {e}")

    def __repr__(self):
        return '\n'.join('\t' + str(one_file_info)
                                    for one_file_info in self.all_file_infos)

    def rescan(self):
        output = {'added': [],
                  'removed': [],
                  'changed': [],
                  'unchanged': []}

        # Go through the current directory
        for root, dirs, files in os.walk(self.pathname):

            for one_filename in files:
                full_filename = os.path.join(root, one_filename)

                try:
                    file_info = self.file_info_for_filename(full_filename)

                    # Is there a file we've never seen before?  Add to "added"
                    if not file_info:
                        output['added'].append(full_filename)

                    # Is the mtime of the file different?  Add to "changed"
                    elif os.stat(full_filename).st_mtime != file_info.mtime:
                        output['changed'].append(full_filename)

                    # Is the SHA-1 of the file different?  Add to "changed"
                    elif hashlib.sha1(open(full_filename, 'rb').read()).hexdigest() != file_info.sha1:
                        output['changed'].append(full_filename)

                    # Default: Say it's unchanged
                    else:
                        output['unchanged'].append(full_filename)

                except IOError as e:
                    print(f"Error reading {full_filename}: {e}")

            for one_file_info in self.all_file_infos:
                if not os.path.exists(one_file_info.filename):
                    output['removed'].append(one_file_info.filename)

        return output

    def file_info_for_filename(self, filename_to_find):
        for one_file_info in self.all_file_infos:
            if one_file_info.filename == filename_to_find:
                return one_file_info
        return None


fl = FileList(pathname)
fl.scan()
pprint(fl.all_file_infos)

pickle.dump(fl, open(filename, 'wb'))

f2 = pickle.load(open(filename,'rb'))

print(f2, '\n')

pprint(fl.rescan())

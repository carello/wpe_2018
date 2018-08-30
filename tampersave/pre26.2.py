import os
from os.path import join, isfile, isdir
import hashlib
import time
import pickle
import sys
from pprint import pprint

filename = 'file_list.pkl2'
pathname = sys.argv[1]
print(f"Searching through {pathname}... \n")


class FileInfo(object):
    def __init__(self, filepath):
        self.filepath = os.path.abspath(filepath)
        self.timestamp = os.stat(self.filepath).st_mtime
        self.sha1 = self.get_sha1(self.filepath)

    @staticmethod
    def get_sha1(file_name):
        BUFSIZE = 1048576
        sha1 = hashlib.sha1()
        try:
            with open(file_name, 'rb') as f:
                while True:
                    data = f.read(BUFSIZE)
                    if not data:
                        break
                    sha1.update(data)
                return sha1.hexdigest()
        except IOError:
            return None

    def __eq__(self, other):
        return vars(self) == vars(other)

    def __hash__(self):
        return hash(self.filepath)

    def __str__(self):
        return(f'filepath:\t{self.filepath}\n'
               f'timestamp:\t{self.timestamp}\n'
               f'sha1:\t{self.sha1}')

class FileList(object):
    def __init__(self, arg=None):
        if arg is None:
            path = os.path.abspath('.')
        else:
            path = os.path.abspath(arg)
        if isdir(path) and os.access(path, os.R_OK):
            self.files_info = self._get_files_info(path)
            self.timestamp = time.time()
            self.directory = path
        elif isfile(path) and os.access(path, os.R_OK):
            self._load_data(path)
        else:
            raise DirectoryFileError(f'Unable to process: {path}')


    def _get_files_info(self, directory):
        files_info = set()
        for root, dirs, files in os.walk(directory):
            for one_file in files:
                one_file_path = join(root, one_file)
                if isfile(one_file_path):
                    files_info.add(FileInfo(one_file_path))
        return files_info

    def rescan(self):
        new_info = self._get_files_info(self.directory)
        updates = self.files_info.symmetric_difference(new_info)
        added = {item for item in updates if item.filepath not in
                    {item.filepath for item in self.files_info}}
        removed = {item for item in updates if item.filepath not in
                    {item.filepath for item in new_info}}
        changed = updates.difference(added).difference(removed)
        report = {}
        report['added'] = [item.filepath for item in added]
        report['removed'] = [item.filepath for item in removed]
        report['changed'] = list({item.filepath for item in changed})
        self.files_info = new_info
        self.timestamp = time.time()
        return report

    def default_file_name(self):
        return (f'tmp/{os.path.basename(self.directory)}_'
                f'{time.strftime("%d%b%Y_%H%M%S", time.localtime(self.timestamp))}')

    def store(self, out_file=None):
        if out_file is None:
            out_file = self.default_file_name()
        try:
            with open(out_file, 'wb') as outfile:
                pickle.dump(vars(self), outfile, protocol=pickle.HIGHEST_PROTOCOL)
        except(IOError, pickle.PicklingError):
            raise DirectoryFileError(f'Unable to save: {out_file}')

    def _load_data(self, in_file):
        try:
            with open(in_file, 'rb') as infile:
                self.__dict__ = pickle.load(infile)
        except (IOError, AttributeError, pickle.UnpicklingError):
            raise DirectoryFileError(f'Unable to load: {in_file}')


f1 = FileList(pathname)
pickle.dump(f1, open(filename, 'wb'))

f2 = pickle.load(open(filename,'rb'))

print(f2, '\n')

pprint(f1.rescan())

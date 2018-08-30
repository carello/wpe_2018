
import os
import sys
import datetime
import hashlib
import pickle
import collections



class Uniquish(object):
    def __eq__(self, other):
        return vars(self) == vars(other)

    def __hash__(self):
        return hash(pickle.dumps(vars(self)))


class FileList:
    def __init__(self, dirname):
        self.dirname = dirname
        self.fileset = {}
        self.last_scan_time = datetime.datetime.now()
        self.store_fname = 'fdata.dat'

    def rescan(self):
        prev_flist = None
        changes = collections.defaultdict(list)

        if os.path.isfile(self.store_fname):
            prev_flist = self.load()

        self.fileset = {FileInfo(os.path.join(d[0], f)) for d in os.walk(self.dirname) for f in d[2]}

        if prev_flist:
            changes['added'] = list(
                set([fi.fname for fi in self.fileset]) - set([fi.fname for fi in prev_flist.fileset]))
            changes['removed'] = list(
                set([fi.fname for fi in prev_flist.fileset]) - set([fi.fname for fi in self.fileset]))
            changed = list(set([fi for fi in prev_flist.fileset]) ^ set([fi for fi in self.fileset]))
            changes['changed'] = list(set(
                [fi.fname for fi in changed if
                 fi.fname not in changes['removed'] and fi.fname not in changes['added']]))

        self.persist()

        return changes

    def persist(self):
        with open(self.store_fname, 'wb+') as sf:
            pickle.dump(self, sf)

    def load(self):
        with open(self.store_fname, 'rb') as sf:
            return pickle.load(sf)


class FileInfo(Uniquish):
    def __init__(self, filename):
        self.fname = filename
        self.tstamp = datetime.datetime.fromtimestamp(os.path.getctime(filename))
        self.sha_1 = hashlib.sha1(open(filename, 'rb').read()).hexdigest()


class CommandLineArgumentException(Exception):
    pass


if __name__ == '__main__':
    dirname = '.'
    if len(sys.argv) != 2:
        raise CommandLineArgumentException("Need a dir arg!")
    else:
        dirname = sys.argv[1]

    changes = FileList(dirname).rescan()
    print(changes)




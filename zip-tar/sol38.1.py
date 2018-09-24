#!/usr/bin/env python 3

import tarfile
import os.path
import zipfile
from zipfile import ZipFile, ZIP_DEFLATED
import shutil

CRED = '\033[91m'
CEND = '\033[0m'
CWHITE = '\033[37m'
CYELLOW = '\033[33m'
CCYAN = '\033[36m'

z_content = 'zippy/'
dir_tmp = 'tmp_tar'

def tar_to_zip(*filenames):
    for one_filename in filenames:
        try:
            with ZipFile(z_content + f'{os.path.splitext(one_filename)[0]}.zip',
                         'w', compression=ZIP_DEFLATED) as zf:
                print(one_filename)
                tf = tarfile.open(one_filename, 'r:*')
                for one_tarinfo in tf:
                    print(f"\t{one_tarinfo}")
                    tf.extract(one_tarinfo, path=dir_tmp)
                    zf.write(f'{dir_tmp}/{one_tarinfo.name}',
                             arcname='cjp2_' + one_tarinfo.name)
        except tarfile.ReadError as e:
            print(f"Couldn't read from '{one_filename}'; ignoring")


def read_zip(read_con):
    print(CWHITE + "--> Reading zippy files..." + CEND)
    only_files = [f for f in os.listdir(read_con) if os.path.isfile(os.path.join(read_con, f))]
    for zipped_file in only_files:
        with zipfile.ZipFile(read_con + '/' + zipped_file, 'r') as f_zip:
            for name in f_zip.namelist():
                print(name, f_zip.read(name))
    print(CCYAN + "*** Completed reading zip files ***\n" + CEND)


os.mkdir(dir_tmp)
print()
tar_to_zip('foo.tar', 'bar.tar.gz', 'baz.tar.bz2', 'combo.tar', 'combo2.tar')
print()
shutil.rmtree(dir_tmp)
read_zip(z_content)




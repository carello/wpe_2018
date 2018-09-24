#! /usr/bin/env python3

import tarfile
import zipfile
from os import listdir
from tempfile import TemporaryDirectory
import os.path as path
# import m_colorit as col

CRED = '\033[91m'
CEND = '\033[0m'
CWHITE = '\033[37m'
CYELLOW = '\033[33m'
CCYAN = '\033[36m'


def convert_file(tar_name, z_con):
    try:
        my_tar = tarfile.open(tar_name)
    except (tarfile.ReadError, tarfile.CompressionError) as e:
        return f'Tar file {tar_name} opening error: {e}'

    zip_name = path.join(path.dirname(tar_name),
                         path.basename(tar_name).split('.')[0])

    with TemporaryDirectory() as tmp:
        my_tar.extractall(tmp)
        with zipfile.ZipFile(z_con + '/' + zip_name + '.zip', 'w', zipfile.ZIP_DEFLATED) as my_zip:
            for one_file in my_tar.getnames():
                my_zip.write(path.join(tmp, one_file), arcname='cjp_' + one_file)
            my_zip.comment = f'Converted from {tar_name}'.encode('utf-8')
            result = my_zip.testzip()
            if result is not None:
                return f'File {result} in {zip_name} is corrupted'
    return 'OK'


def tar_to_zip(names, zz_con):
    print('\n' + CWHITE + '--> Converting TAR files into ZIP files...' + CEND)
    for name in names:
        print(f'{name:15}... ', end='')
        if path.exists(name):
            if tarfile.is_tarfile(name):
                print(convert_file(name, zz_con))
            else:
                print(f"File {name}, is not a TAR file!")
        else:
            print(CRED + "ERROR: " + f"File '{name}' doesn't exist or is inaccessible" + CEND)
    print(CYELLOW + '*** Completed conversion, zip files saved in directory "zippy" ***\n' + CEND)


def read_zip(read_con):
    print(CWHITE + "--> Reading zippy files..." + CEND)
    only_files = [f for f in listdir(read_con) if path.isfile(path.join(read_con, f))]
    for zipped_file in only_files:
        with zipfile.ZipFile(read_con + '/' + zipped_file, 'r') as f_zip:
            for name in f_zip.namelist():
                print(name, f_zip.read(name))
    print(CCYAN + "*** Completed reading zip files ***" + CEND)


def main():
    tar_list = ['foo.tar', 'bar.tar.gz', 'baz.tar.bz2', 'combo.tar', 'combo2.tar', 'pre31.1.9y']
    z_content = 'zippy'

    tar_to_zip(tar_list, z_content)
    read_zip(z_content)
    print()


if __name__ == '__main__':
    main()

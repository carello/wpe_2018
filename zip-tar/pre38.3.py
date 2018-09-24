import tarfile, os, zipfile, shutil, glob, sys
import os.path as path
from os.path import isfile, join
from tempfile import TemporaryDirectory

dir_tmp = 'tmp_tar'
z_content = 'zippy'
tar_list = ['foo.tar', 'bar.tar.gz', 'baz.tar.bz2', 'combo.tar', 'combo2.tar', 'pre31.1.9y']
CRED = '\033[91m'
CEND = '\033[0m'
CBOLD = '\33[1m'
CWHITE = '\33[37m'


def convert_file(tar_name):
    """Converts one tar file of the name tar_name into zip file with the same
    basename. The function returns a string 'OK' on success or string describing
    conversion problem in case of a failure.
    """
    try:
        mytar = tarfile.open(tar_name)
    except (tarfile.ReadError, tarfile.CompressionError) as e:
        return f'Tar file {tar_name} opening error: {e}'
    zip_name = path.join(path.dirname(tar_name),
                         path.basename(tar_name).split('.')[0] + '.zip')
    # the content of the tar file is extracted into temporary directory, which
    # is deleted automatically after zipping all files
    with TemporaryDirectory() as tmp:
        mytar.extractall(tmp)
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as myzip:
            for one_file in mytar.getnames():
                # supplying the arcname argument assures that leading paths of
                # the files will not be saved in the zip archive
                myzip.write(path.join(tmp, one_file), one_file)
            # comment is just for fun :-)
            myzip.comment = f'Converted from {tar_name}'.encode('utf-8')
            result = myzip.testzip()
            if result is not None:
                return f'File {result} in {zip_name} is corrupted'
    return 'OK'


def tar_to_zip(names):
    """Converts batch of Unix .tar, .tar.gz, .tar.bz2 files into .zip files and
    saves them in the same directory as the original files.
    """
    print(CRED + '--> Converting TAR files into ZIP files:' + CEND)
    for name in names:
        print(f'\t{name:15} ... ', end='')
        if path.exists(name):
            if tarfile.is_tarfile(name):
                print(convert_file(name))
            else:
                print('is not a TAR file!')
        else:
            print('does not exists or is inaccessible')
    print('All done.')


def read_zip():
    print(CRED + "--> Reading zippy files..." + CEND)
    for z_file in glob.glob('*'):
        if z_file.endswith('.zip'):
            shutil.move(z_file, z_content)

    onlyfiles = [f for f in os.listdir(z_content) if isfile(join(z_content, f))]
    for zipped_file in onlyfiles:
        with zipfile.ZipFile(z_content + '/' + zipped_file, 'r') as f_zip:
            for name in f_zip.namelist():
                print(name, f_zip.read(name))


os.mkdir(z_content)
tar_to_zip(tar_list)
print()
read_zip()
print()
#shutil.rmtree(z_content)

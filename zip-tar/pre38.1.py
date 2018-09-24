import tarfile
import os
import zipfile
import glob

dir_tmp = 'tmp'


def test_tars(*args):
    for filename in [*args]:
        try:
            print(filename, tarfile.is_tarfile(filename))
        except IOError as e:
            print(filename, e)


def tar_to_zip(*args):
    for f in [*args]:
        #file_paths = []
        with tarfile.open(f, 'r') as t:
            t.extractall(dir_tmp)
            for root, directories, files in os.walk(dir_tmp):
                #for filename in files:
                #    filepath = os.path.join(root, filename)
                #    file_paths.append(filepath)
                file_paths = [os.path.join(root, filename) for filename in files]
                name_only = f.split('.')
                with zipfile.ZipFile(name_only[0] + '.zip', 'w') as zf:
                    for file in file_paths:
                        zf.write(file)
                for fs in glob.glob('tmp/*'):
                    os.remove(fs)


def read_zip(*args):
    for z in [*args]:
        f_zip = zipfile.ZipFile(z)
        for name in f_zip.namelist():
            print(name, f_zip.read(name))



# test_tars('foo.tar', 'bar.tar.gz', 'baz.tar.bz2')
# print()
tar_to_zip('foo.tar', 'bar.tar.gz', 'baz.tar.bz2')
read_zip('foo.zip',  'bar.zip', 'baz.zip')

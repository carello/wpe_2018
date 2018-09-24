import tarfile, os, zipfile, shutil, glob, sys
from os.path import isfile, join

dir_tmp = 'tmp_tar'
z_content = 'zippy'
tar_list = ['foo.tar', 'bar.tar.gz', 'baz.tar.bz2', 'combo.tar', 'combo2.tar', ]
CRED = '\033[91m'
CEND = '\033[0m'
CBOLD = '\33[1m'
CWHITE = '\33[37m'


def test_tars(t_list):
    print(CRED + "\n--> Testing to validate tar files..." + CEND)
    for filename in t_list:
        try:
            print(f'{filename:20} \tvalid_tar_file? - {tarfile.is_tarfile(filename)}')
            if tarfile.is_tarfile(filename) is False:
                print(f"\n-->  {CBOLD + 'ERROR:' + CEND} {CRED + filename + ' is not a tar file' + CEND}\n")
                sys.exit(0)
        except IOError as e:
            print(f'\n {CRED + str(e) + CEND}\n')
            return sys.exit(0)


def tar_to_zip(t_list):
    for f in t_list:
        with tarfile.open(f, 'r') as t:
            t.extractall(dir_tmp)
            name_only = f.split('.')

            with zipfile.ZipFile(z_content + '/' + name_only[0] + '.zip', 'w') as zf:
                for file in t.getnames():
                    zf.write(os.path.join(dir_tmp, file), arcname='cp2_' + file)

                for fs in glob.glob(dir_tmp + '/*.*'):
                    os.remove(fs)


def read_zip():
    print(CRED + "--> Reading zippy files..." + CEND)
    only_files = [f for f in os.listdir(z_content) if isfile(join(z_content, f))]
    for zipped_file in only_files:
        with zipfile.ZipFile(z_content + '/' + zipped_file, 'r') as f_zip:
            for name in f_zip.namelist():
                print(name, f_zip.read(name))


def main():
    os.mkdir(dir_tmp)
    test_tars(tar_list)
    print()
    tar_to_zip(tar_list)
    shutil.rmtree(dir_tmp)
    read_zip()
    print()


if __name__ == '__main__':
    main()

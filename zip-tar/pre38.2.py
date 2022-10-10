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
    print(CRED + "--> Testing to validate tar files..." + CEND)
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
            
            import os
            
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(t, dir_tmp)
            name_only = f.split('.')
            #for root, directories, files in os.walk(dir_tmp):
            #    file_paths = [os.path.join(root, filename) for filename in files]

            with zipfile.ZipFile(z_content + '/' + name_only[0] + '.zip', 'w') as zf:
                #for file in file_paths:
                #    zf.write(file)
                for file in t.getnames():
                    zf.write(os.path.join(dir_tmp, file), file)

                for fs in glob.glob(dir_tmp + '/*.*'):
                    os.remove(fs)


def read_zip(r_list):
    print(CRED + "--> Reading zip files..." + CEND)
    for file_tar in r_list:
        file_tar_name = file_tar.split('.')

        with zipfile.ZipFile(file_tar_name[0] + '.zip', 'r') as f_zip:
                for name in f_zip.namelist():
                    print(name, f_zip.read(name))


def read_zip2():
    print(CRED + "--> Reading zippy files..." + CEND)
    #for z_file in glob.glob('*'):
    #    if z_file.endswith('.zip'):
    #        shutil.move(z_file, z_content)

    only_files = [f for f in os.listdir(z_content) if isfile(join(z_content, f))]
    for zipped_file in only_files:
        with zipfile.ZipFile(z_content + '/' + zipped_file, 'r') as f_zip:
            for name in f_zip.namelist():
                print(name, f_zip.read(name))


def clean_house():
    for stuff in glob.glob('./*.zip'):
        os.remove(stuff)


def main():
    print()
    test_tars(tar_list)
    print()
    os.mkdir(dir_tmp)
    #os.mkdir(z_content)
    tar_to_zip(tar_list)
    #read_zip(tar_list)
    #clean_house()
    shutil.rmtree(dir_tmp)
    print()
    read_zip2()
    print()
    #shutil.rmtree(z_content)


if __name__ == '__main__':
    main()

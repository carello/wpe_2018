import sys


class Tee(object):
    def __init__(self, *files):
        self.files = files

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for one_file in self.files:
            one_file.close()

    def write(self, text):
        for one_file in self.files:
            one_file.write(text)

    def writelines(self, lines):
        for one_file in self.files:
            one_file.writelines(lines)


if __name__ == '__main__':
    f1 = open('tee11.txt', 'w')
    f2 = open('tee22.txt', 'w')

    # Can implement without sys.stdout if desired
    with Tee(sys.stdout, f1, f2) as g:
        g.write('chet\n')
        g.write('connie\n')
        g.write('789\n')

import argparse

default = 3

parser = argparse.ArgumentParser(description='Combines head and tail commands')
parser.add_argument('-s', '--start', nargs='?', type=int, default=default,
                    metavar='number', help='number of head lines, default is 3')
parser.add_argument('-e', '--end', nargs='?', type=int, default=default,
                    metavar='number', help='number of head lines, default is 3')
parser.add_argument('-f', '--file', required=True, metavar='name', help='file name')
arguments = parser.parse_args()


head = default if arguments.start is None or arguments.start < 0 else arguments.start
tail = default if arguments.end is None or arguments.end < 0 else arguments.end

try:
    with open(arguments.file, 'r') as infile:
        all_lines = infile.readlines()
except OSError as e:
    print(f'File: < {arguments.file} > can not be opened\n{e.strerror}')
    raise SystemExit

if head + tail > len(all_lines):
    head = len(all_lines)
print(''.join(all_lines[:head]), end='')
skipped = len(all_lines) - head - tail
if skipped > 0:
    print(f'... <<< skipped {skipped} lines of {arguments.file} >>> ...')
if skipped >=0 and tail > 0:
    print(''.join(all_lines[-tail:]), end='')




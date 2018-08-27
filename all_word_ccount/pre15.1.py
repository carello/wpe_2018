import glob
import time


def count_words_sequential(pattern):
    total = 0
    for one_filename in glob.glob(pattern):
        print(one_filename)
        try:
            total += len(open(one_filename).read().split())
        except:
            pass

    return total


pattern = '/tmp/w*'

first = time.time()
print(count_words_sequential(pattern))
second = time.time()

print("Seq version took {}".format(second - first))


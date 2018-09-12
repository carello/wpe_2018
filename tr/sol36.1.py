from itertools import zip_longest


def tr(source, dest):
    d = dict(zip_longest(source, dest, fillvalue=dest[-1]))
    # print(d, '\n')

    def replace(s):
        output = list(s)
        print(output)
        for index, item in enumerate(output):
            # print(index, item)
            # print(d.get(item))
            output[index] = d.get(item, item)

        return ''.join(output)
    return replace


vowels_to_y = tr('aeiou', 'zy')
print(vowels_to_y('the quick brown fox jumps over the lazy dog'))



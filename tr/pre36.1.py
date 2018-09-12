

def tr(*args):
    def wrapper(f):
        lst = list()
        [lst.append(args[1]) if i in args[0] else lst.append(i) for i in f]
        #for i in f:
        #    if i in args[0]:
        #        lst.append(args[1])
        #    else:
        #        lst.append(i)
        mytr = ''.join(lst)
        return mytr
    return wrapper


out = tr('aeiou', 'zy')
print(out("the quick brown fox jumps over the lazy dog"))





def str_range(start, stop, step=1):
    for _ord in range(ord(start.lower()), ord(stop.lower()) + 1, step):
        yield chr(_ord)


print(list(str_range("j", "p")))
print(list(str_range("a", "f", 2)))

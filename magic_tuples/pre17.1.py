# list comprehension of a nested list, returns an expression
# see solution, there are more examples on expressions
# note Leuven's solution is wrong.


def magic_tuples(total, maxval):
    return ((x, y)
            for x in range(maxval)
            for y in range(maxval)
            if x + y == total)


for t in magic_tuples(60, 100):
    print(t)

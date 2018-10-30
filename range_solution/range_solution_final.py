#! /usr/bin/python3

'''
Objective:
1) A function ("myrange2") that takes one, two, or three parameters and returns a list for Python 2's "range" function.
2) A generator function ("myrange3") that takes one, two, or three parameters and returns an iterator (a generator).
In both cases, it should be possible to take the output of calling our function and stick it into a "for" loop:
    for x in myrange2(10, 30, 3):
        print(x)
'''

# Python2 method - return list
'''
Can implement via:
- with a single argument, which indicates the maximum number. this one is mandatory.
- with two arguments, indicating min (first) and max (second)
- with three arguments, third being the step
'''

def myrange2(first, second=None, step=1):
    if second is None:
        current = 0
        end = first
    else:
        current = first
        end = second

    output = []
    while current < end:
        output.append(current)
        current += step
    return output
    #print('current = {}'.format(current))
    #print('end: = {}'.format(end))
    #print('step: = {}'.format(step))

#print(myrange2(10, 20, 4))


# Python3 style - return a generator
'''
'''
def myrange3(first, second=None, step=1):
    if second is None:
        current = 0
        end = first
    else:
        current = first
        end = second

    while current < end:
        yield current
        current += step


for x in myrange3(10, 20, 3):
    print(x)


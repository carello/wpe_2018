
# Objective
# 1) Create a text file containing 100 exercises
# 2) Each exercise will involve addition and subtraction of 4 randomly chosen
#    positive and negative integers. Range this from -40 to 40 but make room to adjust range
#    if necessary/desired.
# Example of what the file might look like:
#   [  1] (  19) - (   1) - (   4) + (  28) = ______
#   [  2] ( -18) + (   8) - (  16) - (   2) = ______
#   [  3] (  -8) + (  17) - (  15) + ( -29) = ______
#   [  4] ( -31) - ( -12) - (  -5) + ( -26) = ______
#   [  5] ( -15) - (  12) - (  14) - (  31) = ______
# Keep thing aligned and put () around all numbers.
#
# 3) Next read through the lines of this text file and calculate the solutions.
# Example output:
#   [  1] (  19) - (   1) - (  40) + (  28) =  42
#   [  2] ( -18) + (   8) - (  16) - (   2) = -28
#   [  3] (  -8) + (  17) - (  15) + ( -29) = -35
#   [  4] ( -31) - ( -12) - (  -5) + ( -26) = -40
#   [  5] ( -15) - (  12) - (  14) - (  31) = -72
#
import random

sample_numbers = list()

template = '({0:4}) {1:1} ({2:4}) {3:1} ({4:4}) {5:1} ({6:4}) = ______'

def pick_op():
    add_op = '+'
    add_sub = '-'
    return random.choice((add_op, add_sub))


def gen_number_set():
    for y in range(0, 10):
        sample_numbers.append([random.randrange(-40, 40) for x in range(0, 4)])
    return

def view_samples():
    print('\n' + '-' * 80 )
    print('--- Sample math problems ---\n')
    for indx, nums in enumerate(sample_numbers):
        print('[{0:>4}]'.format(str(indx + 1)), end=' ')
        print(template.format(nums[0], pick_op(), nums[1], pick_op(), nums[2], pick_op(), nums[3]))
    print('\n' + '-' * 80)
    return


if __name__ == '__main__':

    gen_number_set()
    view_samples()

    with open('sample_test.txt', 'w') as f:
        for indx, nums in enumerate(sample_numbers):
            f.write('[{0:>4}] '.format(str(indx + 1)))
            f.write(template.format(nums[0], pick_op(), nums[1], pick_op(), nums[2], pick_op(), nums[3]))
            f.write('\n')

    with open('sample_test.txt', 'r') as h:
        for l in h:
            total = 0

            line_num = l[1:5]
            num_one = l[8:12]
            op_one = l[14:15]
            num_two = l[17:21]
            op_two = l[23:24]
            num_three = l[26:30]
            op_three = l[32:33]
            num_four = l[35:39]

            if op_one == '+':
                total = (int(num_one) + int(num_two))
            elif op_one == '-':
                total = (int(num_one) - int(num_two))
            if op_two == '+':
                total += int(num_three)
            elif op_two == '-':
                total -= int(num_three)
            if op_three == '+':
                total += int(num_four)
            elif op_three == '-':
                total -= int(num_four)

            print('[{0:>4}]'.format(int(line_num)), end=' ')
            print('({0:4}) {1:1} ({2:4}) {3:1} ({4:4}) {5:1} ({6:4}) = {7:>4}'.format(str(num_one), op_one,
                                                                                      str(num_two), op_two,
                                                                                      str(num_three), op_three,
                                                                                      str(num_four), str(total)))


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
import re
import operator

# Variables that can be changed based on desired requirements
MAX_NUMBER = 40
MIN_NUMBER = -40
NUM_QUESTIONS = 10
TEST_FILENAME = 'sample_math_test.txt'
WIDTH = str(4)
TEMPLATE = "({0:" + WIDTH + "}) {1:1} " \
           "({2:" + WIDTH + "}) {3:1} " \
           "({4:" + WIDTH + "}) {5:1} " \
           "({6:" + WIDTH + "})"


def pick_op():
    return random.choice(('+', '-'))


def gen_number_set(minl, maxl, num_questions):
    sample_numbers = list()
    for y in range(0, num_questions):
        sample_numbers.append([random.randrange(minl, maxl) for _ in range(0, 4)])
    return sample_numbers


def view_samples(q):
    print('\n{0:#^50}\n'.format('  Practice Math Problems  '))
    for indx, nums in enumerate(q):
        print('[{0:>4}]'.format(str(indx + 1)), end=' ')
        print(TEMPLATE.format(nums[0], pick_op(), nums[1], pick_op(), nums[2], pick_op(), nums[3]), end='')
        print(' = ______')
    print('\n' + '-' * 50)
    return


def create_test(q):
    with open(TEST_FILENAME, 'w') as f:
        for indx, nums in enumerate(q):
            f.write('[{0:>4}] '.format(str(indx + 1)))
            f.write(TEMPLATE.format(nums[0], pick_op(), nums[1], pick_op(), nums[2], pick_op(), nums[3]))
            f.write(' = ______\n')
    return


def answers(s):
    print('\n{0:#^47}\n'.format('  ANSWER KEY  '))

    ops = {'+': operator.add, '-': operator.sub}

    with open(TEST_FILENAME, 'r') as h:
        for l in h:

            nums_ops = s.search(l)
            line_num = nums_ops.group(1)
            num_one = nums_ops.group(2)
            op_one = nums_ops.group(3)
            num_two = nums_ops.group(4)
            op_two = nums_ops.group(5)
            num_three = nums_ops.group(6)
            op_three = nums_ops.group(7)
            num_four = nums_ops.group(8)

            sub_one = ops[op_one](int(num_one), int(num_two))
            sub_two = ops[op_two](sub_one, int(num_three))
            total = ops[op_three](sub_two, int(num_four))

            print('[{0:>4}]'.format(int(line_num)), end=' ')
            print(TEMPLATE.format(str(num_one), op_one, str(num_two), op_two, str(num_three),
                                  op_three, str(num_four)), end=' = ')
            print('{0:>4}'.format(str(total)))

            # Regex alternative example... needs work to make useful in this program
            # numsx = [int(num) for num in re.findall(r'-?\d+', l)[1:]]  # extracts numbers
            # opsx = re.findall(r' ([+-]) ', l)  # extracts operators


if __name__ == '__main__':

    m = re.compile('\[([^()]*)\].'
                   '\(([^()]*)\)'
                   '\s([-|+])\s'
                   '\(([^()]*)\)'
                   '\s([-|+])\s'
                   '\(([^()]*)\)'
                   '\s([-|+])\s'
                   '\(([^()]*)\)')

    sample_questions = gen_number_set(MIN_NUMBER, MAX_NUMBER, NUM_QUESTIONS)

    # Optionally, preview print out
    view_samples(sample_questions)

    create_test(sample_questions)
    answers(m)
    print()

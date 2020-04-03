"""
Letter is invoked and passed n
First we mod n

Mod of n tells us two things
	1. What letter to call next
	2. Which algorithm for the current letter to apply to n

We apply the appropriate algorithm for current letter based on mod n
We call the next letter that is dictated by mod
Pass that function the output of appropriate algorithm for current letter
"""


# Rule: If mod is zero we A - F
# Further: F has 3 outcomes:
# 		1 goes to e
# 		2 goes to g
# 		0 goes to H




import argparse
import sys
from datetime import datetime




DEFAULT_START = 1

DEFAULT_END = 1000000000000


DEFAULT_INTERVAL = 317

CHECK_INTERVAL = 1
DO_CHECK = False



def a(n, sequence_s):
    sequence_s += 'a'
    # print(f'a:{n}')
    mod = (n % 3)
    if mod == 0:
        sequence_s = f((n * 2) // 3, sequence_s)
    elif mod == 1:
        sequence_s = h(n, sequence_s)
    elif mod == 2:
        sequence_s = e((n * 4 - 2) // 3, sequence_s)
    else:
        print("Something went wrong in A")

    return sequence_s


def b(n, sequence_s):
    sequence_s += 'b'
    # print(f'a:{n}')
    mod = (n % 3)
    if mod == 0:
        sequence_s = i(((8 * n) // 3) - 1, sequence_s)
    elif mod == 1:
        sequence_s = c(((4 * n) - 1) // 3, sequence_s)
    elif mod == 2:
        sequence_s = d(((4 * n) - 2) // 3, sequence_s)
    else:
        print("Something went wrong in B")

    return sequence_s


def c(n, sequence_s):
    sequence_s += 'c'
    # print(f'c:{n}')
    mod = (n % 3)
    if mod == 0:
        sequence_s = e((n * 4) // 3, sequence_s)
    elif mod == 1:
        sequence_s = f((n * 2 + 1) // 3, sequence_s)
    elif mod == 2:
        sequence_s = h(n, sequence_s)
    else:
        print("Something went wrong in C")

    return sequence_s


def d(n, sequence_s):
    sequence_s += 'd'
    # print(f'd:{n}')
    mod = (n % 3)
    if mod == 0:
        sequence_s = d((n * 4) // 3, sequence_s)
    elif mod == 1:
        sequence_s = i(n, sequence_s)
    elif mod == 2:
        sequence_s = c((n * 4 + 1) // 3, sequence_s)
    else:
        print("Something went wrong in D")

    return sequence_s


def e(n, sequence_s):
    sequence_s += 'e'
    # print(f'e:{n}')
    mod = (n % 3)
    if mod == 0:
        sequence_s = c((n * 2) // 3, sequence_s)
    elif mod == 1:
        sequence_s = i(n, sequence_s)
    elif mod == 2:
        sequence_s = d((n * 2 - 1) // 3, sequence_s)
    else:
        print("Something went wrong in E")

    return sequence_s


def f(n, sequence_s):
    sequence_s += 'f'
    # print(f'f:{n}')
    mod = (n % 3)
    if mod == 0:
        sequence_s = h(n, sequence_s)
    elif mod == 1:
        sequence_s = e((n * 4 - 1) // 3, sequence_s)
    elif mod == 2:
        sequence_s = g((n * 2 - 1) // 3, sequence_s)
    else:
        print("Something went wrong in F")

    return sequence_s


def g(n, sequence_s):
    sequence_s += 'g'
    # print(f'g:{n}')
    mod = (n % 3)
    if mod == 0:
        sequence_s = g((n * 4) // 6, sequence_s)
    elif mod == 1:
        sequence_s = h(n, sequence_s)
    elif mod == 2:
        sequence_s = e((n * 4 + 1) // 3, sequence_s)
    else:
        print("Something went wrong in G")

    return sequence_s


def h(n, sequence_s):
    sequence_s += 'h'
    # print(f'h:{n}')

    return sequence_s


def i(n, sequence_s):
    sequence_s += 'i'
    # print(f'i:{n}')

    return sequence_s


def lines():
    print(f'-----')


def letter(n):
    """
    Letter is invoked and passed n
    First we mod n

    Mod of n tells us two things
        1. Which algorithm of current function to apply to n
        1. What letter to call next

    We apply the appropriate algorithm for current letter based on mod n
    We note the next letter that is dictated by mod

    Function returns two variables.
        1. The outcome of the math
        2. The next expected letter, or quit condition
        3. No.. No I don't think it will do that
    """


def add_to_dict(n, sequence_s, dict_d):
    if sequence_s in dict_d:
        if len(dict_d[sequence_s]) < 2:
            dict_d[sequence_s].append(n)
    else:
        # print(f'Did not find a key for {sequence_s}')
        dict_d[sequence_s] = [n]


def print_dictionary(dict_d, outf=sys.stdout):
    # print('--- Dictionary ---')
    for x, y in dict_d.items():
        outf.write(f'{x} : {y}\n')


def print_dict_stats(dict_d, outf=sys.stdout):
    import pandas as pd
    outf.write("Length = {}\n".format(len(dict_d)))

    # sr_keys = pd.Series(list(dict_d))
    # print("Longest key: {}".format(sr_keys.apply(lambda k: len(k)).argmax()))

    df = pd.DataFrame({"key": list(dict_d.keys())})
    df["value"] = [dict_d[k] for k in df.key]
    ind = df.key.apply(lambda k: len(k)).argmax()
    lstr = df.key[ind] # df.key.apply(lambda k: len(k)).max()
    outf.write("Longest key length: {}\n".format(len(lstr)))
    outf.write("Longest key: {}\n".format(lstr))




def main(start, end, interval=DEFAULT_INTERVAL):
    '''.'''
    '''mode = 0 for a'''
    '''mode = 1 for b'''
    mode = 0

    dict_d = {}

    for n in range(start, end, interval):
        sequence_s = ''
        # print(f'Evaluating: {n}')

        if DO_CHECK and n % CHECK_INTERVAL == 1:
            stime = datetime.now()

        if mode:
            sequence_s = b(n, sequence_s)

        else:
            sequence_s = a(n, sequence_s)

        '''I now have a meaningful string: sequence_s'''
        # print(f'My string is: {sequence_s}')

        '''Evaluate: Is this string an existing key? 
            If not, make one'''

        add_to_dict(n, sequence_s, dict_d)

        if DO_CHECK and n % CHECK_INTERVAL == 0:
            print("\t{}:\t{}".format(n, datetime.now() - stime))


    '''
    https://www.geeksforgeeks.org/python-ways-to-create-a-dictionary-of-lists/
    '''
    # list1 = [12, 'a', 'b', 'c']
    # list2 = [11, 'a', 'b', 'c']
    # print(list1[1:] == list2[1:])

    # print("Closing")

    return dict_d


if __name__ == '__main__':

    """ 
    Usage Examples:
    python bryan-g_2.py -s 1 -e 10000 -i 1 
    python bryan-g_2.py -s 1 -e 10000 
    python bryan-g_2.py -s 1 -e 10000  -o b_out_1_1000_1.txt 
    
    """

    parser = argparse.ArgumentParser(description="Desciption TBD")

    parser.add_argument("--start", "-s", default=DEFAULT_START, type=int, help="Starting number")
    parser.add_argument("--end", "-e", default=DEFAULT_END, type=int, help="Ending number")
    parser.add_argument("--interval", "-i", default=DEFAULT_INTERVAL, type=int, help="Interval")
    parser.add_argument("--outfname", "-o", default=None, type=str, help="Output file name")

    args = parser.parse_args()

    stime0 = datetime.now()
    print("Started at {}".format((stime0)))

    dict_d = main(args.start, args.end, args.interval)

    etime0 = datetime.now()
    print("Ended at {}".format((etime0)))

    if args.outfname is None:
        outf = sys.stdout
    else:
        outf = open(args.outfname, 'w')
        print("Output writing in {}...".format(args.outfname))

    outf.write("\nTOTAL:\t{}\n".format(etime0 - stime0))

    print_dictionary(dict_d, outf)
    print_dict_stats(dict_d, outf)

    print("Output written in {}".format(args.outfname))

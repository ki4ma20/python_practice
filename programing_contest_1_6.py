#!/usr/bin/env python

def is_trianglable(data):
    maximum = max(data)
    s = 0
    for i in data:
        s += i;
    s -= maximum
    if s > maximum:
        return 1
    else:
        return 0

def get_triangle_round_length(data_array):
    s = 0

    if is_trianglable(data_array) == 1:
        for l in data_array:
            s += l
    return s

def print_triangle_data(data):
    print "input data is", data
    print "round length is", get_triangle_round_length(data)

if __name__=='__main__':
    test_data = (4, 3, 5)
    print_triangle_data(test_data)

    data_size = 5
    data_array = (2, 3, 4, 5, 10)

    triangle_data = [0, 0, 0]

    maximum_round_length = 0

    for a in xrange(data_size):
        for b in xrange(a + 1,data_size):
            for c in xrange(b + 1,data_size):

                triangle_data[0] = data_array[a]
                triangle_data[1] = data_array[b]
                triangle_data[2] = data_array[c]

                print_triangle_data(triangle_data)


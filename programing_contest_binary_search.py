#!/usr/bin/env python

def binary_search(data_array, search_value):
    data_size = len(data_array)
    seek_area_start = 0
    seek_area_end = data_size

    while seek_area_end - seek_area_start >= 1:
        center_address = (seek_area_start + seek_area_end) / 2
        center_value = data_array[center_address]

        if center_value == search_value:
            return 1
        elif center_value < search_value:
            seek_area_start = center_address + 1
        else:
            seek_area_end = center_address
    return 0

def get_sum_table(data_array, sum_table):
    data_size = len(data_array)

    for data1 in data_array:
        for data2 in data_array:
            sum_table.append(data1 + data2)

if __name__=='__main__':
    data_array = [5, 3, 65, 7, 89, 6, 7, 9, 10]
    search_value = 15
    data_array.sort()

    print "value ", search_value
    if binary_search(data_array, search_value) == 1:
        print "Exists"
    else:
        print "Does not exist"

    sum_table = []
    get_sum_table(data_array, sum_table)
    sum_table.sort()

    if binary_search(sum_table, search_value) == 1:
        print "Exists in sum table"
    else:
        print "Does not exist in sum table"


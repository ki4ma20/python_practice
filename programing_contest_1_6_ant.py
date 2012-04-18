#! /usr/bin/env python

length_of_rod = 10

position_of_ants = (2, 6, 7)

def calculate_shortest_dead_time_of_ant(position):

    length_to_nearer_end_point_of_rod = min(position, length_of_rod - position)

    return length_to_nearer_end_point_of_rod

def calculate_longest_dead_time_of_ant(position):

    length_to_farer_end_point_of_rod = max(position, length_of_rod - position)

    return length_to_farer_end_point_of_rod

if __name__=='__main__':

    shortest_dead_time_array = []
    longest_dead_time_array = []

    for position in position_of_ants:
        shortest_dead_time_array.append(calculate_shortest_dead_time_of_ant(position))
        longest_dead_time_array.append(calculate_longest_dead_time_of_ant(position))

    # calculate time of all members falled
    print "minimum end time is ", max(shortest_dead_time_array)
    print "maximum end time is ", max(longest_dead_time_array)


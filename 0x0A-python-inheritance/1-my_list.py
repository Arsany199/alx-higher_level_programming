#!/usr/bin/python3
'''Define 1-my_list'''


class MyList(list):
    '''class MyList'''

    def print_sorted(self):
        '''prints the list sorted'''
        print(sorted(self))

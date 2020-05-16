"""Assignment Four: Creating a Sensor Dictionary and Lists

Author: Arvind Kumar
CWID: 20372024
Date: 10/22/2018

Enhancements in this release: Using and getting introduced to recursions.

['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
26
"""

alphabet = [l for l in 'abcdefghijklmnopqrstuvwxyz']


def reverse_a_list(my_list):
    if len(my_list)>0:
        print(len(my_list))
    if len(my_list) == 0:
        return []
    return [my_list[-1]]+reverse_a_list(my_list[:-1])

print(alphabet)
print(reverse_a_list(alphabet))
print(alphabet)

'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/arvindkumar/Desktop/UCI/second year/fall quarter/cs 3a Foothill/Assignment 5: Reversing a List with Recursion.py"
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Process finished with exit code 0

'''
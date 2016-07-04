#! /usr/bin/env python

# Copyright Lajos Katona
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.


def selection_brute(mlist, t):
    for i, l in enumerate(mlist):
        if t == l:
            return i
    return -1


def selection_pythonic(mlist, t):
    return mlist.index(t)


def select_max_brute(mlist):
    max = mlist[0]
    max_index = -1
    for i, l in enumerate(mlist):
        if l > max:
            max_index = i
    return max_index


def select_max_pythonic(mlist):
    return mlist.index(max(mlist))


def select_min_brute(mlist):
    min = mlist[0]
    min_index = -1
    for i, l in enumerate(mlist):
        if l < min:
            min_index = i
    return min_index


def select_min_pythonic(mylist):
    return mylist.index(min(mylist))


if __name__ == '__main__':
    mylist = [1, 2, 3, 4, 5]
    mylist2 = [1, 2, 3, 2, 1, 10, 9, 8, 11, -1]
    print(selection_brute(mylist, 4))
    print(selection_pythonic(mylist, 4))
    print(select_max_brute(mylist2))
    print(select_max_pythonic(mylist2))
    print(select_min_brute(mylist2))
    print(select_min_pythonic(mylist2))

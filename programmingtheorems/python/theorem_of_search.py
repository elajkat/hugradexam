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


def search_linear(mylist, t):
    for i, l in enumerate(mylist):
        if l == t:
            return i
    return -1


def search_logarithm(mylist, t):
    lower_b = 0
    upper_b = len(mylist)
    while True:
        if lower_b == upper_b:
            return -1
        mid = (lower_b + upper_b) // 2
        mid_item = mylist[mid]
        if mid_item == t:
            return mid
        if mid_item < t:
            lower_b = mid + 1
        else:
            upper_b = mid


if __name__ == '__main__':
    mylist = [1, 2, 3, 4, 5]
    print(search_linear(mylist, 4))
    print(search_logarithm(mylist, 4))

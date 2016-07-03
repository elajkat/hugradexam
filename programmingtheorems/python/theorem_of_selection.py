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


def selection_brute(mylist, t):
    for i, l in enumerate(mylist):
        if t == l:
            return i
    return 0


def selection_pythonic(mylist, t):
    return mylist.index(t)


if __name__ == '__main__':
    mylist = [1, 2, 3, 4, 5]
    print(selection_brute(mylist, 4))
    print(selection_pythonic(mylist, 4))
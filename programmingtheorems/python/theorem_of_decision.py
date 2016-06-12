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


def decide_if_at_least_one_dummy(mylist, t):
    result = False
    for i in mylist:
        if i == t:
            result = True
            break
    return result


def decide_if_all_dummy(mylist, t):
    result = True
    for i in mylist:
        if i != t:
            result = False
            break
    return result


def decide_if_at_least_one_conprehension(mylist, t):
    return any(True if i == t else False for i in mylist)


def decide_if_all_conprehension(mylist, t):
    return all(True if i == t else False for i in mylist)


if __name__ == '__main__':
    mylist = [1, 2, 3, 4, 5]
    print(decide_if_at_least_one_dummy(mylist, 8))
    print(decide_if_at_least_one_conprehension(mylist, 9))

    mylist = [2, 2, 2, 3, 2]
    print(decide_if_all_dummy(mylist, 2))
    print(decide_if_all_conprehension(mylist, 2))

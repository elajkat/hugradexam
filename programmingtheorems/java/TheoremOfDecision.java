/******************************************************************************
 * Copyright Lajos Katona
 *
 *     Licensed under the Apache License, Version 2.0 (the "License");
 *     you may not use this file except in compliance with the License.
 *     You may obtain a copy of the License at
 *
 *          http://www.apache.org/licenses/LICENSE-2.0
 *
 *     Unless required by applicable law or agreed to in writing, software
 *     distributed under the License is distributed on an "AS IS" BASIS,
 *     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *     See the License for the specific language governing permissions and
 *     limitations under the License.
 *****************************************************************************/

public class TheoremOfDecision {

    public Boolean decide_if_at_least_one(int[] mylist, int t) {
        for (int i : mylist) {
            if (i == t) {
                return true;
            }
        }
        return false;
    }

    public Boolean decide_if_all(int[] mylist, int t) {
        for (int i : mylist) {
            if (i != t) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int[] mylist = {1, 2, 3, 4, 5};
        TheoremOfDecision tod = new TheoremOfDecision();
        System.out.println(tod.decide_if_at_least_one(mylist, 8));

        int[] mylist2 = {2, 2, 3, 2, 2};
        System.out.println(tod.decide_if_all(mylist2, 2));
    }

}
'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
'''

import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #keyElem = {}
        keyElem = collections.defaultdict(list)
        for elem in strs:
            keySorted = "".join(sorted(elem))
            # print(keySorted, elem)
            keyElem[keySorted] += [elem]
            '''
            if keyElem.get(keySorted, "0") == "0":
                # print("in if")
                keyElem[keySorted] = [elem]
            else:
                # print("in else", keyElem[keySorted])
                keyElem[keySorted].append(elem)
                # keyElem[keySorted] =
            '''
            # print(keyElem, "\n")

        # print(keyElem)
        returnList = []
        for values in keyElem.values():
            returnList.append(values)

        return returnList
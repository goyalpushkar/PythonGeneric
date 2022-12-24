'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        search_word = ""
        found_words = []
        start_index = 0
        for index in range(0, len(s)):
            search_word += s[index]

            print(f"search_word start: {search_word}")
            for j in range(start_index, len(wordDict)):
                if wordDict[j] == search_word:
                    found_words.append(search_word)
                    search_word = ""
                    start_index = j

            print(found_words)
            if search_word in found_words:
                search_word = ""

            print(f"search_word end: {search_word}")

        if search_word == "":
            return True
        else:
            return False


if __name__ == '__main__':

    s = "aaaaaaa"
    #  "catsandog"
    word_dict = ["aaaa","aaa"]
    # ["cats", "dog", "sand", "and", "cat"]

    solution = Solution()
    result = solution.wordBreak(s, word_dict)
    print(result)

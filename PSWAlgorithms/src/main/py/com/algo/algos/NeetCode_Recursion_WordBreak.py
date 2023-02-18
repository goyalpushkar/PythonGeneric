'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
sequence of one or more dictionary words.

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
import collections

class Solution(object):
    # "aaaaaaa", ["aaaa", "aaa"]
    '''
    0 1 2 3 4 5 6
    a a a a a a a", ["aaaa", "aaa"]
                _ -> False
              _ -> False
            _ -> True
          _ -> True
        _ -> True
      _ -> True
    _ => True

    1. prepare a DP array of len of string and initialize all values to False and mark last value (base case as True)
    2. Check from the last character in the string for each of the words if it is there as a word if yes then set
    dp value as True
    '''
    def wordBreak(self, s, wordDict):
        # dp = [False for _ in range(len(s)+1)]
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        # Start from last character if any dict word exists
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]

                if dp[i]:
                    break

        # print(dp)
        return dp[0]

    # Trie Method
    def wordBreak_trie(self, s, wordDict):
        trie = {}
        for word in wordDict:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node['#'] = True

        print(f"node: {node} trie: {trie}")
        bfs = [trie]
        for c in s:
            nxt = []
            trie_added = False
            while bfs:
                node = bfs.pop()
                if not c in node: continue
                nxt.append(node[c])
                if '#' in node[c] and not trie_added:
                    nxt.append(trie)
                    trie_added = True
            bfs = nxt
        return trie in bfs

    def wordBreak_trie2(self, s, wordDict):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        for word in wordDict:
            ptr = trie
            for c in word:
                ptr = ptr[c]
            ptr['#'] = ''

        print(f"ptr: {ptr}")

        @cache
        def dp(i):
            if i >= len(s):
                return True

            result = False

            ptr = trie
            for j in range(i, len(s) + 1):
                if '#' in ptr:
                    result = result or dp(j)
                    if result:
                        return result

                if j == len(s):
                    break

                if s[j] in ptr:
                    ptr = ptr[s[j]]
                    continue
                else:
                    break

            return result

        return dp(0)

    # 35/45
    # failed "aaaaaaa", ["aaaa","aaa"] - aaa, aaa, a will result in failure
    def wordBreak_n(self, s, wordDict):

        word_dict = {}
        for word in wordDict:
            word_dict[word] = word_dict.get(word, 0) + 1

        start = 0
        end = 0
        new_word = ""
        # while start <= len(s) - 1:
        #     print(f"start: {start}")
        #     new_word += s[start]
        #     # to check if new_word has one last character in it
        #     if new_word in word_dict:
        #         new_word = ""
        #         start += 1
        #         continue
        #
        #     end = start + 1
        while end <= len(s) - 1:
            new_word += s[end]
            print(f"end: {end} new_word: {new_word}")
            if new_word in word_dict:
                new_word = ""
                # start = end + 1

            end += 1

            # to check if new_word has one last character in it
            # if new_word != "" and new_word in word_dict:
            #     new_word = ""
            #
            # start += 1

        return False if new_word != "" else True

    # 30/45
    def wordBreak_exis(self, s, wordDict):
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

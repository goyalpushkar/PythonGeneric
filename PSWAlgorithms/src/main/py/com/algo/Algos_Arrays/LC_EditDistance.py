'''
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.


Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "a", t = ""
Output: true
Example 4:

Input: s = "", t = "A"
Output: true


Constraints:

0 <= s.length <= 104
0 <= t.length <= 104
s and t consist of lower-case letters, upper-case letters and/or digits.
'''


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        # If empty strings
        if len(s) == len(t) and len(t) == 0:
            return False

        # If difference between strings is huge
        if len(s) - len(t) > 1 or len(s) - len(t) < -1:
            return False

        # If strings are same
        if s == t:
            return False

        diff = 0
        for i in range(min(len(s), len(t))):
            if s[i] == t[i]:
                continue
            else:
                if s[i + 1:] == t[i + 1:] or s[i:] == t[i + 1:] or s[i + 1:] == t[i:]:
                    return True
                else:
                    return False

        return True
        '''
        #Replace Part if len is same
        if len(s) == len(t):
            for i in range(max(len(s), len(t))):
                firstString = ''
                secondString = ''
                if i < len(s):
                    firstString = s[i]
                if i < len(t):
                    secondString = t[i]

                if firstString == secondString:
                    continue
                else:
                    diff += 1

            if diff > 1:
                return False
            else:
                return True

        #Insert or Delete Part    
        else:
            i = 0
            j = 0
            while i < len(s) and j < len(t) :
                firstString = ''
                secondString = ''
                #if i < len(s):
                firstString = s[i]
                #if j < len(t):
                secondString = t[j]

                if firstString == secondString:
                    i += 1 
                    j += 1
                    #continue
                else:
                    diff += 1
                    if len(s) < len(t):
                        j += 1
                    else:
                        i +=1 

            #print("diff - ", diff, " :i - ", i, " :j - ", j)
            if diff > 1:
                return False
            else:
                return True
        '''

        '''
        table_values = [ [0 for j in range(len(t)+1)] for i in range(len(s)+1)]

        for i in range(len(s)+1):
            table_values[i][0] = i

        for j in range(len(t)+1):
            table_values[0][j] = j

        for i in range(1, len(s)+1, 1):
            for j in range(1, len(t)+1, 1):
                if s[i-1] == t[j-1]:
                    table_values[i][j] = table_values[i-1][j-1]
                else:
                    table_values[i][j] = min( table_values[i-1][j]
                                             ,table_values[i][j-1]
                                             ,table_values[i-1][j-1] 
                                            ) + 1
        #print(table_values)
        if table_values[len(s)][len(t)] > 1:
            return False
        else:
            return True
        '''
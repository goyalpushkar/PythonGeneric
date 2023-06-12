'''
Given a seven-digit phone number, return all the character combinations that can be generated according to the
following mapping:

Graph

Return the combinations in the lexicographical order.

Example One
{
"phone_number": "1234567"
}
Output:

[
"adgjmp",
"adgjmq",
"adgjmr",
"adgjms",
"adgjnp",
...
"cfilns",
"cfilop",
"cfiloq",
"cfilor",
"cfilos"
]
First string "adgjmp" in the first line comes from the first characters mapped to digits 2, 3, 4, 5, 6 and 7
respectively. Since digit 1 maps to nothing, nothing is appended before 'a'. Similarly, the fifth string "adgjnp"
generated from first characters of 2, 3, 4, 5 second character of 6 and first character of 7. All combinations
generated in such a way must be returned in the lexicographical order.

Example Two
{
"phone_number": "1234567"
}
Output:

[""]
Notes
Return an array of the generated string combinations in the lexicographical order. If nothing can be generated,
return a list with an empty string "".
Digits 0 and 1 map to nothing. Other digits map to either three or four different characters each.

Constraints:
Input string is 7 characters long; each character is a digit.
'''

class Solution:
    def get_words_from_phone_number(phone_number):
        """
        Args:
         phone_number(str)
        Returns:
         list_str
        """
        # Write your code here.
        num_char_map = {0: "", 1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        result = []
        def helper(sol, i):
            if i == 7:
                result.append("".join(elem for elem in sol))
                return
            else:
                if int(phone_number[i]) in (0, 1):
                    sol.append(num_char_map[int(phone_number[i])])
                    helper(sol, i + 1)
                    sol.pop()
                else:
                    for index in range(len(num_char_map[int(phone_number[i])])):
                        sol.append(num_char_map[int(phone_number[i])][index])
                        helper(sol, i + 1)
                        sol.pop()

        # Since digits 0 and 1 map to no characters, remove them from the input string as they have no effect on the output
        # phone_number = phone_number.replace("0", "").replace("1", "")
        # if we remove 0 and 1 then IF condition is not required for 0,1 check

        helper([], 0)
        return result

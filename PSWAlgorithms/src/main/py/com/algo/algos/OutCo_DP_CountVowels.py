'''
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u).

Input: n (Integer)
Output: Integer
Example:
Input: n = 1
Output: 5
Explanation: The strings that consist of vowels only are ["a","e","i","o","u"].

Input: n = 2
Output: 25
Explanation: The 25 strings that consist of vowels are
["aa","ae","ai","ao","au","ea", ee","ei","eo","eu","ia","ie","ii","io","iu","oa","oe","oi",
"oo","ou","ua", "ue", "ui", "uo" "uu"].
Constraints
Time Complexity: O(5^N)

Space Complexity: O(N)
'''
def countVowelStrings(n):
    vowels = ['a','e','i','o','u']


    def helper(build, height, n, final_result):
        if height == n:
            final_result.append(build)
            return final_result

        for elem in vowels:
            final_result = helper(build+elem, height+1, n, final_result)

        return final_result

    final_result = []
    final_result = helper("", 0, n, final_result)
    print(final_result)
    return len(final_result)


if __name__ == '__main__':
    no_of_tests = int(input("No of tests: "))
    # bbabcbcab - 7
    # vtvvv - 4
    # pwnnb - 2
    # ttbtctcbt - 7
    for i in range(no_of_tests):
        input_string = int(input("Enter length for no of vowels: "))
        result = countVowelStrings(input_string)
        # longest_palindrome(input_string)
        print(f"result: {result}")
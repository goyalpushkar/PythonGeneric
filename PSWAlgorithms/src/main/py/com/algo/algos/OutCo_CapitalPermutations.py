'''
Given a string str of lowercase alphabetical characters, return the set of all permutations of those characters in upper
 AND lowercase.

Advanced
Solve the same problem, except now you may have number characters in your string (which don't have a
lowercase or uppercase, but should still be included in your result) and capital letters, that need to be lowercased.

Input: str (String)
Output: [Str] (Array of Strings)
Example
Input: "abc"
Output: ["ABC", "ABc", "AbC", "aBC", "Abc", "aBc", "abC", "abc"]


Advanced:

Input: "A1d3"
Output: ["A1D3", "a1D3", "A1d3", "a1d3"]
Constraints
Time Complexity: O(2^N)
Space Complexity: O(2^N)
The order of the strings in the final result does not matter.

In the basic solution, all the input characters will be lowercase letters.

In the advanced solution, the input characters can be uppercase letters and numbers too.

State Variable - build, depth
base case - Append word to result and return result at Return depth = len(word)
Left case - word[depth-1] as small case
Right case - word[depth-1] as Large case

                                                        abc
                abc                                                                 Abc
        abc              aBc                                              Abc                   ABc
    abc       abC    aBc        aBC                                 Abc         AbC         ABc       ABC


'''

def capital_permutations(word):
    word_length = len(word)
    result = []

    def helper_capital_perm(build, depth, result):

        if depth == word_length:
            result += [build]
            return result

        # Left Case
        build_left = build[0:depth] + build[depth].lower() + build[depth+1:]
        result = helper_capital_perm(build_left, depth+1, result)
        print(f"{('-') * depth} Left result:  {result}")

        # Right Case
        build_right = build[0:depth] + build[depth].upper() + build[depth+1:]
        result = helper_capital_perm(build_right, depth+1, result)
        print(f"{('-') * depth} Right result:  {result}")

        return result

    result = helper_capital_perm(word, 0, result)
    return result


if __name__ == '__main__':
    word = input("Enter level: ")
    final_result = capital_permutations(word)
    print(f"Final Output:\n {final_result}")

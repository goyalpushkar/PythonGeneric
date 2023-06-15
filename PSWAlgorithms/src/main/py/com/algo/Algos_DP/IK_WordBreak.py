'''
Given a string and a dictionary of words, check whether the given string can be broken down into a space-separated sequence of one or more dictionary words.

Example One
{
"s": "helloworldhello",
"words_dictionary": ["world", "hello", "faang"]
}
Output:
1
helloworldhello can be broken down as hello world hello.

Example Two
{
"s": "interviewkickstart",
"words_dictionary": ["interview", "preparation"]
}
Output:
0
Notes
The same word in the dictionary may be used multiple times in the breakdown process.

Constraints:

1 <= length of given string <= 103
1 <= number of words in the dictionary <= 103
1 <= length of each word in the dictionary <= 20
Each string consists of lowercase English alphabets only.
All words in the dictionary are unique.
'''


def word_break(s, words_dictionary):
    """
    Args:
     s(str)
     words_dictionary(list_str)
    Returns:
     bool
    """

    '''
    {
    "s": "dogsilverat",
    "words_dictionary": ["dogs", "silver", "rat"]
    }
    '''
    # Write your code here.
    memo = {}

    def word_rec(index):
        # print(index)

        if index in memo:
            return memo[index]

        if index > len(s):
            return False

        if index == len(s):
            return True

        for word in words_dictionary:
            # print(s, "index: ", index, len(word), "fnd word: ", s[index:index+len(word)], "in word: ", word)
            if s[index:index + len(word)] == word:
                if word_rec(index + len(word)):
                    memo[index] = True
                    return memo[index]

        memo[index] = False
        return memo[index]

    return word_rec(0)


def word_break(s, words_dictionary):
    """
    Args:
     s(str)
     words_dictionary(list_str)
    Returns:
     bool
    """
    # Write your code here.
    n = len(s)
    tab = [False for _ in range(n + 1)]
    tab[n] = True
    word_dict = set(words_dictionary)
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i:j + 1] in word_dict and tab[j + 1]:
                tab[i] = True
                break

    return tab[0]


# Not working for 1 scenario in IK
def word_break(s, words_dictionary):
    """
    Args:
     s(str)
     words_dictionary(list_str)
    Returns:
     bool
    """

    '''
    {
    "s": "dogsilverat",
    "words_dictionary": ["dogs", "silver", "rat"]
    }
    '''
    # Write your code here.
    initial_str = ""
    word_str = ""

    words_dict = set(words_dictionary)

    for index in range(len(s) - 1, -1, -1):
        initial_str = s[index] + initial_str
        word_str = s[index] + word_str
        print(word_str, initial_str)

        if word_str in words_dict or initial_str in words_dict:
            word_str = ""

    print(word_str, initial_str)
    if len(word_str) == 0:
        return True
    else:
        return False
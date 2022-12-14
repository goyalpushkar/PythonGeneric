'''
Powerset
String combinations in the output array must be in the same order as the characters in the intial input string. This
means that for an input of "ab", the out put can be ["","a","ab","b"] but it cannot be ["","a","b","ba"]

abc -  ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']

State Variable - build, depth
base case - Append word to result and return result at Return depth = len(word)
Left case - build as it is
Right case - build + word[depth-1]

                                                        ""
                    ""                                                                      a
         ""                  b                                                    a                    ab
    ""         c        b           bc                                      a           ac      ab              abc
'''


def powerset(word):
    word_length = len(word)
    result = []

    def helper_powerset(build, depth, result):
        # print(f"build: {build}\n"
        #       f"depth: {depth}\n"
        #       f"result: {result}\n"
        #       f"\n")
        if depth == word_length:
            result += [build]
            return result

        # left
        build_left = build
        result = helper_powerset(build_left, depth+1, result)
        print(f"{('-')*depth} Left result:  {result}")

        # right
        build_right = build + word[depth]
        result = helper_powerset(build_right, depth+1, result)
        print(f"{('-')*depth} Right result:  {result}")

        return result

    final_result = helper_powerset("", 0, result)
    return final_result


if __name__ == '__main__':
    user_word = input("Enter word: ")
    final_result = powerset(user_word)
    print(f"Final Output:\n {final_result}")

'''
  File "C:/Users/pgoyal/PyCharmWorkspace/GenericProcessing/algos/OutCo_PowerSet.py", line 26, in helper_powerset
    result += [build]
UnboundLocalError: local variable 'result' referenced before assignment
'''
# def powerset_glob(word):
#     word_length = len(word)
#     global result
#     result = []
#
#     def helper_powerset(build, depth):
#         # print(f"build: {build}\n"
#         #       f"depth: {depth}\n"
#         #       f"result: {result}\n"
#         #       f"\n")
#         if depth == word_length:
#             result += [build]
#             return
#
#         # left
#         build_left = build
#         helper_powerset(build_left, depth+1)
#         print(f"{('-')*depth} Left result:  {result}")
#
#         # right
#         build_right = build + word[depth]
#         helper_powerset(build_right, depth+1)
#         print(f"{('-')*depth} Right result:  {result}")
#
#     final_result = helper_powerset("", 0)
#     return final_result
'''
Given a positive integer n, return an array of all the binary strings of length n that DO NOT contain consecutive 1s.

Input: n (Integer)
Output: [Str] (Array of Strings)
Example
Input: 2
Output: ["00", "01", "10"]

Input: 3
Output: ["000", "001", "010", "100", "101"]

Constraints
Time Complexity: O(2^N)
Auxiliary Space Complexity: O(2^N)

State Variable - build, depth
base case - Append word to result if last two caharcters are not 1s and return result at Return depth = len(word)
Left case - build + "0"
Right case - build + "1"


                                                        ""
                                    "0"                                             "1"
                        "00"                    "01"                     "10"                   "11"
              "000"             "001"    "010"          "011"      "100"        "101"    "110"          "111"


'''


def non_consecutive_ones(n):
    print(n)
    build = ""     # [""]
    result = []

    def get_values(build, height, result):
        print(f"build: {build}\t {len(build)}\n"
              f"height: {height}\n"
              f"result: {result}\n"
              f"\n"
             )
        if n == height:
            if build[len(build)-2:] != "11":
                result += [build] # [build[len(build)-1]]

            return result

        # Go left
        # build_left = build
        build_left = build+"0"   # [len(build)-1]
        result = get_values(build_left, height+1, result)
        print(f"{('-')*height} Left result: {result}\n")

        # Go Right
        # build_right = build
        # if (len(build) > 0):
        #     if (build[len(build)-1] != "1"):
        build_right = build+"1"  # [len(build) - 1]
        # build_right.append(build_right[len(build_right)-1]+"1")
        result = get_values(build_right, height+1, result)
        print(f"{('-')*height} Right result: {result}\n")

        return result

    result = get_values(build, 0, result)

    return result


if __name__ == '__main__':
    n = int(input("Enter level: "))
    final_result = non_consecutive_ones(n)
    print(f"Final Output:\n {final_result}")
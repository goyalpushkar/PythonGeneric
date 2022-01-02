'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
'''


class Solution:
    def binarySum(self, first: str, second: str) -> (str, str):
        if first == "1" and second == "1":
            return ("1", "0")
        elif (first == "1" and second == "0") or (first == "0" and second == "1"):
            return ("0", "1")
        elif first == "0" and second == "0":
            return ("0", "0")

    def addBinary(self, a: str, b: str) -> str:

        minLength = min(len(a), len(b))
        returnString = ""
        prevCarry = "0"
        a = a[::-1]
        b = b[::-1]
        for elem in range(minLength):  # reversed
            (carry, value) = self.binarySum(a[elem], b[elem])
            if prevCarry == "1":
                (carry, value) = self.binarySum(value, prevCarry)
                # print(a[elem], b[elem])
                if a[elem] == "1" and b[elem] == "1":
                    carry = "1"

            returnString += value  # + returnString
            prevCarry = carry
            # print(returnString, prevCarry)

        if len(a) - minLength == 0 and len(b) - minLength == 0:
            if prevCarry == "1":
                returnString += prevCarry  # + returnString

        if len(a) - minLength > 0:
            for index in range(minLength, len(a), 1):  # reversed
                (carry, value) = self.binarySum(a[index], prevCarry)
                returnString += value  # + returnString
                prevCarry = carry

            if carry == "1":
                returnString += carry  # + returnString

        if len(b) - minLength > 0:
            for index in range(minLength, len(b), 1):  # reversed
                (carry, value) = self.binarySum(b[index], prevCarry)
                returnString += value  # + returnString
                prevCarry = carry

            if carry == "1":
                returnString += carry  # + returnString

        return returnString[::-1]

    def addBinary(self, a: str, b: str) -> str:
        sum = int(a, 2) + int(b, 2)
        return bin(sum)[2:]
'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''


class Solution:
    import math

    def __init__(self):
        self.dictNum = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                        9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                        16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty',
                        40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety',
                        100: 'Hundred', 1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion'}

    def get3Digits(self, num: int) -> str:
        returnString = ""

        remainder = num % 100
        hundredsPlace = num // 100
        # print(hundredsPlace)
        hundredWords = self.dictNum.get(hundredsPlace, 'minus')
        if hundredWords != 'minus':
            returnString += hundredWords + ' Hundred '

        # print(returnString)
        words = self.dictNum.get(remainder, 'minus')

        # Number not found
        if words == 'minus':
            unitPlace = remainder % 10
            unitWords = self.dictNum.get(unitPlace, 'minus')

            tensPlace = remainder - unitPlace
            tensWords = self.dictNum.get(tensPlace, 'minus')

            if tensWords != 'minus':
                returnString += tensWords + " "

            if unitWords != 'minus':
                returnString += unitWords

        else:
            returnString += words

        # print(len(returnString))
        return returnString.strip()

    def numberToWords(self, num: int) -> str:
        quotient = num
        finalWord = ""
        looped = 0

        if quotient == 0:
            return "Zero"

        while quotient > 0:
            remainder = quotient % 1000
            quotient = quotient // 1000
            returnWord = self.get3Digits(remainder)
            # print(returnWord)
            if looped == 0 and returnWord != "":
                finalWord = returnWord  # + " " + finalWord
            if looped == 1 and returnWord != "":
                finalWord = returnWord + " Thousand " + finalWord
            if looped == 2 and returnWord != "":
                finalWord = returnWord + " Million " + finalWord
            if looped == 3 and returnWord != "":
                finalWord = returnWord + " Billion " + finalWord
            if looped == 4 and returnWord != "":
                finalWord = returnWord + " Trillion " + finalWord

            looped += 1

        return finalWord.strip()
'''
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess,
you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong
 position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows.
 Note that both secret and guess may contain duplicate digits.



Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
 _ __
Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
   _              _
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be
rearranged to allow one 1 to be a bull.


Constraints:

1 <= secret.length, guess.length <= 1000
secret.length == guess.length
secret and guess consist of digits only.


Naive -
    do a loop to compare a digit from both words:
        compare the current digit for both numbers if they are same, increment bull
            else put digit from secret to a dict with count and
                 check if digit from the guess in dict then increment cow and decrement count from dict
        move to the next

    # Problem 1 -> If a mismatched digit came later from the secret and digit from guess is already checked then
    # it will not be marked in the cow

'''
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cows = 0
        bulls = 0
        mismatched_sec = {}
        mismatched_guess = {}

        len_range = len(str(secret))
        secret = int(secret)
        guess = int(guess)
        # for index in range(len(str(secret_iter))):
        #     sec_value = secret_iter % 10
        #     mismatched[sec_value] = mismatched.get(sec_value, 0) + 1
        #     secret_iter = (secret_iter - sec_value) // 10

        # for index in range(len_range):
        for sec_value, guess_value in zip(secret, guess):
            # sec_value = secret % 10
            # guess_value = guess % 10
            if sec_value == guess_value:
                bulls += 1
                # mismatched_sec[sec_value] -= 1
            else:
                # mismatched_sec[sec_value] = mismatched_sec.get(sec_value, 0) + 1
                # mismatched_guess[guess_value] = mismatched_guess.get(guess_value, 0) + 1
                if guess_value in mismatched_sec.keys() and mismatched_sec[guess_value] > 0:
                    cows += 1
                    mismatched_sec[guess_value] -= 1
                else:
                    mismatched_guess[guess_value] = mismatched_guess.get(guess_value, 0) + 1

                if sec_value in mismatched_guess.keys() and mismatched_guess[sec_value] > 0:
                    cows += 1
                    mismatched_guess[sec_value] -= 1
                else:
                    mismatched_sec[sec_value] = mismatched_sec.get(sec_value, 0) + 1

            # secret = (secret - sec_value ) // 10
            # guess = (guess - guess_value) // 10
            print(f"mismatched_sec: {mismatched_sec}\n"
                  f"mismatched_guess: {mismatched_guess}\n"
                  f"secret: {secret}\n"
                  f"guess: {guess}")

        return str(bulls)+"A"+str(cows)+"B"



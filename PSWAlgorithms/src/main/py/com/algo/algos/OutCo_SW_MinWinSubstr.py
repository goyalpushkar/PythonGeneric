'''
Given a string and set of characters return the substring representing the Smallest window containing those characters
Input: fullString{String}
       chars {String}
Output: {String}

Example1 -
Input - "ADOBECODEBANC", "ABC"
Output - "BANC" (BANC is the shortest containing all the characters)


Input - "HELLO WORLD", "FOO"
Output - ""

Extra - How will you handle repeat chars - if two A characters are given, a valid window must contain 2 As
'''
def minimumWindowSubstring(fullString, chars):
    # Write your code here
    search_chars = len(chars)
    missing_dict = {}
    start = 0
    end = 0
    min_length = len(fullString) + 1
    return_value = ""
    for chr in chars:
        if chr in missing_dict:
            missing_dict[chr] += 1
        else:
            missing_dict[chr] = 1

    # Hunting
    while end <= len(fullString)-1:
        # print(f"1. start: {start}\tend:{end}\tsearch_chars:{search_chars}\tmin_length:{min_length}\tCurrent Char:{fullString[end]}")
        # print(missing_dict)
        if search_chars > 0:
            if fullString[end] in missing_dict:
                missing_dict[fullString[end]] -= 1
                if missing_dict[fullString[end]] >= 0:
                    search_chars -= 1

        # print(f"2. start: {start}\tend:{end}\tsearch_chars:{search_chars}\tmin_length:{min_length}")
        # Catching
        while search_chars == 0:
            length = end - start + 1
            # print(f"length:{length}\tmin_length:{min_length}")
            if length < min_length:
                return_value = fullString[start:end+1]
                min_length = length

            if fullString[start] in missing_dict:
                missing_dict[fullString[start]] += 1
                if missing_dict[fullString[start]] > 0:
                    search_chars += 1
            # print(f"return_value:{return_value}\tmin_length:{min_length}")
            start += 1

        # print(f"3. start: {start}\tend:{end}\tsearch_chars:{search_chars}\tmin_length:{min_length}\n\n")
        end += 1

    return return_value

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fullString = input("Enter Full String: ")
    chars = input("Enter Search String: ")

    result = minimumWindowSubstring(fullString, chars)
    print(f"result: {result}")

    # fptr.write(result + '\n')
    # fptr.close()
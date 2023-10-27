'''
Given a dictionary of words and a string txt, find the number of ways the string can be broken down into the dictionary words. Return the answer modulo 109 + 7.

Example
{
"dictionary": ["kick", "start", "kickstart", "is", "awe", "some", "awesome"],
"txt": "kickstartisawesome"
}
Output:

4
Here are all four ways to break down the string into the dictionary words:

kick start is awe some
kick start is awesome
kickstart is awe some
kickstart is awesome
4 % 1000000007 = 4 so the correct output is 4.

Notes
Constraints:

1 <= number of words in the dictionary <= 2 * 105
1 <= length of any dictionary word <= 102
1 <= length of the string txt <= 2 * 103
Dictionary words and the string txt all consist of lowercase latin characters only (no whitespace, in particular).
'''

def word_break_count(dictionary, txt):
    """
    Args:
    dictionary(list_str)
    txt(str)
    Returns:
    int32
    """
    # Write your code here.
    # mem = [-1 for i in range(len(txt))]
    dict_set = set(dictionary)
    mod = pow(10, 9) + 7
    mem = {}

    def dfs(idx, prefix):
        # print(f"idx: {idx}, prefix: {prefix}")
        if idx in mem:
            return mem[idx]
            
        if idx == len(txt):
            return 1
            
        result = 0
        curr_txt = ""
        for i in range(idx, len(txt)):
            curr_txt += txt[i]
            
            if curr_txt in dict_set:
                result += dfs(i+1, prefix+curr_txt)
                
        mem[idx] = result % mod
        
        return mem[idx]
    
    final_result = dfs(0, "")
    # print(f"mem: {mem}")
    
    return final_result
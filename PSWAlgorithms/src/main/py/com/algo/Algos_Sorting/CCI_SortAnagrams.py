'''
Write a method to sort an array of strings so that all the anagrams are next to each other.
'''

from functools import cmp_to_key

def mycomparator(a, b):
    return sort_strings(a) > sort_strings(b)

def sort_strings(str):
    return "".join(sorted(list(str)))

    '''newStr = ""
    for elem in sorted_array:
        newStr += elem

    return  newStr
    '''
def sort_array(arr1):
    #return sorted(arr1, key=lambda word: ''.join(sorted(word.replace(" ", "").lower())))
    return sorted(arr1, key=sort_strings)  #cmp_to_key(mycomparator)

#abets mates baste meats  betas beast  steam  tames  beats  teams -> abets baste betas beast beats mates meats steam tames teams
if __name__ == '__main__':
    arr1 = list( map(str, input("Array of Strings: ").strip().split()) )

    final_arr = sort_array(arr1)

    for index in range(len(final_arr)):
        print( final_arr[index], end=" ")
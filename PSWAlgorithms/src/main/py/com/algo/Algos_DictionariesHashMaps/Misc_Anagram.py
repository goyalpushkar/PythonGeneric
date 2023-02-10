'''
Created on Jan 23, 2020

@author: goyalpushkar
'''
from collections import Counter

def anagramSolution1(s1, s2):
    second_list = list(s2)
    
    pos1 = 0
    still_ok = True 
    
    if ( len(s1) != len(s2) ):
        return False
   
    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(second_list) and not found:
            if s1[pos1] == second_list[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
                
        if found:
            second_list[pos2] = None
        else:  
            still_ok = False
            
        pos1 = pos1 + 1
        #print( pos1 )
        #print(still_ok)
    return still_ok

def anagramSolution2(s1, s2): 
    first_list = list(s1)
    second_list = list(s2)
    
    first_list.sort()
    second_list.sort()
    
    if ( len(s1) != len(s2) ):
        return False
    
    #print(first_list)
    #print(second_list)
    pos = 0
    matches = True
    while pos < len(first_list) and matches:
        if first_list[pos] == second_list[pos]:
            pos = pos + 1
        else:
            matches = False
        #print(pos)
    return matches

def anagramSolution3(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    
    for i in range( len(s1) ):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range( len(s2) ):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
        
    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False
    return still_ok

def anagramSolution4(s1, s2):
    
    counter = {}
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')
    
    for letter in s1:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
            
    for letter in s2:
        if letter in counter:
            counter[letter] -= 1
        else:
            counter[letter] = 1
            
    for k in counter:
        if counter[k] != 0:
            return False
        
    return True

def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

def isAnagram(self, s: str, t: str) -> bool:
    ana_dict = {}
    for elem in s:
        ana_dict[elem] = ana_dict.get(elem, 0) + 1

    for elem in t:
        ana_dict[elem] = ana_dict.get(elem, 0) - 1

    for key in ana_dict.keys():
        if ana_dict[key] != 0:
            return False

    return True

if __name__ == '__main__':
    print(anagramSolution2('abcd','bdca'))        
    print(anagramSolution4('abcd','bdca'))    
    print(anagramSolution4('clint eastwood','old west action'))     
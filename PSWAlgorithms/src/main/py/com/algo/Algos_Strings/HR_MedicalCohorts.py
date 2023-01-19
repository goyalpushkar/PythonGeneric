#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solution' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY illnesses
#  2. STRING_ARRAY drugs
#  3. STRING_ARRAY cohorts
#
# patient1 => melanoma
# patient2 => glibo
# patient3=>melanoma
# {m:p1,p3,g:p2} # Use illnessess to convert to a dictionary
# (d1:p1,p2,p3,d2:p3)# Use drugs to convert to a dictionary
# [p1,p3],[p2],[p3]
def solution(illnesses, drugs, cohorts):
    # Write your code here
    print('illnesses:', illnesses)
    print('drugs:', drugs)
    print('cohorts:', cohorts)

    def intersection(lst1, lst2):
        print('lst1:',lst1)
        print('lst2:', lst2)
        if len(lst1) == 0:
            return lst2
        temp = set(lst2)
        lst3 = [value for value in lst1 if value in temp]
        print('lst3:', lst3)
        return lst3

    result = []
    illdict = {}
    for i in illnesses:
        i = i.split(", ")
        print('i:',i)
        if i[1] not in illdict:
            illdict[i[1]] = [i[0]]
        else:
            illdict[i[1]].append(i[0])
    print('illdict:', illdict)
    drugdict = {}
    for d in drugs:
        d = d.split(", ")
        if d[1] not in drugdict:
            drugdict[d[1]] = [d[0]]
        else:
            drugdict[d[1]].append(d[0])
    print('drugdict:', drugdict)
    for c in cohorts:
        c = c.split(", ")
        illpatients = []
        lst1 = []
        lst2 = []
        print('c',c)
        for v in c:
            #v = v.split(", ")
            print('v', v)
            if v in illdict:
                #lst1.extend(illdict[v])  # [p1,p3]
                lst1 = intersection(lst1,illdict[v])
            if v in drugdict:
                lst1 = intersection(lst1,drugdict[v])  # [p1,p2,p3]
        #illpatients = intersection(lst1, lst2)
        lst1 = sorted(lst1)
        lst1 = ", ".join(lst1)
        # result.append(str(sorted(lst1)))
        result.append(str(lst1))
    print(result)
    print("List in proper method", '[%s]' % ', '.join(map(str, result)))
    print('\n'.join(result))
    print('\n')

illnesses= ['patient1, melanoma', 'patient2, glioblastoma', 'patient3, melanoma']
drugs= ['patient1, drug1', 'patient2, drug1', 'patient3, drug2', 'patient3, drug1']
cohorts= ['melanoma, drug1', 'drug1, glioblastoma', 'melanoma, drug1, drug2']

solution(illnesses, drugs, cohorts)
'''if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    illnesses_count = int(input().strip())

    illnesses = []

    for _ in range(illnesses_count):
        illnesses_item = input()
        illnesses.append(illnesses_item)

    drugs_count = int(input().strip())

    drugs = []

    for _ in range(drugs_count):
        drugs_item = input()
        drugs.append(drugs_item)

    cohorts_count = int(input().strip())

    cohorts = []

    for _ in range(cohorts_count):
        cohorts_item = input()
        cohorts.append(cohorts_item)

    result = solution(illnesses, drugs, cohorts)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()'''
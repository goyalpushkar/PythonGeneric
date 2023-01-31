'''
Given a positive integer n, return the nth Power Number.

A Power Number is a positive integer i that can be written as two positive integers x and y where i = x^y and x > 1
 and y > 1.

So for example:

The number 4 is a power number, because 4 == 2^2. The number 25 is a power number, because 25 == 5^2. The number 8 is
a power number, because 8 == 2^3. The number 7 is NOT a power number, because it can't be written as some number
squared, cubed, etc.

Your goal is to return the nth power number. Meaning, if you were to sort all power numbers in ascending order, there
 would be a first, second, third... nth.

Here is a list of the first 10 power numbers: [4, 8, 9, 16, 25, 27, 32, 36, 49, 64]

Input: n, Integer
Output: Integer
Example
In: 1
Out: 4

In: 10
Out: 64
Constraints
Time Complexity: O(N)
Auxiliary Space Complexity: O(N)
n will always be greater than or equal to 1.

There may be some power numbers that can be produced in multiple ways (ie 16 is 2^4 or 4^2). You should only count
 those once.

Hints for Interviewer
Create a list by hand of the first 10 or 20 power numbers.

Think about what the smallest power you can raise some integer to (2).

Think about how you can use that information to set a MAXIMUM RANGE on what the nth power number could be.

For example, if you computed the first 10 squares (powers of 2), you'd get 2-11 squared.

Now you have 10 valid power numbers, but 121 (11 squared) is going to be larger than the nth power number,
because we haven't taken into account powers of 3, 4, 5...

Think about where a heap might fit into all this.

https://www.geeksforgeeks.org/check-if-a-number-can-be-expressed-as-xy-x-raised-to-power-y/

https://www.geeksforgeeks.org/check-if-a-number-can-be-expressed-as-ab-set-2/

'''
import math
import heapq

class Solution:
    def nth_power_num_long(self, n):
        # limit = math.sqrt(n)

        # nth power number will be at max square of (n+1) e.g. 10th power number at max will be 11^2 = 121
        limit = pow((n+1),2)
        num_list = set()
        for i in range(2, n+2):
            for po in range(2,100):
                numb = pow(i, po)
                if numb < limit:
                    num_list.add(numb)
                else:
                    break

        # num_list = set(num_list)
        num_list = sorted(num_list)

        return num_list[:n], num_list[n-1]

    '''
        Get max value that n can reach to i.e. if all squares are considered starting from 2 to n+1. e.g. 10 numbers can
        be 2^2 = 4 to 11^2 = 121 if all squares are the only numbers
        first take all squares and insert them into set and a max heap
        take next higher powers like 3, 4, etc. and if next higher power is smaller then max element in heap and not in 
        the set then remove max element from heap and add this new element
        
    '''
    def nth_power_num(self, n):
        # limit = pow((n + 1), 2)
        num_list = set()
        max_heap = []

        po = 2
        for i in range(2, n+2):
            value = pow(i, po)
            num_list.add(value)
            heapq.heappush(max_heap, -value)

        # print(f"num_list: {num_list}\n"
        #       f"max_heap: {max_heap}")

        po = 3
        i = 2
        # index = 1
        # for i in range(2, n + 1):
        while i <= n+1:  # and index < 12
            value = pow(i, po)
            # print(f"i: {i}, po: {po}, value: {value}")

            # Check if value not exists in the set and smaller than max element then remove top element from heap
            # and add it to heap
            # if value not in num_list and value < heap(max_heap):

            if value < -max_heap[0]:
                if value not in num_list:
                    remove_elem = heapq.heappop(max_heap)
                    heapq.heappush(max_heap, -value)
                    num_list.add(value)
                i += 1
            else:
                # if max power of 2 is more than the max heap elements then return
                if i == 2:
                    break
                po += 1
                i = 2

            # index +=1
            # print(f"num_list: {num_list}\n"
            #       f"max_heap: {max_heap}")

        return [-1*elem for elem in max_heap], -1*max_heap[0]

    '''
        Check if number can be written as nth power as x^y 
        T - O(sqrt(n)
        S - O(1)
    '''
    def check_nthpower(self, n):
        # n = x^y take log
        # log n = y log x => y = log n / log x

        for x in range(2, int(math.sqrt(n)) + 1):
            value = math.log2(n) / math.log2(x)

            # if value is an integer or a number with decimal places upto 8 zeroes
            if math.round(value - int(value), 8) < .00000001:
                return True

        return False



if __name__ == '__main__':
    test_cases = int(input("Enter no of test cases: "))
    for i in range(test_cases):
        n = int(input("Enter number nth power number: "))
        sol = Solution()
        result = sol.nth_power_num_long(n)
        print(f"Long result: {result}")

        result = sol.nth_power_num(n)
        print(f"result: {result}")

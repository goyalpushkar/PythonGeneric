'''
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to  the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.
Given the number of trailing days  and a client's total daily expenditures for a period of  days, find and print the number of times the client will receive a notification over all  days.
For example,  and . On the first three days, they just collect spending data. At day , we have trailing expenditures of . The median is  and the day's expenditure is . Because , there will be a notice. The next day, our trailing expenditures are  and the expenditures are . This is less than  so no notice will be sent. Over the period, there was one notice sent.
Note: The median of a list of numbers can be found by arranging all the numbers from smallest to greatest. If there is an odd number of numbers, the middle one is picked. If there is an even number of numbers, median is then defined to be the average of the two middle values. (Wikipedia)
Function Description
Complete the function activityNotifications in the editor below. It must return an integer representing the number of client notifications.
activityNotifications has the following parameter(s):
expenditure: an array of integers representing daily expenditures
d: an integer, the lookback days for median spending
Input Format
The first line contains two space-separated integers  and , the number of days of transaction data, and the number of trailing days' data used to calculate median spending.
The second line contains  space-separated non-negative integers where each integer  denotes .
Constraints



Output Format
Print an integer denoting the total number of times the client receives a notification over a period of  days.
Sample Input 0
9 5
2 3 4 2 3 6 8 4 5
Sample Output 0
2
Explanation 0
We must determine the total number of  the client receives over a period of  days. For the first five days, the customer receives no notifications because the bank has insufficient transaction data: .
On the sixth day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which triggers a notification because : .
On the seventh day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which triggers a notification because :  .
On the eighth day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which does not trigger a notification because : .
On the ninth day, the bank has  days of prior transaction data, , and a transaction median of  dollars. The client spends  dollars, which does not trigger a notification because : .
Sample Input 1
5 4
1 2 3 4 4
Sample Output 1
0
There are  days of data required so the first day a notice might go out is day . Our trailing expenditures are  with a median of  The client spends  which is less than  so no notification is sent.
'''
import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
import queue
import math
def activityNotifications(expenditure, d):
    queueOfElems = queue.Queue(0)
    sortedCount = [0 for i in range(201)]
    #total_sum = 0  #This can be used if it would have been an average
    number_of_notifications = 0

    if d % 2 == 0:
        median_position = d // 2
        average_yn = "Y"
    else:
        median_position = d // 2 + 1
        average_yn = "N"

    #print(median_position)
    #print(average_yn)
    for elem in range(0, d):
        queueOfElems.put(expenditure[elem])
        sortedCount[expenditure[elem]] += 1
        #total_sum += expenditure[elem]

    print(sortedCount)
    for elem in range(d, len(expenditure)):
        #median = total_sum / d
        median = get_median_value(sortedCount,median_position,average_yn)
        print(median)
        if expenditure[elem] >= median * 2:
            number_of_notifications += 1

        #total_sum -= queueOfElems.get()
        #total_sum += expenditure[elem]
        sortedCount[queueOfElems.get()] -= 1
        sortedCount[expenditure[elem]] += 1
        queueOfElems.put(expenditure[elem])

    return number_of_notifications

def get_median_value(sortedCount,median_position,average_yn):
    median = 0
    sum = 0
    median_low = -1
    median_high = -1
    for elem in range(len(sortedCount)):
        sum += sortedCount[elem]
        #median_low = elem
        #print("Sum and Median Position")
        #print(sum)
        #print(median_position)
        #print(elem)
        if sum >= median_position:
            if average_yn == "N":
                median = elem
                break
            else:
                if median_low == -1:
                    median_low = elem

                if sum >= median_position + 1:
                    median_high = elem
                    median = (median_high + median_low) / 2
                    break

    return median


def activityNotifications_new(expenditure, d):
    sorted_queue = queue.Queue(0)
    sorted_array = [0 for i in range(201)]
    number_of_notifications = 0
    median_low = (d // 2) + 1
    median_high = (d // 2) + 1

    if d % 2 == 0:  # Even
        median_low = d // 2

    for index in range(0, len(expenditure)):

        if index >= d:
            median_spending = get_median(sorted_array, median_low, median_high)
            if (2 * median_spending) <= expenditure[index]:
                number_of_notifications += 1

            removed_value = sorted_queue.get()
            sorted_array[removed_value] -= 1

        sorted_queue.put(expenditure[index])
        sorted_array[expenditure[index]] += 1

    return number_of_notifications


def get_median(sorted_array, median_low, median_high):
    low_value = 0
    high_value = 0
    low_found = 0
    sum = 0
    for elem in range(len(sorted_array)):
        sum += sorted_array[elem]

        if sum >= median_low and low_found == 0:
            low_value = elem
            low_found = 1

        if sum >= median_high:
            high_value = elem
            break

    median_value = (low_value + high_value) / 2

    return median_value

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input("Total Number of days and number of days transaction data - ").split()

    n = int(nd[0])
    d = int(nd[1])
    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)
    print(str(result) + '\n')
    #fptr.write(str(result) + '\n')
    #fptr.close()

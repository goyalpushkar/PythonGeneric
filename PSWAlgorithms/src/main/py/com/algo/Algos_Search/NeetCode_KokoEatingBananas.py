'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas
from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas
during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:

1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9

'''
class Solution:

    def minEatingSpeed(self, piles, h):
        import math

        def get_total_hours(mid):
            sum = 0
            for pile in piles:
                sum += math.ceil(pile / mid)

            return sum


        # def find_min_in_range(min_val, max_val, h):
        #
        #     mid = math.floor(max_val - (max_val - min_val) / 2)
        #     min_hrs = get_total_hours(mid)
        #
        #     # print(f"min_val: {min_val} max_val: {max_val} mid: {mid} min_hrs: {min_hrs}")
        #     if min_hrs == h:
        #         while mid > min_val and min_hrs == h:
        #             mid -= 1
        #             min_hrs = get_total_hours(mid)
        #
        #         return mid if min_hrs == h else mid + 1
        #     elif min_hrs > h:
        #         if mid+1 > max_val:
        #             return mid+1
        #         return find_min_in_range(mid+1, max_val, h)
        #     else:
        #         if min_val > mid-1:
        #             return mid-1
        #         return find_min_in_range(min_val, mid-1, h)

        def find_min_in_range(min_val, max_val, h):
            while min_val <= max_val:
                mid = math.floor(max_val - (max_val - min_val) / 2)
                min_hrs = get_total_hours(mid)
                print(f"min_val: {min_val} max_val: {max_val} mid: {mid} min_hrs: {min_hrs}")

                # search on left space if calculated hours are less than target
                if min_hrs <= h:
                    min_val = min(min_val, mid)
                    max_val = mid - 1
                else:
                    min_val = mid + 1
                    max_val = max(mid, max_val)

            return min_val

        n = len(piles)
        piles = sorted(piles)
        print(f"n: {n}")
        if n == h:
            return max(piles)
        elif n > h:
            return -1   # not possible
        else:
            q = h // n
            r = h % n

            min_val = math.ceil(piles[0] / q)
            max_val = math.ceil(piles[-1] / q)
            print(f"min_val: {min_val}\n"
                  f"max_val: {max_val}\n"
                  f"piles[-r]: {piles[-r]} piles[-1]: {piles[-1]} q:{q} r: {r}")

            # 34392671, 891616382, 813261297  - 712127987
            # if r != 0:
            #     min_val = math.ceil(piles[-r] / (q+1))
            #     # max_val = math.ceil(piles[-1] / (q+1))
            #     print(f"min_val: {min_val}\n"
            #           f"max_val: {max_val}")
                # if piles[-(r+1)] >= min_val:
                #     return piles[-(r+1)]

            # print(f"min_val: {min_val}\n"
            #       f"max_val: {max_val}")
            return find_min_in_range(min_val, max_val, h)



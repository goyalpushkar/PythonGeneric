'''
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next
(i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit
once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique


Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.


Constraints:
n == gas.length == cost.length
1 <= n <= 105
0 <= gas[i], cost[i] <= 104
'''
class Solution:
    def canCompleteCircuit(self, gas, cost):
        # Sum of Gas should be >= Sum of cost
        if sum(gas) < sum(cost):
            return -1

        # Keep adding gas - cost in total if total is negative then reset total to 0
        res = 0
        total = 0
        for index in range(len(gas)):
            total += gas[index] - cost[index]
            if total < 0:
                total = 0
                res = index + 1

        return res

    # 31/39 passed [5,5,1,3,4] [8,1,7,1,1]
    def canCompleteCircuit(self, gas, cost):
        # 1. Calculate the tank value at each index. If tank >= 0 and gas cost at that point is higher than cost
        # then save this tank value in an array for each index otherwise keep tank as -1
        # 2. Find the index where tank has max value and use that index as starting point
        # 3. Check if circle can be completed starting from that index.
        tank_val = []
        n = len(gas)
        for index in range(len(gas)):
            # if index == 0:
            #     tank = gas[index] # + gas[(start_index+1)%n] - cost[start_index]
            # else:
            #     tank = tank + gas[index] - cost[index-1]
            tank = gas[index] + gas[(index + 1) % n] - cost[index]

            if tank >= 0 and gas[index] >= cost[index]:
                tank_val.append(tank)
            else:
                tank_val.append(-1)

        print(tank_val)
        # tank_val = sorted(tank_val)
        max_val = -1
        max_index = -1
        for index in range(len(tank_val)):
            if max_val < tank_val[index]:
                max_index = index
                max_val = tank_val[index]
                # break

        if max_index == -1:
            return -1

        start_index = max_index
        tank = -1
        for index in range(len(gas)):
            start_index = start_index % n
            # For first time
            if tank == -1:
                tank = gas[start_index]  # + gas[(start_index+1)%n] - cost[start_index]
            else:
                tank = tank + gas[start_index] - cost[start_index - 1]

            print(f"start_index: {start_index} tank: {tank}")
            if tank >= 0 and tank >= cost[start_index]:
                start_index += 1
                continue
            else:
                return -1

        return max_index
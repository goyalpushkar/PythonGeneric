'''
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a
 different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of
 time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

Constraints:
1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].

'''
import heapq
from collections import Counter, deque
class Solution:

    # beats 15.12% 782 ms
    def leastInterval_standard(self, tasks, n):
        task_count = Counter(tasks)
        heap_arr = [-v for k, v in task_count.items()]
        # print(f"task_count first: {task_count} heap_arr: {heap_arr}")

        # Create a heap on the values of dict
        heapq.heapify(heap_arr)
        # print(f"heap_arr first: {heap_arr}")

        count_time = 0
        extracted_elems = deque()
        # loop over heap until empty
        while len(heap_arr) > 0 or len(extracted_elems) > 0:
            count_time += 1

            # get top elem, place in a new array
            if len(heap_arr) > 0:
                elem = heapq.heappop(heap_arr)
                new_num = elem + 1
                # print(f"elem: {elem} new_num: {new_num} count_time: {count_time}\n"
                #       f"heap_arr extract: {heap_arr}")

                # put elem in the seq, increment counter
                if new_num < 0:
                    extracted_elems.append([new_num, count_time + n])

            if extracted_elems and extracted_elems[0][1] == count_time:
                heapq.heappush(heap_arr, extracted_elems.popleft()[0])


        # return count time
        return count_time

    # Mathematical Way - 425ms
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n

        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)

    # Mathematical Way - 406 ms
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        max_freq = max(freqs.values())
        count = 0
        for freq in freqs.values():
            if freq == max_freq:
                count += 1

        return max(len(tasks), max_freq + (max_freq - 1) * n + count - 1)

    # With custom heap
    def leastInterval(self, tasks, n):
        task_count = Counter(tasks)
        heap_arr = [str(v) + "_" + str(k) for k, v in task_count.items()]
        # print(f"task_count first: {task_count} heap_arr: {heap_arr}")

        # Create a heap on the values of dict
        self.heapify(heap_arr)
        # print(f"heap_arr first: {heap_arr}")

        count_time = 0
        extracted_elems = deque()
        # loop over heap until empty
        while len(heap_arr) > 0 or len(extracted_elems) > 0:
            count_time += 1

            # get top elem, place in a new array
            if len(heap_arr) > 0:
                elem, heap_arr = self.extract_max(heap_arr)
                dict_val = elem.split("_")
                new_num = int(dict_val[0])-1
                new_val = str(new_num) + "_" + dict_val[1]
                # print(f"elem: {elem} new_val: {new_val} new_num: {new_num}\n"
                #       f"heap_arr extract: {heap_arr}")

                # put elem in the seq, increment counter
                if new_num > 0:
                    extracted_elems.append([new_val, count_time+n])

            if extracted_elems and extracted_elems[0][1] == count_time:
                heap_arr.append(extracted_elems.popleft()[0])
                self.heapify(heap_arr)

        # return count time
        return count_time

    # 57/71 passed
    def leastInterval_self(self, tasks, n):
        task_count = Counter(tasks)
        heap_arr = [str(v) + "_" + str(k) for k, v in task_count.items()]

        # Create a heap on the values of dict
        self.heapify(heap_arr)
        print(f"heap_arr first: {heap_arr}")

        count_time = 0
        extracted_elems = deque()
        # loop over heap until empty
        while len(heap_arr) > 0:
            idle_limit = n

            # get top elem, place in a new array
            elem, heap_arr = self.extract_max(heap_arr)

            dict_val = elem.split("_")
            new_num = int(dict_val[0])-1
            new_val = str(new_num) + "_" + dict_val[1]
            print(f"elem: {elem} new_val: {new_val} new_num: {new_num}")
            count_time += 1

            # put elem in the seq, increment counter
            if new_num > 0:
                extracted_elems.append([new_val, count_time+idle_limit])

            # while n != 0:
            while idle_limit > 0 and len(extracted_elems) > 0:
                print(f"heap_arr inside idle_time loop: {heap_arr}\t count_time:{count_time}")
                count_time += 1
                # decrement n
                idle_limit -= 1

                # check if heap is not empty then get next elem, place it in the same array
                if len(heap_arr) > 0:
                    sec_elem, heap_arr = self.extract_max(heap_arr)
                    dict_val = sec_elem.split("_")
                    new_num = int(dict_val[0]) - 1
                    new_val = str(new_num) + "_" + dict_val[1]
                    print(f"sec_elem: {sec_elem} new_val: {new_val} new_num: {new_num}")
                    if new_num > 0:
                        extracted_elems.append([new_val, count_time+idle_limit])
                # else add idle time until n becomes 0


            # Push new array into heap
            heap_arr += extracted_elems
            self.heapify(heap_arr)
            print(f"heap_arr: {heap_arr} \t count_time: {count_time}")


        # return count
        return count_time

    def get_child(self, arr, index, limit=None):
        if limit is None:
            limit = len(arr)
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child >= limit:
            return left_child
        elif right_child >= limit:
            return left_child
        elif arr[right_child] <= arr[left_child]:
            return left_child
        else:
            return right_child

    def bubble_down(self, arr, index, limit=None):
        if limit is None:
            limit = len(arr)

        # print(f"bubble_down: arr: {arr} index: {index} limit: {limit}")
        while index < limit:
            child = self.get_child(arr, index, limit)
            # print(f"bubble_down: child: {child} ")
            if child < limit and arr[child] > arr[index]:
                arr[child], arr[index] = arr[index], arr[child]
            else:
                break

            index = child

    def heapify(self, arr):
        index = len(arr) - 1
        while index >= 0:
            self.bubble_down(arr, index)
            index -= 1

    def extract_max(self, arr, limit=None):
        if limit is None:
            limit = len(arr)

        last_elem = limit - 1
        arr[last_elem], arr[0] = arr[0], arr[last_elem]
        self.bubble_down(arr, 0, last_elem)

        return_elem = arr[last_elem]
        arr = arr[:-1]

        return return_elem, arr
'''
Given k linked lists where each one is sorted in the ascending order, merge all of them into a single sorted
 linked list.

Example
{
"lists": [
[1, 3, 5],
[3, 4],
[7]
]
}
Output:

[1, 3, 3, 4, 5, 7]
Notes
Constraints:

0 <= k <= 104
0 <= length of any given linked list <= 103
-109 <= node values <= 109
Sum of the lengths of all given lists won't exceed 105.
'''

    '''
        {
        "lists": [
        [],
        [],
        [],
        [],
        []
        ]
        }

        {
            "lists": [
            [1, 13, 22, 23],
            [2, 12, 14],
            [3, 11, 15, 21],
            [4, 10, 16],
            [5, 9, 17, 20],
            [6, 8, 18],
            [7, 19]
            ]
            }

    '''
# T - O(n log k) S - O(1)
def merge_k_lists(lists):
    # def merge_lists(list1, list2):
    #     index_1 = 0
    #     index_2 = 0
    #     len_1 = len(list1)
    #     len_2 = len(list2)
    #     new_list = []
    #     while index_1 < len_1 or index_2 < len_2:
    #         if index_1 < len_1 and index_2 < len_2 and list1[index_1] < list2[index_2]:
    #             new_list.append(list1[index_1])
    #         elif index_1 < len_1 and index_2 < len_2 and list1[index_1] > list2[index_2]:
    #             new_list.append(list2[index_2])
    #         elif index_1 >= len_1:
    #             while index_2 < len_2:
    #                 new_list.append(list2[index_2])
    #         elif index_2 >= len_2:
    #             while index_1 < len_1:
    #                 new_list.append(list1[index_1])
    #
    #     return new_list

    def merge_lists(list1, list2):

        return_node = LinkedListNode("Dummy")
        new_list = return_node

        while list1 or list2:
            if list1 and list2 and list1.value <= list2.value:
                # print(list1.value, list2.value)

                new_node = LinkedListNode(list1.value)
                list1 = list1.next

                new_list.next = new_node
                # print(new_list.value, new_list)
                new_list = new_node

            elif list1 and list2 and list1.value > list2.value:
                # print(list1.value, list2.value)

                new_node = LinkedListNode(list2.value)
                list2 = list2.next

                new_list.next = new_node
                # print(new_list.value, new_list)
                new_list = new_node

            elif list1 is None:
                while list2:
                    # print(list2.value)
                    new_node = LinkedListNode(list2.value)
                    list2 = list2.next

                    new_list.next = new_node
                    # print(new_list.value, new_list)
                    new_list = new_node

            elif list2 is None:
                while list1:
                    # print(list1.value)
                    new_node = LinkedListNode(list1.value)
                    list1 = list1.next

                    new_list.next = new_node
                    # print(new_list.value, new_list)
                    new_list = new_node

        # print(return_node.next.value)
        return return_node.next

    if len(lists) == 0:
        return None

    last = len(lists) - 1
    while last != 0:
        start = 0
        end = last
        while start < end:
            new_list = merge_lists(lists[start], lists[end])
            lists[start] = new_list
            # while new_list:
            #     print('traverse', new_list.value)
            #     new_list = new_list.next

            start += 1
            end -= 1

        last = end

    return lists[0]

# sorted_lists = []
    # for index in range(len(lists)):
    #     # print(index, lists[index].value)
    #     sorted_lists.append([lists[index].value, index])
    #
    # sorted_lists = sorted(sorted_lists, key=lambda x: x[0])
    # print(sorted_lists)
    #
    # sorted_index = 0
    # final_lists = []
    # while sorted_index < len(sorted_lists):
    #     if sorted_index + 1 < len(sorted_lists):
    #         new_list = merge_lists(lists[sorted_lists[sorted_index][1]], lists[sorted_lists[sorted_index + 1][1]])
    #     else:
    #         new_list = lists[sorted_lists[sorted_index][1]]
    #
    #     print('after return', new_list.value)
    #     sorted_index += 2
    #     final_lists.append(new_list)
    #
    #     # printing only
    #     while new_list:
    #         print('traverse new list', new_list.value)
    #         new_list = new_list.next
    #
    # # print(final_lists)
    # return_head = LinkedListNode("head")
    # return_list = return_head
    # for part_list in final_lists:
    #     # return_list.append(elem for elem in part_list)
    #     while part_list:
    #         new_node = LinkedListNode(part_list.value)
    #         part_list = part_list.next
    #
    #         return_list.next = new_node
    #         return_list = new_node
    #
    # return return_head.next

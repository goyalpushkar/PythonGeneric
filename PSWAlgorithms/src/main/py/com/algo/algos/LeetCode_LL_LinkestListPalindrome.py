'''
Given the head node of a singly linked list, return true if the values of the linked list forms a palindrome.
       (1) -> (2) -> (3) -> (3) -> (2) -> (1)
        ^
        |
Input: (1)
Output: True


       (1) -> (2) -> (4) -> (2) -> (1)
        ^
        |
Input: (1)
Output: True



       (5) -> (8) -> (4) -> (1) -> (7)
        ^
        |
Input: (5)
Output: False

Provide if asked:

Time Complexity: O(N)
Auxiliary Space Complexity: O(N)

However, if time permits, or if you'd just like to challenge the interviewee:

Time Complexity: O(N)
Auxiliary Space Complexity: O(1)


https://leetcode.com/problems/palindrome-linked-list/description/

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # O(N) - Space, O(N) - Time
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        traverse = head
        node_val_list = []
        while traverse != None:
            node_val_list.append(traverse.val)
            traverse = traverse.next

        return self.check_palindrome(node_val_list)

    def check_palindrome(self, val_list):
        left = 0
        right = len(val_list) - 1

        while left <= right:
            if val_list[left] == val_list[right]:
                left += 1
                right -= 1
            else:
                return False

        return True

    # O(1) - Space, O(N) - Time
    def isPalindrome_O1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        traverse_node = head
        tot_length = 0
        while traverse_node != None:
            tot_length += 1
            traverse_node = traverse_node.next

        mid = tot_length // 2
        is_even_yn = "Y" if tot_length % 2 == 0 else "N"

        prev = None
        curr = head
        new_length = 0
        while curr != None:

            if new_length >= mid+1:
                # start reverse
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            else:
                prev = curr
                curr = curr.next

            new_length += 1

        left = head
        right = prev
        while left != right and right != None and right.next != left:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    no_of_tests = int(input("No of tests: "))

    # head = ListNode(1)
    # head.next = ListNode(5)
    # head.next.next = ListNode(7)
    # head.next.next.next = ListNode(10)
    # head.next.next.next.next = ListNode(7)
    # head.next.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next.next = ListNode(1)

    for i in range(no_of_tests):
        no_of_elems = int(input("Enter number of elements in the Linked List: "))
        elem = input("Enter LinkList Elements as comma separated values: ")

        # Prepare linked list
        elem_list = elem.split(", ")
        for index, element in enumerate(elem_list):
            if index == 0:
                head = ListNode(element)
                notehead = head
            else:
                notehead.next = ListNode(element)

        solution = Solution()
        result = solution.isPalindrome(head)
        print(f"result: {result}")

    # fptr.write(result + '\n')
    # fptr.close()
'''
Write a function to find the node at which the intersection of two singly linked lists begins.

If there is no intersection between the two nodes, simply return null.

Input:  headA {ListNode}, headB {ListNode}
Output: {ListNode} or null

Example
Input: 	a1, b1
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
Output:	c1

Input:  a1, b1

A:          a1 → a2

B:     b1 → b2 → b3
Output: null

Constraints
Time Complexity: O(N)

Auxiliary Space Complexity: O(1)
Each ListNode has the following properties:

ListNode {
  val : Integer
  next: null/ListNode
}
Hints/Edge cases: There could be duplicate values in either Linked List. Knowing this information, it might be best to
compare the nodes themselves instead of the node.value/data itself.

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # Using finding the length of the lists
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        '''
        Check the length of both the lists.  
        Traverse on both the lists, save the traversed values of shorter list in a dict, cmpare their values and 
        value of longer list in dict if it matches or exists in dict then that is the common value (link)
        '''
        def get_length(head):
            traverse = head
            length = 0
            while traverse is not None:
                length += 1
                traverse = traverse.next

            return length

        lengthA = get_length(headA)
        lengthB = get_length(headB)

        length_diff = lengthB-lengthA if lengthB > lengthA else lengthA-lengthB
        max_length = max(lengthA, lengthB)
        min_length = min(lengthA, lengthB)

        if lengthA < lengthB:
            save_list = "A"
        else:
            save_list = "B"

        # Move the longer list the number of times the length difference is
        while length_diff > 0:
            if save_list == "A":
                headB = headB.next
            else:
                headA = headA.next
            length_diff -= 1

        for elem in range(min_length):
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None

        # Below logic worked for 38/39 test cases
        # shorter_dict = {}
        # for elem in range(max_length):
        #     if headA.val == headB.val or save_list == "A" and headB in shorter_dict and headB.next == shorter_dict[headB].next \
        #             or save_list == "B" and headA in shorter_dict and headA.next == shorter_dict[headA].next:
        #         return headB if save_list == "A" else headA
        #
        #     if save_list == "A":
        #         shorter_dict[headA] = headA
        #     else:
        #         shorter_dict[headB] = headB
        #
        #     if headA.next is not None:
        #         headA = headA.next
        #
        #     if headB.next is not None:
        #         headB = headB.next
        #
        # return None

        # Without finding the length of the lists Append List A to List B and List B to List A so that total elements on
        # both lists will be same i.e. Length A + Length B = Length B + Length A
        # in one pass when both elements are equal then that is the intersection point
        def getIntersectionNode(self, headA, headB):
            """
            :type head1, head1: ListNode
            :rtype: ListNode
            """
            traverseA = headA
            traverseB = headB
            while traverseA != traverseB:
                traverseA = traverseA.next if traverseA is not None else headB
                traverseB = traverseB.next if traverseB is not None else headA

            return traverseA


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
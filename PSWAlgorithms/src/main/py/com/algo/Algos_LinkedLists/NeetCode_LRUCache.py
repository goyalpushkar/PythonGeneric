'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the
cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
'''

from collections import OrderedDict

class LRUCache:

    # Beats 84.51% 766 ms
    def __init__(self, capacity):
        self.lru_cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.lru_cache:
            value = self.lru_cache[key]
            self.lru_cache.pop(key)
            self.lru_cache[key] = value
            return value
        else:
            return -1


    def put(self, key, value) -> None:

        if key in self.lru_cache:
            old_value = self.lru_cache[key]
            self.lru_cache.pop(key)
            # Other ways
            # self.data.move_to_end(key)
            # del self.hash_map[key]
            self.lru_cache[key] = value
        else:
            if len(self.lru_cache) + 1 > self.capacity:
                self.lru_cache.popitem(last=False)

            self.lru_cache[key] = value


class Node:

    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.val = value
        self.next = next
        self.prev = prev


class LRUCache_Custom:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        node = self.dic[key]
        value = node.val
        self.deleteNode(node)
        self.addToHead(node)

        return value

    def put(self, key: int, value: int) -> None:

        if key in self.dic:

            node = self.dic[key]
            self.deleteNode(node)
            self.addToHead(node)
            node.val = value


        else:

            if len(self.dic) == self.capacity:
                node = self.tail.prev
                self.deleteNode(node)
                del self.dic[node.key]

            newNode = Node(key, value)
            self.addToHead(newNode)
            self.dic[newNode.key] = newNode

    def addToHead(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

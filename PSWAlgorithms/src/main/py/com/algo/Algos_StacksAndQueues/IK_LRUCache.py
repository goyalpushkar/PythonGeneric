'''
Implement a Least Recently Used (LRU) cache and execute a given sequence of SET(key, value) 
and GET(key) operations. Return the results of all the GET operations from the sequence.

Initially the cache is empty. Cache capacity is a part of the input. Keys and values are all positive. 
GET(key) returns either the cached value or -1 (cache miss). SET(key, value) adds or updates the value
 for the key. If cache is at capacity and a new value needs to be added, remove the least recently 
 used (LRU) value first.

Example
{
"capacity": 2,
"query_type": [1, 1, 0, 1, 0, 1, 0],
"key": [5, 10, 5, 15, 10, 5, 5],
"value": [11, 22, 1, 33, 1, 55, 1]
}
Output:

[11, -1, 55]
query_type of 0 means GET and query_type of 1 means SET.

Here are the operations from the input along with the return values and side effects of their execution:

Operation	Cache after	Returned value	Side effect
SET(5, 11)	[5 -> 11]		5 -> 11 added to cache
SET(10, 22)	[10 -> 22, 5 -> 11]		5 -> 11 became LRU
GET(5)	[5 -> 11, 10 -> 22]	11	10 -> 22 became LRU
SET(15, 33)	[15 -> 33, 5 -> 11]		10 -> 22 got evicted
GET(10)	[15 -> 33, 5 -> 11]	-1	Access order unchanged
SET(5, 55)	[5 -> 55, 15 -> 33]		Key 5 updated, became the
most recently used (MRU)
GET(5)	[5 -> 55, 15 -> 33]	55	No change; key 5 already
was the MRU
Notes
The function accepts four arguments:

The cache capacity,
query_type array with 0 for GET and 1 for SET operation,
key array with the keys for all the operations,
value array with the values for SET operations (value to be ignored for GETs).
The three input arrays all have the same length n and together they represent n operations.
Constraints:

1 <= capacity <= 105
1 <= n <= 105
1 <= any key <= 105
1 <= any value <= 105
'''
def implement_lru_cache(capacity, query_type, key, value):
    """
    Args:
    capacity(int32)
    query_type(list_int32)
    key(list_int32)
    value(list_int32)
    Returns:
    list_int32
    """
    # Write your code here.
    from collections import OrderedDict
    
    lru_keys = OrderedDict()
    # key_val_map = {}
    
    def insert(key, val):
        # if it is an update then no change in the size just update the existing value
        if key not in lru_keys:
            if len(lru_keys) >= capacity:
                lru_keys.popitem(last=False)
            # key_val_map.pop(key)
        
        lru_keys[key] = val
        lru_keys.move_to_end(key)
        # key_val_map[key] = val
    
    def remove(key):
        if key not in lru_keys:
            return -1
        
        # Also reinsert this key in lru to make it least recently used
        # val = lru_keys.pop(key)
        # insert(key, val)
        lru_keys.move_to_end(key)
        
        return lru_keys[key]
    
    return_arr = []
    for i, val in enumerate(query_type):
        if val == 0:
            ret_val = remove(key[i])
            return_arr.append(ret_val)
        else:
            insert(key[i], value[i])
        
        # print(f"lru_keys: {lru_keys}, return_arr: {return_arr}")
    
    return return_arr
#Find the smallest key(sorted alphabatically) with the nth highest value

from functools import cmp_to_key

def myComparator(a,b):
    if a[1] < b[1]:
        return 1
    elif a[1] > b[1]:
        return -1
    else:
        if a[0] < b[0]:
            return -1
        elif a[0] > b[0]:
            return 1
        else:
            return 0

def nthSmallestKey(df, n):

    print("Sorted Values")
    sorted_values = sorted(df.values(), reverse=True)
    print(sorted_values)

    value = sorted_values[n - 1]
    print("nth Largest Value", value)

    sorted_by_key = sorted(df.items())
    print("Sorted by Keys", sorted_by_key)

    for key in sorted(df.keys()):
        if df[key] == value:
            return key

    return None

def nthSmallestKeySorted(df, n):
    index = 1
    for key in sorted_dict:
        if index == 2:
            return key[0]

        index += 1

if __name__ == '__main__':
    df = {'a': 1, 'b': 2, 'd': 100, 'e': 90, 'g': 90}

    #Sort dictionary on values
    print("Sorted dictionary on values")
    print(sorted(df.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))

    print("Sorted dictionary on values and keys")
    print(sorted(df.items(), key=cmp_to_key(myComparator)))
    sorted_dict = sorted(df.items(), key=cmp_to_key(myComparator))

    print(nthSmallestKeySorted(sorted_dict, 2))

    print(nthSmallestKey(df, 2))

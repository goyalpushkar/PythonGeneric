'''
Given a number and a list of words, return the given number of most frequent words.

Example
{
"k": 4,
"words": ["car", "bus", "taxi", "car", "driver", "candy", "race", "car", "driver", "fare", "taxi"]
}
Output:

["car", "driver", "taxi", "bus"]
Notes
Every word consists of only lowercase English letters.
Return the answer sorted by the frequency from highest to lowest. Sort the words with the same
 frequency by their lexicographical order.
Constraints:

1 <= number of words <= 105
1 <= size of each word <= 10
1 <= the given number <= the number of unique words
'''

class Solution:

    def k_most_frequent(k, words):
        """
        Args:
         k(int32)
         words(list_str)
        Returns:
         list_str
        """
        # Write your code here.
        word_dict = {}
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1
        # print(word_dict)
        # sorted_word_dict = dict(sorted(word_dict.items(), key=lambda x: x[1], reverse=True))

        reverse_dict = {}
        for key, value in word_dict.items():
            if value in reverse_dict:
                reverse_dict[value].append(key)
            else:
                reverse_dict[value] = [key]
            # reverse_dict[value] = reverse_dict.get(value, []).append(key)
            # reverse_dict.get(value, []).append(key)
        # print(reverse_dict)

        reverse_dict = dict(sorted(reverse_dict.items(), reverse=True))
        # print(reverse_dict)

        final_list = []
        total = 0
        for key, values in reverse_dict.items():
            # sorted_vals = sorted(values)[0:k-total]
            # print(sorted_vals)
            for val in sorted(values)[0:k - total]:
                # print(val)
                final_list.append(val)

            total += len(values[0:k - total])

            if total >= k:
                return final_list

            # if len(values) < k-total:
            #     for val in sorted(values):
            #         final_list.append(val)
            # else:
            #     for val in sorted(values[0:k-total]):
            #         final_list.append(val)

            #     return final_list

            # total += len(values)

        return final_list


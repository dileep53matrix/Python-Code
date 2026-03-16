# def get_first_item(my_list):
#     return my_list[2]

# list = ["Dileep", "ujwal", "sanchit"]
# print(get_first_item(list))
# def get_unique_word_lengths(text):
#     # Split the string into a list of words
#     words = text.split()
    
#     # Convert the list to a set to get only unique words
#     unique_words = set(words)
    
#     # Create a dictionary to store each unique word and its length
#     word_lengths = {}
#     for word in unique_words:
#         word_lengths[word] = len(word)
        
#     return word_lengths

# # Example Usage:
# sentence = "the quick brown fox jumps over the lazy dog the quick brown fox"
# lengths = get_unique_word_lengths(sentence)
# print(lengths)
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return " "
            

        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0

        while i < len(first) and i <len(last) and first[i] == last[i]:
            i += 1
        return first[:i]
    print(longestCommonPrefix(["flower","flow","flight"]))

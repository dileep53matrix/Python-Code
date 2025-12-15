#Develop a program to print 10 most frequently appearing words in a text
# file. [Hint: Use a dictionary
# program to print 10 most frequentely appearing words in text file
filename = input("Enter the file name ")

#creating an empty dictionary to store word frequinces 

word_freq = {}
# read the file and process
with open(filename,'r') as file:
    for line in file:
        #convet line to lowecase and split into words 
        words = line.lower().split()
        for word in words:
            #count the word in dictionary
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
#sort the dictionary by frequency in decending order
sorted_words = sorted(word_freq.items(), key = lambda x: x[1] , reverse = True)
#slice the top 10 words
top_10 = sorted_words[:10]
#display the top 10 words and their frequencies 
print("top 10 frequent words:")

for word, freq in top_10:
    print(word,":", freq)

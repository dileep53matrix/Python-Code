import re
paragraph = input("enter a aparagraph :\n")

# convert to lowercase
text = paragraph.lower()
words = re.findall(r"[a-zA-Z0-9]+", text)
frequency = {}
for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]= 1
longest_word = " "
for word in words:
    if len(word)>len(longest_word):
        longest_word = word
    
sentences= re.split(r"[.!?]+",paragraph)
sentences = [s for s in sentences if s.strip()]
print("\n...  text analysis result..")
print("total words:", len(words))
print("Numbers of sentences :", len(sentences))
print("longest word:", longest_word)
print("word frequency")

for word, count in frequency.items():
    print(f"{word}:{count}")


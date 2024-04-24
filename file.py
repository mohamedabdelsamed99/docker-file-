import pandas as pd
import nltk
from nltk.corpus import stopwords

file = open('paragraphs.txt', 'r')
paragraph = file.readlines()
## print(paragraph[:10]) 
file.close()  
paragraph_string = ''.join(paragraph)
print(paragraph_string[:1000])


# download the stopwords corpus
nltk.download('stopwords')
#define the stopwords
stop_words = set(stopwords.words('english')) 
stop_words

# to splite the paragraph
words =paragraph_string.split()

#to remove the stop words 
filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]
filtered_sentence = ' '.join(filtered_words)
print(filtered_sentence[:100])

word_freq = {}
for word in filtered_words:
    if word not in word_freq:
        word_freq[word] = 0
    word_freq[word] += 1
for word, freq in word_freq.items():
    print(f"{word}: {freq}")

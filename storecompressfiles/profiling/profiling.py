import sys
from pandas import *
words_data = read_csv("storecompressfiles\profiling\words.csv")

words = words_data['original_word'].tolist()
encode_words = words_data['encoded_word'].tolist()
encode_words = [int(i) for i in encode_words]

words_avg_size = 0
encode_words_avg_size = 0

for i in range(len(words)):
    words_avg_size += sys.getsizeof(words[i])
    encode_words_avg_size += sys.getsizeof(encode_words[i])

original_size = words_avg_size/len(words)
new_size = encode_words_avg_size/len(encode_words)

print("Compress rate: {}".format(((original_size-new_size)/original_size)*100))
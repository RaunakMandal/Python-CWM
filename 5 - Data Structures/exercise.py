# Find the highest occuring character

from pprint import pprint  # Prettyprint
sentence = "This is a common interview question"
char_freq = {}
for char in sentence:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

char_freq_sorted = sorted(char_freq.items(),
                          key=lambda kv: kv[1],
                          reverse=True)
print(char_freq_sorted[0])

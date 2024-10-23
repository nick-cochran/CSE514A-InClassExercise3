import re

# 1.3 & 1.4 Working
file_path_1 = 'PA1_training_text.txt'
# Okay, don't know the pathing here, but locally I got 323 words before, then 173 filtered. 
with open(file_path_1, 'r', encoding='utf-8', errors='ignore') as file:
    text = file.read()

text = text.lower()

text = re.sub(r'[.,:]', '', text)

words = text.split()

unique_words = set(words)

print(f"Total words: {len(words)}")
less_4= [words for words in words if len(words) < 4]
#print(less_4)
print(f"# Words <4 :" , len(less_4))
print(f"Unique words: {len(unique_words)}")
less_4_unique= [unique_words for unique_words in unique_words if len(unique_words) < 4]
print(f"# Words <4 :" , len(less_4_unique))


# print(unique_words)


# 1.5
#res = [ele for ele in text if len(ele) < 4]
# res = ' '.join(res)
#print("Removed words:", len(res))

#filtered_unique_words= [unique_word for unique_word in unique_words if len(unique_word) < 4]
#print(len(filtered_unique_words))


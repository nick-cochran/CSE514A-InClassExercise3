import pandas as pd
import re

# Importing the .txt file named PA1_training_text.txt

# help me, it didn't run

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        data = file.read()
    return data

file_path_1 = 'PA1_training_text.txt'
file_path_2 = 'PA2_training_text.txt'
file_content_1 = read_file(file_path_1)
file_content_2 = read_file(file_path_2)

file_content_1 = file_content_1.lower()
file_content_1 = re.sub(r'[.,:]', '', file_content_1)
file_content_2 = file_content_2.lower()
file_content_2 = re.sub(r'[.,:]', '', file_content_2)

split_content_1 = file_content_1.split()
print(f"len(split_content_1): ", len(split_content_1))
split_content_2 = file_content_2.split()
print(f"len(split_content_2): ", len(split_content_2))

# words_over_4_1 = list()
# words_over_4_2 = list()
# for i in split_content_1:
#     if len(i) >= 4:
#         words_over_4_1.append(i)

# for i in split_content_2:
#     if len(i) < 4:
#         words_over_4_2.append(i)

# print(f"Words in PA1 (after removing): ", len(words_over_4_1))
# print(f"Words in PA2 (after removing): ", len(words_over_4_2))







# unique_words_2 = set(words_over_4_2)
# print(f"unique words in PA2 (after removing): ", len(unique_words_2))


removed_words_1 = [ele for ele in split_content_1 if len(ele) > 3]
print("PA1 Words list (after removing):", len(removed_words_1))
unique_words_1 = set(removed_words_1)
print(f"unique words in PA1 (after removing): ", len(unique_words_1))

removed_words_2 = [ele for ele in split_content_2 if len(ele) > 3]
print("PA2 Words list (after removing):", len(removed_words_2))
unique_words_2 = set(removed_words_2)
print(f"unique words in PA2 (after removing): ", len(unique_words_2))

vocabulary = unique_words_1.union(unique_words_2)
print(f"Vocabulary length: ", len(vocabulary))

PA1_dict = dict()
PA2_dict = dict()

for i in vocabulary:
    PA1_dict[i] = 0
    for j in removed_words_1:
        if i == j:
            PA1_dict[i] += 1


for i in vocabulary:
    PA2_dict[i] = 0
    for j in removed_words_2:
        if i == j:
            PA2_dict[i] += 1

print(PA1_dict["algorithm"])
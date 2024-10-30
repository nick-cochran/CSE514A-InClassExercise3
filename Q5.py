import re
from ICE3 import sorted_vocabulary, PA1_probabilities, PA2_probabilities


# Importing the .txt file named PA1_training_text.txt
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        data = file.read()
    return data


file_path_1 = 'PA2_testing_text_1.txt'
file_path_2 = 'PA2_testing_text_2.txt'
file_path_3 = 'PA2_testing_text_3.txt'
file_path_4 = 'PA2_testing_text_4.txt'
file_content_1 = read_file(file_path_1)
file_content_2 = read_file(file_path_2)
file_content_3 = read_file(file_path_3)
file_content_4 = read_file(file_path_4)

comb_file_contents = file_content_1 + file_content_2 + file_content_3 + file_content_4

comb_file_contents = comb_file_contents.lower()
comb_file_contents = re.sub(r'[.,:]', '', comb_file_contents)

print("Combined test data")
split_content = comb_file_contents.split()
print(f"len(split_content_1): ", len(split_content))

unique_words = set(split_content)
print(f"unique words in PA1: ", len(unique_words))

removed_words = [ele for ele in split_content if len(ele) > 3]
print("PA1 Words list (after removing):", len(removed_words))
removed_unique_words = set(removed_words)
print(f"unique words in PA1 (after removing): ", len(removed_unique_words))

# create bag of words for test set
test_counts = {word: removed_words.count(word) for word in sorted_vocabulary}

PA1_test_prob = 1
PA2_test_prob = 1

# calculate approximate probabilities
for word, count in test_counts.items():
    if count > 0:
        PA1_test_prob *= PA1_probabilities[word] ** count
        PA2_test_prob *= PA2_probabilities[word] ** count

print("Proportional probability of PA1 for combined test data:", PA1_test_prob)
print("Proportional probability of PA2 for combined test data:", PA2_test_prob)

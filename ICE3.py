import re
import csv


# Importing the .txt file named PA1_training_text.txt
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

unique_words_1 = set(split_content_1)
print(f"unique words in PA1: ", len(unique_words_1))
unique_words_2 = set(split_content_2)
print(f"unique words in PA2: ", len(unique_words_2))

removed_words_1 = [ele for ele in split_content_1 if len(ele) > 3]
print("PA1 Words list (after removing):", len(removed_words_1))
removed_unique_words_1 = set(removed_words_1)
print(f"unique words in PA1 (after removing): ", len(removed_unique_words_1))

removed_words_2 = [ele for ele in split_content_2 if len(ele) > 3]
print("PA2 Words list (after removing):", len(removed_words_2))
removed_unique_words_2 = set(removed_words_2)
print(f"unique words in PA2 (after removing): ", len(removed_unique_words_2))

vocabulary = removed_unique_words_1.union(removed_unique_words_2)
print(f"Vocabulary length: ", len(vocabulary))
# Sort the vocabulary alphabetically
sorted_vocabulary = sorted(vocabulary)


# calculate word counts for PA1 and PA2
PA1_dict = dict()
PA2_dict = dict()

for word in sorted_vocabulary:
    PA1_dict[word] = removed_words_1.count(word)
    PA2_dict[word] = removed_words_2.count(word)


v = len(vocabulary)
n1 = len(removed_words_1)
n2 = len(removed_words_2)

# Calculate conditional probabilities with Laplace smoothing
PA1_probabilities = dict()
PA2_probabilities = dict()

# calculate probabilities
for word in sorted_vocabulary:
    PA1_probabilities[word] = (PA1_dict[word] + 1) / (n1 + v)
    PA2_probabilities[word] = (PA2_dict[word] + 1) / (n2 + v)


# paths for saving to csv
PA1_csv = 'PA1_probabilities.csv'
PA2_csv = 'PA2_probabilities.csv'

# save PA1 and PA2 probabilities to csv
with open(PA1_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Vocabulary', 'P(word|PA1)'])
    # Write each word and its probability
    for word in sorted_vocabulary:
        writer.writerow([word, PA1_probabilities[word]])

with open(PA2_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    # headers
    writer.writerow(['Vocabulary', 'P(word|PA2)'])
    # word and probability
    for word in sorted_vocabulary:
        writer.writerow([word, PA2_probabilities[word]])


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

print("Number of times 'algorithm' is in PA1: ", PA1_dict["algorithm"])
print("Number of times 'algorithm' is in PA2: ", PA2_dict["algorithm"])

import re
import csv


# Importing the .txt file named PA1_training_text.txt
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        data = file.read()
    return data


file_path_1 = 'PA1_training_text.txt'
file_path_2 = 'PA2_training_text.txt'

file_path_test1 = 'PA1_testing_text.txt'
file_path_test2_1 = 'PA2_testing_text_1.txt'
file_path_test2_2 = 'PA2_testing_text_2.txt'
file_path_test2_3 = 'PA2_testing_text_3.txt'
file_path_test2_4 = 'PA2_testing_text_4.txt'

file_content_1 = read_file(file_path_1)
file_content_2 = read_file(file_path_2)

file_content_test1 = read_file(file_path_test1)
file_content_test2_1 = read_file(file_path_test2_1)
file_content_test2_2 = read_file(file_path_test2_2)
file_content_test2_3 = read_file(file_path_test2_3)
file_content_test2_4 = read_file(file_path_test2_4)

file_content_1 = file_content_1.lower()
file_content_1 = re.sub(r'[.,:]', '', file_content_1)
file_content_2 = file_content_2.lower()
file_content_2 = re.sub(r'[.,:]', '', file_content_2)

file_content_test1 = file_content_test1.lower()
file_content_test1 = re.sub(r'[.,:]', '', file_content_test1)
file_content_test2_1 = file_content_test2_1.lower()
file_content_test2_1 = re.sub(r'[.,:]', '', file_content_test2_1)
file_content_test2_2 = file_content_test2_2.lower()
file_content_test2_2 = re.sub(r'[.,:]', '', file_content_test2_2)
file_content_test2_3 = file_content_test2_3.lower()
file_content_test2_3 = re.sub(r'[.,:]', '', file_content_test2_3)
file_content_test2_4 = file_content_test2_4.lower()
file_content_test2_4 = re.sub(r'[.,:]', '', file_content_test2_4)

split_content_1 = file_content_1.split()
print(f"len(split_content_1): ", len(split_content_1))
split_content_2 = file_content_2.split()
print(f"len(split_content_2): ", len(split_content_2))

split_content_test1 = file_content_test1.split()
split_content_test2_1 = file_content_test2_1.split()
split_content_test2_2 = file_content_test2_2.split()
split_content_test2_3 = file_content_test2_3.split()
split_content_test2_4 = file_content_test2_4.split()

unique_words_1 = set(split_content_1)
print(f"unique words in PA1: ", len(unique_words_1))
unique_words_2 = set(split_content_2)
print(f"unique words in PA2: ", len(unique_words_2))

unique_words_test1 = set(split_content_test1)
unique_words_test2_1 = set(split_content_test2_1)
unique_words_test2_2 = set(split_content_test2_2)
unique_words_test2_3 = set(split_content_test2_3)
unique_words_test2_4 = set(split_content_test2_4)

removed_words_1 = [ele for ele in split_content_1 if len(ele) > 3]
print("PA1 Words list (after removing):", len(removed_words_1))
removed_unique_words_1 = set(removed_words_1)
print(f"unique words in PA1 (after removing): ", len(removed_unique_words_1))

removed_words_2 = [ele for ele in split_content_2 if len(ele) > 3]
print("PA2 Words list (after removing):", len(removed_words_2))
removed_unique_words_2 = set(removed_words_2)
print(f"unique words in PA2 (after removing): ", len(removed_unique_words_2))

removed_words_test1 = [ele for ele in split_content_test1 if len(ele) > 3]
print("PA1 Test Words list (after removing):", len(removed_words_test1))
removed_unique_words_test1 = set(removed_words_test1)
print(f"unique words in PA1 Test (after removing): ", len(removed_unique_words_test1))

removed_words_test2_1 = [ele for ele in split_content_test2_1 if len(ele) > 3]
print("PA2_1 Test Words list (after removing):", len(removed_words_test2_1))
removed_unique_words_test2_1 = set(removed_words_test2_1)
print(f"unique words in PA2_1 Test (after removing): ", len(removed_unique_words_test2_1))

removed_words_test2_2 = [ele for ele in split_content_test2_2 if len(ele) > 3]
print("PA2_2 Test Words list (after removing):", len(removed_words_test2_2))
removed_unique_words_test2_2 = set(removed_words_test2_2)
print(f"unique words in PA2_1 Test (after removing): ", len(removed_unique_words_test2_2))

removed_words_test2_3 = [ele for ele in split_content_test2_3 if len(ele) > 3]
print("PA2_3 Test Words list (after removing):", len(removed_words_test2_3))
removed_unique_words_test2_3 = set(removed_words_test2_3)
print(f"unique words in PA2_3 Test (after removing): ", len(removed_unique_words_test2_3))

removed_words_test2_4 = [ele for ele in split_content_test2_4 if len(ele) > 3]
print("PA2_4 Test Words list (after removing):", len(removed_words_test2_4))
removed_unique_words_test2_4 = set(removed_words_test2_4)
print(f"unique words in PA2_4 Test (after removing): ", len(removed_unique_words_test2_4))

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
# PA1_csv = 'PA1_probabilities.csv'
# PA2_csv = 'PA2_probabilities.csv'
#
# # save PA1 and PA2 probabilities to csv
# with open(PA1_csv, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     # Write header
#     writer.writerow(['Vocabulary', 'P(word|PA1)'])
#     # Write each word and its probability
#     for word in sorted_vocabulary:
#         writer.writerow([word, PA1_probabilities[word]])
#
# with open(PA2_csv, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     # headers
#     writer.writerow(['Vocabulary', 'P(word|PA2)'])
#     # word and probability
#     for word in sorted_vocabulary:
#         writer.writerow([word, PA2_probabilities[word]])


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
print()

# Question 4.3 checking proportional probabilities
# create bag of words for test set
test_counts = {word: removed_words_test1.count(word) for word in sorted_vocabulary}

PA1_test_prob = 1
PA2_test_prob = 1

for word, count in test_counts.items():
    if count > 0:
        PA1_test_prob *= PA1_probabilities[word] ** count
        PA2_test_prob *= PA2_probabilities[word] ** count

print("Proportional probability of PA1 for PA1_testing_text:", PA1_test_prob)
print("Proportional probability of PA2 for PA1_testing_text:", PA2_test_prob)
print()


test_files = {
    "PA2_test_1": removed_words_test2_1,
    "PA2_test_2": removed_words_test2_2,
    "PA2_test_3": removed_words_test2_3,
    "PA2_test_4": removed_words_test2_4,
}

for test_name, test_words in test_files.items():
    test_counts = {word: test_words.count(word) for word in sorted_vocabulary}

    PA1_test_prob = 1
    PA2_test_prob = 1

    for word, count in test_counts.items():
        # if word in document
        if count > 0:
            PA1_test_prob *= PA1_probabilities[word] ** count
            PA2_test_prob *= PA2_probabilities[word] ** count

    print(f"Proportional probability of PA1 for {test_name}: {PA1_test_prob}")
    print(f"Proportional probability of PA2 for {test_name}: {PA2_test_prob}")
    print()


# Question 5

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
PA1_bad_muls_count = 0
PA2_bad_muls_count = 0

# calculate approximate probabilities
for word, count in test_counts.items():
    if count > 0:
        if PA1_test_prob * PA1_probabilities[word] ** count != 0.0:
            PA1_test_prob *= PA1_probabilities[word] ** count
        else:
            PA1_bad_muls_count += 1
        if PA2_test_prob * PA2_probabilities[word] ** count != 0.0:
            PA2_test_prob *= PA2_probabilities[word] ** count
        else:
            PA2_bad_muls_count += 1
        # print(f"PA1_prob: {PA1_probabilities[word]}, PA2_prob: {PA2_probabilities[word]}, PA1_test_prob: {PA1_test_prob}, PA2_test_prob: {PA2_test_prob}")

print(f"Proportional probability of PA1 for combined test data: {PA1_test_prob} with {PA1_bad_muls_count} multiplications that would've resulted in 0.0")
print(f"Proportional probability of PA2 for combined test data: {PA2_test_prob} with {PA2_bad_muls_count} multiplications that would've resulted in 0.0")
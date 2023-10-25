def extract_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        return words

def create_word_dictionary(file1_words, file2_words):
    word_dictionary = {}
    
    for word in file1_words:
        if word in word_dictionary:
            word_dictionary[word].append("file1.txt")
        else:
            word_dictionary[word] = ["file1.txt"]
    
    for word in file2_words:
        if word in word_dictionary:
            word_dictionary[word].append("file2.txt")
        else:
            word_dictionary[word] = ["file2.txt"]
    
    return word_dictionary

def intersect_posting_lists(list1, list2):
    result = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1

    return result

file1_path = "file1.txt"
file2_path = "file2.txt"

file1_words = extract_words_from_file(file1_path)
file2_words = extract_words_from_file(file2_path)

word_set_file1 = set(file1_words)
word_set_file2 = set(file2_words)

common_words = word_set_file1.intersection(word_set_file2)

print("کلمات مشترک بین فایل 1 و فایل 2:", common_words)




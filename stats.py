def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text:
        c = char.lower()
        if c in char_count:
            char_count[c] = char_count[c] + 1
        else:
            char_count[c] = 1
    return char_count

def sort_characters(char_dictionaries):
	char_list = []

def sort_on(item):
    return item["num"]

def sort_characters(char_dictionaries):
    char_list = []
    for char, count in char_dictionaries.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

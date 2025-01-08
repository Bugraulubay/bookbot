def get_contents(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_characters(text):
    lowered_text = text.lower()
    character_dict = {}
    for c in lowered_text:
        if c.isalpha():
            if c in character_dict:
                character_dict[c] += 1
            else: character_dict[c] = 1
    return character_dict

def report(word_count,character_count_dict):
    print("--- The Report of books/frankenstein.txt ---")
    print(f"{word_count} words found in document")
    dict_sorted = dict(sorted(character_count_dict.items(), key=lambda item: item[1], reverse=True))
    for c in dict_sorted:
        print(f"The '{c}' character was found {dict_sorted[c]} times")
    print("--------------- End of Report ---------------")

def main():
    paths = ["books/frankenstein.txt"]
    content = get_contents(paths[0])
    word_count = count_words(content)
    character_count_dict = count_characters(content)
    report(word_count,character_count_dict)

main()
def get_contents(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    word_list = text.split()
    return len(word_list)

def main():
    paths = ["books/frankenstein.txt"]
    word_count = count_words(get_contents(paths[0]))
    print(word_count)

main()
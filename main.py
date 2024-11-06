def print_fs():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def word_count_fs():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        single_words = file_contents.split()
        word_count = len(single_words)
        print(f"The book contains {word_count} words.")


def main():
    word_count_fs()

main()

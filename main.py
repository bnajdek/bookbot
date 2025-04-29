from stats import count_words
from stats import letter_count
from stats import sorted_count
from sys import argv
from sys import exit
def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    with open(argv[1]) as f:
        file_contents = f.read()
    letters = letter_count(file_contents)
    #counted_words = (count_words(file_contents))
    #return(count_words(file_contents),letters)
    print(count_words(file_contents))
    sorted_list = sorted_count(letters)
    for entry in sorted_list:
        print(f"{entry['char']}: {entry['count']}")

main()
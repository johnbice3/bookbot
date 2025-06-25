import sys

if len(sys.argv) == 1:
    print ('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    pass

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

from stats import word_count

from stats import character_count

from stats import character_list_sorting

def main():
    path = sys.argv[1]
    text = (get_book_text(path))
    final_count = word_count(text)
    character_amounts = character_count(text)
    sorted_chars = character_list_sorting(character_amounts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {final_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_chars:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")

main()
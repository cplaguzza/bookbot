import sys
from stats import get_num_words, get_num_characters, get_sorted_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1] 
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        num_characters = get_num_characters(text)
        sorted_dict = get_sorted_dict(num_characters)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char_dict in sorted_dict:
            if char_dict["char"].isalpha():
                print(f"{char_dict['char']}: {char_dict['num']}")
        print("============= END ===============")
   
def get_book_text(path):
    with open(path) as f:
        return f.read()
   
main()


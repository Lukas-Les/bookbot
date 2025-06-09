import sys
from stats import get_num_words, get_num_symbols, generate_report


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, "r") as f:
        file_contents = f.read()
    return file_contents

def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    print(generate_report(file_path, book_text))

main()

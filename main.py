from stats import get_num_words


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, "r") as f:
        file_contents = f.read()
    return file_contents

def main() -> None:
    book_text = get_book_text("books/frankenstein.txt")
    get_num_words(book_text)

main()

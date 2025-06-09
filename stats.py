from collections import defaultdict


def get_num_words(text: str) -> int:
    num_words = len(text.split())
    return num_words


def get_num_symbols(text: str) -> dict:
    text_split = text.lower().split()
    result = defaultdict(int)
    for word in text_split:
        for s in word:
            result[s] +=1
    return result


def generate_report(file_path: str, book_text: str) -> str:
    words_total = get_num_words(book_text)
    message = f"""
============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------j
Found {words_total} total words
--------- Character Count -------\n
"""
    symmbol_count = get_num_symbols(book_text)
    symmbol_count_list = [{k: v} for k, v in symmbol_count.items() if k.isalpha()]
    symmbol_count_list.sort(key=lambda x: list(x.values()), reverse=True)
    for item in symmbol_count_list:
        message += f"{list(item.keys())[0]}: {list(item.values())[0]}\n"
    message += "============= END ==============="
    return message

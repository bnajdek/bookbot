def count_words(text):
    words = text.split()
    word_count = len(words)
    return(f"Found {word_count} total words")

def letter_count(text):
    text = text.lower()
    char_dict = dict()
    for character in text:
        if character.isalpha():
            if character in char_dict:
                char_dict[character] += 1
            else:
               char_dict[character] = 1
    return(char_dict)

def sorted_count(chars_with_count):
    chars_and_counts = [
        {"char": char, "count": count}
        for char, count in chars_with_count.items()
    ]

    chars_and_counts.sort(
        key=lambda d: d["count"],
        reverse=True
    )

    return chars_and_counts
def count_words(text):
    words = text.split()
    return len(words)

def count_character(text):
    character_count = {}
    for c in text.lower():
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1
    return character_count

def sort_character(character_count):
    char_list =[{"char": char, "count": character_count[char]} for char in character_count]
    char_list.sort(key=lambda x: x["count"], reverse=True)
    return char_list
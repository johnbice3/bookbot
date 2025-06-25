def word_count(text):
    count_of_words = text.split()
    return len(count_of_words)

def character_count(text):
    characters = {}
    for character in text:
        char_to_count = character.lower()
        if char_to_count in characters:
            characters[char_to_count] += 1
        else:
            characters[char_to_count] = 1
    return characters

def character_list_sorting(characters):
    counted_letters = []
    for key, value in characters.items():
        counted_letters.append({"char": key, "num": value})

    def sort_on(item):
        return item["num"]
    
    counted_letters.sort(reverse=True, key=sort_on)
    return counted_letters  

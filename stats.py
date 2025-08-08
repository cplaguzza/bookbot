def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    num_characters = {}
    characters = text.lower()
    for character in characters:
        if character in num_characters:
            num_characters[character] += 1
        else: 
            num_characters[character] = 1
    return num_characters 
     



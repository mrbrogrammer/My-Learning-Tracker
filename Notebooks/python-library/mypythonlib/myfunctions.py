# def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    
#     # Convert decimal degrees to radians
#     lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2,
#     lat2])

#     # Haversine formula
#     dlon = lon2 - lon1
#     dlat = lat2 - lat1
#     a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
#     c = 2 * np.arcsin(np.sqrt(a))
#     km = 6367 * c
#     return km * 1000



# open file and read lines as words
def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# print the word with the unguessed letters censored
def random_fill_word(word):
    new_word = []
    random_index = random.randint(0, len(word)-1)
    random_letter = word[random_index]
    for i in range(len(word)):
        if word[i] == random_letter:
            new_word.append(word[i])
        else:
            new_word.append("_")

    new_word = "".join(new_word)
    return new_word

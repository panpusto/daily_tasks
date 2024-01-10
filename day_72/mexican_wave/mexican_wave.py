def wave(people: str) -> list[str]:
    words = []
    for i in range(len(people)):
        if people[i].isalpha():
            words.append(people[:i] + people[i].upper() + people[i+1:])
    return words

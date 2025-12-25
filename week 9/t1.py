def are_anagrams(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    # string1 = string1.strip(" .,")
    # string2 = string2.strip(" .,")
    for i in " .,":
        string1 = string1.replace(i, "")
        string2 = string2.replace(i, "")
    return sorted(string1) == sorted(string2)
print(are_anagrams("Listen", "Silent"))
print(are_anagrams("The Morse Code", "Here come dots"))
print(are_anagrams("Astronomer", "Moon starer"))
print(are_anagrams("Hello", "World"))
print(are_anagrams("Dormitory", "Dirty room."))
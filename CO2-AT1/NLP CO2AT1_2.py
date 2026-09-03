words = ["unhappy", "happiness", "happily"]

def morphological_parse(word):

    if word.startswith("un"):
        prefix = "un"
        root = word[2:]
        suffix = "-"
        transformation = "Derivational"

    elif word.endswith("ness"):
        prefix = "-"
        root = word[:-4]
        suffix = "ness"
        transformation = "Derivational"

    elif word.endswith("ly"):
        prefix = "-"
        root = word[:-2]
        suffix = "ly"
        transformation = "Derivational"

    else:
        prefix = "-"
        root = word
        suffix = "-"
        transformation = "None"

    return prefix, root, suffix, transformation


print("\nMORPHOLOGICAL PARSING")
print("-" * 85)
print(f"{'Word':<15}{'Prefix':<12}{'Root':<15}"
      f"{'Suffix':<12}{'Type':<20}{'Normalized':<15}")
print("-" * 85)

for word in words:
    prefix, root, suffix, transformation = morphological_parse(word)

    print(f"{word:<15}{prefix:<12}{root:<15}"
          f"{suffix:<12}{transformation:<20}{root:<15}")
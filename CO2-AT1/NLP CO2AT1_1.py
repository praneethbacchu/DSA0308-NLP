words = ["connected", "connecting", "connection"]

def analyze_word(word):
    if word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        suffix_type = "Inflectional"

    elif word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        suffix_type = "Inflectional"

    elif word.endswith("ion"):
        root = word[:-3]
        suffix = "ion"
        suffix_type = "Derivational"

    else:
        root = word
        suffix = "-"
        suffix_type = "None"

    return root, suffix, suffix_type


print("\nMORPHOLOGICAL ANALYSIS")
print("-" * 75)
print(f"{'Word':<15}{'Root':<15}{'Suffix':<12}{'Type':<18}{'Normalized':<15}")
print("-" * 75)

for word in words:
    root, suffix, suffix_type = analyze_word(word)

    print(f"{word:<15}{root:<15}{suffix:<12}"
          f"{suffix_type:<18}{root:<15}")
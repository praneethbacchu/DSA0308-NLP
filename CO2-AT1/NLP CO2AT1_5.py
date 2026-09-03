words = ["relational", "relation", "relate"]


def porter_stem(word):

    original = word
    steps = []

    # Step 2: ational -> ate
    if word.endswith("ational"):
        word = word[:-6] + "e"
        steps.append("ATIONAL -> ATE: " + word)

    # Step 2: tional -> tion
    elif word.endswith("tional"):
        word = word[:-2]
        steps.append("TIONAL -> TION: " + word)

    # Step 4: remove ion
    if word.endswith("ion"):
        stem = word[:-3]

        if stem.endswith("at"):
            word = stem
            steps.append("ION removal: " + word)

    # Step 5: remove final e
    if word.endswith("e") and len(word) > 3:
        word = word[:-1]
        steps.append("E removal: " + word)

    return original, steps, word


print("\nPORTER STEMMER ANALYSIS")
print("-" * 80)
print(f"{'Original':<15}{'Applied Rules':<40}{'Final Stem':<15}")
print("-" * 80)

for word in words:

    original, steps, stem = porter_stem(word)

    rules = " | ".join(steps)

    print(f"{original:<15}{rules:<40}{stem:<15}")
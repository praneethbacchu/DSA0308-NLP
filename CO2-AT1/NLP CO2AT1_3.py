words = ["played", "player", "playing"]

def stem_word(word):

    if word.endswith("ing"):
        stem = word[:-3]
        affix = "ing"
        transformation = "Inflectional"

    elif word.endswith("ed"):
        stem = word[:-2]
        affix = "ed"
        transformation = "Inflectional"

    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        transformation = "Derivational"

    else:
        stem = word
        affix = "-"
        transformation = "None"

    return stem, affix, transformation


print("\nSTEMMING ANALYSIS")
print("-" * 85)
print(f"{'Original':<15}{'Stem':<15}{'Affix':<12}"
      f"{'Transformation':<20}{'Normalized':<15}")
print("-" * 85)

for word in words:
    stem, affix, transformation = stem_word(word)

    print(f"{word:<15}{stem:<15}{affix:<12}"
          f"{transformation:<20}{stem:<15}")
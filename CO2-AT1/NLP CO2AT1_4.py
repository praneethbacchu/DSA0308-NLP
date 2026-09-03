words = ["writes", "writing", "written"]

def finite_state_parser(word):

    if word == "writes":
        path = ["q0", "q1", "q2", "q3"]
        root = "write"
        morpheme = "write + s"
        pattern = "Regular Inflection"
        normalized = "write"

    elif word == "writing":
        path = ["q0", "q1", "q2", "q3"]
        root = "write"
        morpheme = "write + ing"
        pattern = "Regular Inflection"
        normalized = "write"

    elif word == "written":
        path = ["q0", "q1", "q_irregular", "q3"]
        root = "write"
        morpheme = "write → written"
        pattern = "Irregular Inflection"
        normalized = "write"

    else:
        path = ["q0", "q_reject"]
        root = word
        morpheme = "-"
        pattern = "Unknown"
        normalized = word

    return path, morpheme, root, pattern, normalized


print("\nFINITE-STATE MORPHOLOGICAL PARSER")
print("-" * 110)
print(f"{'Word':<12}{'State Path':<35}{'Morphology':<20}"
      f"{'Root':<12}{'Pattern':<22}{'Normalized':<12}")
print("-" * 110)

for word in words:

    path, morpheme, root, pattern, normalized = finite_state_parser(word)

    print(f"{word:<12}{' → '.join(path):<35}"
          f"{morpheme:<20}{root:<12}"
          f"{pattern:<22}{normalized:<12}")
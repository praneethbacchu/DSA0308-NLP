# HMM POS TAGGING USING VITERBI ALGORITHM
corpus = [
    [("The", "DT"), ("boy", "NN"), ("eats", "VBZ"), ("rice", "NN")],
    [("The", "DT"), ("girl", "NN"), ("drinks", "VBZ"), ("milk", "NN")],
    [("A", "DT"), ("cat", "NN"), ("drinks", "VBZ"), ("milk", "NN")],
    [("The", "DT"), ("dog", "NN"), ("chases", "VBZ"), ("cat", "NN")],
    [("A", "DT"), ("teacher", "NN"), ("teaches", "VBZ"), ("students", "NNS")],
    [("Students", "NNS"), ("study", "VBP"), ("English", "NN")],
    [("Birds", "NNS"), ("fly", "VBP"), ("high", "RB")],
    [("Children", "NNS"), ("play", "VBP"), ("games", "NNS")]
]
# Separate words and tags
print("WORDS AND POS TAGS")
for i, sentence in enumerate(corpus, 1):
    words = []
    tags = []
    for word, tag in sentence:
        words.append(word)
        tags.append(tag)
    print("\nSentence", i)
    print("Words:", words)
    print("Tags :", tags)
# Get POS states
states = []
for sentence in corpus:
    for word, tag in sentence:
        if tag not in states:
            states.append(tag)
print("\nPOS TAGS:", states)
# Count POS tags
tag_count = {}
for sentence in corpus:
    for word, tag in sentence:
        if tag not in tag_count:
            tag_count[tag] = 0
        tag_count[tag] += 1
print("\nPOS TAG COUNTS")
for tag in tag_count:
    print(tag, "=", tag_count[tag])
# Emission probabilities

emission_count = {}
for sentence in corpus:
    for word, tag in sentence:
        key = (word, tag)
        if key not in emission_count:
            emission_count[key] = 0
        emission_count[key] += 1
emission = {}
for key in emission_count:
    tag = key[1]
    emission[key] = emission_count[key] / tag_count[tag]
print("\nEMISSION PROBABILITIES")
for key in emission:
    print(
        key,
        "=",
        round(emission[key], 4)
    )
# Transition probabilities
transition_count = {}
from_tag_count = {}
for sentence in corpus:
    for i in range(len(sentence) - 1):
        current_tag = sentence[i][1]
        next_tag = sentence[i + 1][1]
        key = (current_tag, next_tag)
        if key not in transition_count:
            transition_count[key] = 0
        transition_count[key] += 1
        if current_tag not in from_tag_count:
            from_tag_count[current_tag] = 0
        from_tag_count[current_tag] += 1
transition = {}
for key in transition_count:
    current_tag = key[0]
    transition[key] = (
        transition_count[key] /
        from_tag_count[current_tag]
    )
print("\nTRANSITION PROBABILITIES")
for key in transition:
    print(
        key,
        "=",
        round(transition[key], 4)
    )
# Initial probabilities
initial_count = {}
for sentence in corpus:
    first_tag = sentence[0][1]
    if first_tag not in initial_count:
        initial_count[first_tag] = 0
    initial_count[first_tag] += 1
initial = {}
for tag in initial_count:
    initial[tag] = initial_count[tag] / len(corpus)
print("\nINITIAL PROBABILITIES")
for tag in initial:
    print(
        tag,
        "=",
        round(initial[tag], 4)
    )
# Viterbi Algorithm
sentence = ["The", "cat", "drinks", "milk"]
viterbi = []
backpointer = []
first_word = sentence[0]

v = {}
b = {}
for state in states:
    start_probability = initial.get(state, 0)
    emission_probability = emission.get(
        (first_word, state), 0
    )
    v[state] = (
        start_probability *
        emission_probability
    )
    b[state] = None
viterbi.append(v)
backpointer.append(b)
for i in range(1, len(sentence)):
    word = sentence[i]
    v = {}
    b = {}
    for current_state in states:
        best_probability = 0
        best_previous_state = None
        emission_probability = emission.get(
            (word, current_state), 0
        )
        for previous_state in states:
            transition_probability = transition.get(
                (previous_state, current_state), 0
            )
            probability = (
                viterbi[i - 1][previous_state]
                * transition_probability
                * emission_probability
            )
            if probability > best_probability:
                best_probability = probability
                best_previous_state = previous_state
        v[current_state] = best_probability
        b[current_state] = best_previous_state
    viterbi.append(v)
    backpointer.append(b)
# Find best final state
best_state = None
best_probability = 0
for state in states:
    if viterbi[-1][state] > best_probability:
        best_probability = viterbi[-1][state]
        best_state = state
# Backtracking
best_path = [best_state]
for i in range(len(sentence) - 1, 0, -1):
    previous_state = backpointer[i][best_path[0]]
    best_path.insert(0, previous_state)
# Final output
print("\nVITERBI RESULT")
for i in range(len(sentence)):
    print(sentence[i], "->", best_path[i])
print("\nFinal POS Sequence:")
print(best_path)
print("\nFinal Viterbi Probability:")
print(best_probability)
print("\nTagged Sentence:")
for i in range(len(sentence)):
    print(
        sentence[i] + "/" + best_path[i],
        end=" "
    )

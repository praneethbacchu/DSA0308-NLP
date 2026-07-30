import re

paragraph = """
Artificial Intelligence (AI) is transforming industries across the world.
AI is used in healthcare to assist doctors in diagnosis,
banking to detect fraud, and in education to provide personalized learning experiences.
Many companies invest heavily in AI research because AI improves efficiency
and enables intelligent decision-making.
As AI continues to evolve, professionals with AI skills are in high demand.
"""		

print("Original Paragraph:\n")
print(paragraph)

# Split into sentences
sentences = re.split(r'[.!?]+', paragraph)

print("\nSentences:")
count = 1
for sentence in sentences:
    sentence = sentence.strip()
    if sentence:
        print(f"{count}. {sentence}")
        count += 1

# Split into words
words = re.split(r'\s+', paragraph.strip())

print("\nWords:")
print(words)

print("\nTotal Sentences :", len([s for s in sentences if s.strip()]))
print("Total Words :", len(words))

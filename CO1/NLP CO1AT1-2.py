import re

paragraph = """
Artificial Intelligence (AI) is transforming industries across the world.
AI is used in healthcare to assist doctors in diagnosis,
banking to detect fraud, and in education to provide personalized learning experiences.
Many companies invest heavily in AI research because AI improves efficiency
and enables intelligent decision-making.
As AI continues to evolve, professionals with AI skills are in high demand.
"""

word = "AI"

match = re.search(word, paragraph)

if match:
    print("First occurrence found.")
    print("Starting Position :", match.start())
    print("Ending Position   :", match.end()-1)

    total = len(re.findall(word, paragraph))
    print("Total Occurrences :", total)

else:
    print("Word not found.")


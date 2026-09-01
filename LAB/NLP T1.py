from transformers import pipeline

# Create an English-to-French translator
translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)

# English text
english_text = "Hello, how are you? I am learning NLP."

# Translate English to French
result = translator(english_text)

# Display the translation
print("English:", english_text)
print("French:", result[0]["translation_text"])

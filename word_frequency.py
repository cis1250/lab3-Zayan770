#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True

# Prompt user for a valid sentence
user_sentence = input("Enter a sentence: ")
while not is_sentence(user_sentence): 
    print("Invalid sentence. Please try again.")
    user_sentence = input("Enter a sentence: ")

# Clean and split the sentence
sentence_clean = user_sentence.replace('.', '').replace(',', '').replace('!', '').replace('?', '').lower()
words = sentence_clean.split()

unique_words = []
frequencies = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)
        frequencies.append(1)
    else:
        index = unique_words.index(word)
        frequencies[index] += 1

for i in range(len(unique_words)):
    print(f"{unique_words[i]}: {frequencies[i]}")

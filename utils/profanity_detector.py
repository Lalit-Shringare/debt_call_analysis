import re

def load_bad_words(filepath='assets/profane_words.txt'):
    with open(filepath, 'r') as f:
        return set(word.strip().lower() for word in f)

def detect_profanity(conversation, speaker, bad_words):
    flagged = []
    for entry in conversation:
        if entry['speaker'] == speaker:
            text = entry['text'].lower()
            if any(re.search(rf'\b{re.escape(word)}\b', text) for word in bad_words):
                flagged.append(entry)
    return len(flagged) > 0, flagged

import re

VERIFICATION_KEYS = ['date of birth', 'address', 'social security']
SENSITIVE_KEYS = ['balance', 'account number']

def detect_violation(conversation):
    verified = False
    for entry in conversation:
        if entry['speaker'] == 'agent':
            text = entry['text'].lower()
            if any(kw in text for kw in VERIFICATION_KEYS):
                verified = True
            if any(kw in text for kw in SENSITIVE_KEYS):
                if not verified:
                    return True
    return False